tokenvlue.py

# Sample token
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

def get_value_from_token(token: str, key: str):
    try:
        payload = jwt.decode(token, options={"verify_signature": False})
        return payload.get(key)
    except jwt.JWTError as e:
        print(f"Error decoding token: {e}")
        return None

token_value = get_value_from_token(token, "sub")
print("Value:", token_value)
