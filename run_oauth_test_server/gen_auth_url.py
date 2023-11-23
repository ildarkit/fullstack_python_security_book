#! env python

import os
import random
import string
import base64
import hashlib


CLIENT_ID = 'Dhn3Uq49caY6gR4ZuoWXRcSxvxcHglGzaYn7UkEQ'
CLIENT_SECRET = 'zDLpojbKHp0zfsqIn5bZu4EaQV0F3UH7ctCweTY5fE11AnkNH4Iqfsm9CfRdghTE7tbYQjt9RgKKGq7Mkj2eLHLPD2dQaPp3MpZ2MtMnbbxm4Fo3Seh6Jzb57Mu5STJ8'
REDIRECT_URL = 'https://localhost:8000/callback/'
AUTH_URL = 'https://localhost:8000/o/authorize/?response_type=code&code_challenge={code_challenge}&code_challenge_method=S256&client_id={client_id}&redirect_uri={redirect_uri}'


if __name__ == '__main__':
    code_verifier = ''.join(
        random.choice(
            string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128))
    ) 
    code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
    print(f'{CLIENT_ID=}')
    print(f'{CLIENT_SECRET=}')
    print(f'{code_verifier=}')
    print(f'{code_challenge=}')
    print(AUTH_URL.format(code_challenge = code_challenge, client_id = CLIENT_ID, redirect_uri = REDIRECT_URL))


