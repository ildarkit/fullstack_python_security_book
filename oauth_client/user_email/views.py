import ssl
import random
import string
import base64
import hashlib

from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.cache import cache
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth


CLIENT_ID = r'Dhn3Uq49caY6gR4ZuoWXRcSxvxcHglGzaYn7UkEQ'
CLIENT_SECRET = r'zDLpojbKHp0zfsqIn5bZu4EaQV0F3UH7ctCweTY5fE11AnkNH4Iqfsm9CfRdghTE7tbYQjt9RgKKGq7Mkj2eLHLPD2dQaPp3MpZ2MtMnbbxm4Fo3Seh6Jzb57Mu5STJ8'
AUTH_SERVER = 'https://localhost:8000'
AUTH_FORM_URL = f'{AUTH_SERVER}/o/authorize/'
TOKEN_EXCHANGE_URL = f'{AUTH_SERVER}/o/token/'
REVOKE_TOKEN_URL = f'{AUTH_SERVER}/o/revoke_token/'
RESOURCE_URL = f'{AUTH_SERVER}/oauth/hello/'


def generate_pkce():
    code_verifier = ''.join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128))
    )
    code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
    code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
    return code_verifier, code_challenge


class WelcomeView(View):
    def get(self, request):
        access_token = request.session.get('access_token')
        client = OAuth2Session(CLIENT_ID, token=access_token)
        ctx = {}

        if not access_token:
            code_verifier, code_challenge = generate_pkce()
            url, state = client.authorization_url(
                AUTH_FORM_URL,
                code_challenge=code_challenge,
                code_challenge_method='S256',
            ) 
            ctx['authorization_url'] = url
            cache.set(state, code_verifier, 30) 
        else:
            response = client.get(RESOURCE_URL, verify=ssl.get_default_verify_paths().capath)
            ctx['email'] = response.json()['email']

        return render(request, 'welcome.html', context=ctx)


class OAuthCallbackView(View):
    def get(self, request):
        state = request.GET.get('state', None)
        client = OAuth2Session(CLIENT_ID, state=state)

        redirect_uri = request.build_absolute_uri()
        access_token = client.fetch_token(
            TOKEN_EXCHANGE_URL,
            client_secret=CLIENT_SECRET,
            code_verifier=cache.get(state),
            authorization_response=redirect_uri,
            verify=ssl.get_default_verify_paths().capath,
        )
        request.session['access_token'] = access_token
        
        return redirect(reverse('welcome'))
