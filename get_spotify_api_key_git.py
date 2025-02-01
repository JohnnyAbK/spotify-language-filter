import requests
import base64

CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
REDIRECT_URI = 'YOUR_REDIRECT_URI'
AUTHORIZATION_CODE = 'CODE_FROM_STEP_1'

# Prepare the token exchange request
token_url = "https://accounts.spotify.com/api/token"
headers = {
    'Authorization': f'Basic {base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()}',
}
data = {
    'grant_type': 'authorization_code',
    'code': AUTHORIZATION_CODE,
    'redirect_uri': REDIRECT_URI
}

# Request access token
response = requests.post(token_url, headers=headers, data=data)
response_data = response.json()
access_token = response_data['access_token']
print(access_token)
