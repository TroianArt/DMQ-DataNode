import jwt
from .. import rsa_key


def verify_token(token):
    try:
        payload = dict(jwt.decode(token, key=rsa_key, algorithms='RS256'))
        return payload['permissions']
    except jwt.ExpiredSignatureError:
        return 'Your token has expired'
    except jwt.InvalidTokenError:
        return 'Invalid token'
