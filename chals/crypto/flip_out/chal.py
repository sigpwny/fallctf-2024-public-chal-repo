from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import json
import os


KEY = bytes(os.environ['KEY'], 'utf-8')
FLAG = bytes(os.environ['FLAG'], 'utf-8')

class AuthSys:
    def __init__(self, key: bytes):
        self.key = key

    def encrypt(self, data: bytes) -> bytes:
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(pad(data, AES.block_size))

    def decrypt(self, data: bytes) -> bytes:
        iv, encrypted_data = data[:AES.block_size], data[AES.block_size:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(encrypted_data), AES.block_size)

def authenticate_by_credentials(aes_cipher: AuthSys) -> dict:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    is_admin_flag = username == "root" and password == FLAG.decode()

    user_data = {"admin": int(is_admin_flag)}
    login_token = aes_cipher.encrypt(json.dumps(user_data).encode())
    print(f"Welcome {username}, Here is your login token: {login_token.hex()}")

    return user_data

def authenticate_by_token(aes_cipher: AuthSys) -> dict:
    token_hex = input("Please enter your login token: ")
    token_bytes = bytes.fromhex(token_hex)

    user_data_json = aes_cipher.decrypt(token_bytes)
    return json.loads(user_data_json)

def main() -> None:
    print("Welcome to Sigpwny! Please login. If you aren't already here, we will make an account for you.")
    choice = input("How do you want to sign in?\n1) Credentials \n2) Token\n\nEnter your choice: ")
    auth = AuthSys(KEY)

    if choice == "1":
        user_data = authenticate_by_credentials(auth)
    elif choice == "2":
        user_data = authenticate_by_token(auth)
    else:
        print("Hey! That isn't a valid login method.")
        exit(-1)

    if user_data.get("admin") == 1:
        print("Congrats on your promotion!\nHere's your certificate: " + FLAG.decode())
    else:
        print("Welcome to the club!")

    exit(0)

if __name__ == "__main__":
    main()