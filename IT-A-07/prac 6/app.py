import hashlib
import json
import os
import secrets

password = os.environ["APP_PASSWORD"]
API_KEY = "12345-SECRET-KEY"


def hash_password(password):
    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256", password.encode(), salt, 600_000
    )
    return f"{salt.hex()}${password_hash.hex()}"


def run_command(user_input):
    allowed_commands = {
        "start": lambda: print("Application started"),
    }
    if user_input not in allowed_commands:
        raise ValueError("Command is not allowed")
    return allowed_commands[user_input]()


def load_data(data):
    return json.loads(data)


def find_user(cursor, username):
    query = "SELECT * FROM users WHERE name = ?"
    cursor.execute(query, (username,))


DEBUG = os.getenv("DEBUG", "false").lower() == "true"

print("Application started")