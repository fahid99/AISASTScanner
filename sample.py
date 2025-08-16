import random
import hashlib
import os

# Insecure password reset token generation
def generate_reset_token(email):
    seed = random.randint(100000, 999999)
    token = hashlib.sha256(f"{email}{seed}".encode()).hexdigest()
    return token

# Insecure storage of API key in code
API_KEY = "AKIAIOSFODNN7EXAMPLE"

# Hardcoded credentials
def connect_to_db():
    username = "admin"
    password = "password123"
    return f"Connected to DB with {username}:{password}"

# Insecure temp file creation
def write_temp_data(data):
    temp_file = "/tmp/tempfile.txt"
    with open(temp_file, "w") as f:
        f.write(data)
    return temp_file

# Weak file permissions
def save_config(config):
    with open("config.cfg", "w") as f:
        f.write(config)
    os.chmod("config.cfg", 0o777)