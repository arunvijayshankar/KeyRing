import os.path
from cryptography.fernet import Fernet
import redis

sym_key_path = ''


def get_sym_key():
    if os.path.exists(sym_key_path):
        with open(sym_key_path, "r") as f:
            sym_key = f.readlines()
        return sym_key[0].encode()
    else:
        with open(sym_key_path, "w") as f:
            sym_key = Fernet.generate_key()
            f.write(sym_key.decode())
        return sym_key


def get_cipher():
    return Fernet(get_sym_key())


def encrypt_val(val):
    cipher = get_cipher()
    if val:
        return cipher.encrypt(val.encode("utf-8"))
    else:
        print("Error: Cannot encode empty strings")


def decrypt_val(val):  # move to utils
    cipher = get_cipher()
    if val:
        return cipher.decrypt(val)
    else:
        print("Error: Cannot decode empty strings")


def init_redis():       # maybe a with/as statement?
    r = redis.Redis(host="localhost", port=9028, db=0)
    return r


def kill_redis_conn(r):
    client_id = r.client_id()
    r.client_kill_filter(_id=client_id)
