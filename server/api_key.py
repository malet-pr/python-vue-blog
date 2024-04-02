from typing import Dict
import base64
import shortuuid

# In-memory storage --> reemplazar por redis
api_keys_storage: Dict[str, str] = {}

def generate_value(email: str, password: str):
    key = base64.b64encode(f"{email}:{base64.b64decode(password)}".encode())
    return key

def generate_api_key():
    return shortuuid.uuid()[:16] 

def check_api_key(api_key: str):
    return api_key in api_keys_storage

def store_key_value(key: str, value: str):
    api_keys_storage.update({key:value})

def get_user_email_from_api_key(api_key: str):
    decoded_data = base64.b64decode(api_keys_storage[api_key])
    decoded_string = decoded_data.decode('utf-8')
    return decoded_string.split(':')[0]

    

