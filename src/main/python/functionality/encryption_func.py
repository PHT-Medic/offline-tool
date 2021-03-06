from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding, utils
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pickle
from io import BytesIO
import json
from typing import List, Union, BinaryIO


class FileEncryptor:
    """
    Performs symmetric encryption and decryption of sensitive files belonging to the train cargo
    """

    def __init__(self, key: bytes):
        self.fernet = Fernet(key)

    def decrypt_files(self, files: Union[List[str], List[BinaryIO]], binary_files=False):
        """
        Decrypt the given files using symmetric encryption
        :return:
        """
        print("Decrypting files..")
        if binary_files:
            # TODO evaluate memory consumption
            decr_files = []
            for i, file in enumerate(files):
                print(f"file {i + 1}/{len(files)}...", end="")
                data = self.fernet.decrypt(file.read())
                decr_files.append(BytesIO(data))
                print("Done")
            return decr_files
        for i, file in enumerate(files):
            print(f"File {i + 1}/{len(files)}...", end="")
            with open(file, "rb") as f:
                decr_file = self.fernet.decrypt(f.read())
            with open(file, "wb") as ef:
                ef.write(decr_file)
            print("Done")


def create_rsa_keys(password: str):
    """
    Generates a rsa private public key pair and returns their byte representation
    :return: rsa_private_key_pem
    :return: rsa_public_key_pem
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    private_key_pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                format=serialization.PrivateFormat.PKCS8,
                                                encryption_algorithm=serialization.BestAvailableEncryption(str.encode(password[0])))

    public_key = private_key.public_key()
    public_key_pem = public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                             format=serialization.PublicFormat.SubjectPublicKeyInfo)
    public_key_pem = public_key_pem.hex()

    return private_key_pem, public_key_pem


def store_keys(path: str, rsa_private_key_pem, rsa_public_key_pem, name):
    """
    Stores the given keys at the specified path
    :param path:
    :param rsa_private_key_pem:
    :param rsa_public_key_pem:
    :return:
    """

    with open(os.path.join(path, name + "_sk.pem"), "wb") as sk:
        sk.write(rsa_private_key_pem)
        print("Wrote " + name + " to " + path)
    with open(os.path.join(path, name + "_pk.pem"), "w") as pk:
        pk.write(rsa_public_key_pem)
        print("Wrote " + name + " to " + path)


def load_private_key(path: str, password: str):
    """
    Loads a private key from the given path
    :param path:
    :return:
    """

    with open(path, "rb") as key:
        try:
            if password[0] != "":
                try:
                    private_key = serialization.load_pem_private_key(key.read(),
                                                                     password=str.encode(password[0]),
                                                                     backend=default_backend())
                except:
                    private_key = "wrong_password"
                    return private_key
            else:
                private_key = serialization.load_pem_private_key(key.read(),
                                                                 password=None,
                                                                 backend=default_backend())
        except:
            private_key = "invalid"
            return private_key
        else:
            return private_key


def sign_hash(private_key: rsa.RSAPrivateKey, hash: bytes):
    """
    Creates an ecc signature using the provided private key and hash
    :param private_key: rsa private key
    :param hash: hash as byte object
    :return: DER encoded byte object representing the signature
    """
    signature = private_key.sign(hash,
                                 padding.PSS(
                                     mgf=padding.MGF1(hashes.SHA512()),
                                     salt_length=padding.PSS.MAX_LENGTH
                                 ),
                                 utils.Prehashed(hashes.SHA512()))
    return signature


def decrypt_symmetric_key(encrypted_sym_key: bytes, private_key: rsa.RSAPrivateKey):
    """
    Decrypts a given symmetric key using the private key of the user
    :param encrypted_sym_key: rsa encrypted symmetric key
    :param private_key: rsa private key
    :return:
    """

    decrypted_key = private_key.decrypt(
        encrypted_sym_key,
        padding=padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA512()),
            algorithm=hashes.SHA512(),
            label=None
        )
    )
    return decrypted_key


def decrypt_models(models: Union[List[str], List[os.PathLike]], sym_key: bytes):
    """
    Decrypts the given models using the provided symmetric key
    :param models: list of encrypted models
    :param sym_key: symmetric key
    :return: list of decrypted models
    """
    decr_models = []
    fernet = Fernet(sym_key)
    for model in models:
        with open(model, "rb") as mf:
            token = mf.read()
        fernet_decrypt = fernet.decrypt(token)
        decr_models.append(fernet_decrypt)
    return decr_models


def hash_string(hash_inp: str):
    hasher = hashes.Hash(hashes.SHA512(), default_backend())
    hasher.update(hash_inp.encode())
    return hasher.finalize()


def load_config(config: json):
    with open(config) as f:
        data = json.load(f)

    print(data)
    return data


def load_public_key(key: str):
    """
    Loads a public key
    :param key: string representation of a public key
    :return: public key object for asymmetric encryption
    """
    public_key = serialization.load_pem_public_key(bytes.fromhex(key),
                                                   backend=default_backend())
    return public_key


def verify_digital_signature(config: json):
    """
    Verifies the digital signature of the train_config by iterating over the list of signatures and verifying each one
    using the correct public key stored in the train configuration json

    :raise: InvalidSignatureError if any of the signed values can not be validated using the provided public keys

    """
    ds = config["digital_signature"]

    for sig in ds:
        try:
            public_key = load_public_key(
                config["rsa_public_keys"][sig["station"]])
        except:
            raise ValueError("Error loading public key")

        public_key.verify(bytes.fromhex(sig["sig"][0]),
                          bytes.fromhex(sig["sig"][1]),
                          padding.PSS(mgf=padding.MGF1(hashes.SHA512()),
                                      salt_length=padding.PSS.MAX_LENGTH),
                          utils.Prehashed(hashes.SHA512())
                          )
