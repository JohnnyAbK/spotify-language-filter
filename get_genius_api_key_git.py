import requests

CLIENT_ID = 'YOUR_GENIUS_CLIENT_ID'
CLIENT_SECRET = 'YOUR_GENIUS_CLIENT_SECRET'
REDIRECT_URI = 'YOUR_REDIRECT_URI'
AUTHORIZATION_CODE = 'CODE_FROM_STEP_4'

# Prepare the token exchange request
token_url = "https://api.genius.com/oauth/token"
data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'code': AUTHORIZATION_CODE,
    'redirect_uri': REDIRECT_URI,
    'grant_type': 'authorization_code'
}

# Request access token
response = requests.post(token_url, data=data)
response_data = response.json()
access_token = response_data['access_token']
print(access_token)