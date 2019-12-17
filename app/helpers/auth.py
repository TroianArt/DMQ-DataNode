import jwt
from ..routes.connect import SECRET


def verify_token(token):
    try:
        payload = dict(jwt.decode(token, key=SECRET, algorithms='HS256'))
        print(payload)
        return payload['permissions']
    except jwt.ExpiredSignatureError:
        return 'Your token has expired'
    except jwt.InvalidTokenError:
        return 'Invalid token'
