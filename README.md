How to Obtain Authorization Tokens for Genius and Spotify
1) Getting Spotify Access Token

Spotify uses the OAuth 2.0 authorization flow to allow applications to access a user's data. To get the access token for Spotify:
Steps:
  
  1. Go to Spotify Developer Dashboard:
      . Visit: [Spotify Developer Dashboard](https://developer.spotify.com/).
      . Log in with your Spotify account or create one if you don't have one.
  
  2. Create a New Application:
      . Click "Create an App" to create a new Spotify application.
      . Fill in the application details. For personal use, you can set the Redirect URI to something like http://localhost:9999/spotify.
  
  3. Obtain Client ID and Client Secret:
      . After creating the app, you'll be given a Client ID and Client Secret. Save them for later.
  
  4. Use Spotify’s Authorization Code Flow.
  To get the Access Token for your app, perform the following steps:

    Step 1: Request Authorization Code
    Open your browser and go to this URL, replacing YOUR_CLIENT_ID with your Client ID and YOUR_REDIRECT_URI with the one you set earlier:
    https://accounts.spotify.com/authorize?client_id={YOUR_CLIENT_ID}&response_type=code&redirect_uri={YOUR_REDIRECT_URI}&scope=user-library-read
    This will take you to a page asking for permission to access your account. After allowing it, you'll be redirected to YOUR_REDIRECT_URI with a code in the URL query.
  
    Step 2: Exchange the Authorization Code for Access Token
    Use the Python script in the repository (get_spotify_api_key_git.py) to exchange the authorization code for an access token.
  
  5. Store the Access Token
  Once you have the access_token, save it securely as it will be used to authenticate API requests to Spotify.

2) Getting Genius API Token (Access Token)

Genius requires OAuth for authentication, and you will need to register your app with Genius to get the Client ID and Client Secret.
Steps:

  1. Go to Genius Developer Dashboard:
    . Visit: [Genius Developer](https://docs.genius.com/).
    . Log in or sign up for an account.

  2. Create a New API Client:
    . Once logged in, go to "Create an API Client".
    . Fill in the required details for the app. For Redirect URI, you can use http://localhost:8888/genius.

  3. Obtain Client ID and Client Secret:
    . After creating the app, you’ll get a Client ID and Client Secret. Save these credentials.

  4. Get Authorization Code.
  To get the authorization code, perform the following steps:

    Step 1: Request Authorization Code
    Open your browser and go to this URL, replacing YOUR_CLIENT_ID with your Client ID and YOUR_REDIRECT_URI with the one you set earlier:
    https://api.genius.com/oauth/authorize?client_id={YOUR_CLIENT_ID}&redirect_uri={YOUR_REDIRECT_URI}&response_type=code
    After allowing permissions, you will be redirected to the YOUR_REDIRECT_URI with a code in the URL query.

    Step 2: Exchange the Authorization Code for Access Token
    Use the Python script in the repository (get_genius_api_key_git.py) to exchange the authorization code for the access token.
  5. Store the Access Token
  Once you receive the access_token from Genius, save it securely as you’ll use it for API requests.
