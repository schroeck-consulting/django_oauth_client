#  _____      _                         _      _____ _____
# /  ___|    | |                       | |    |_   _|_   _|
# \ `--.  ___| |__  _ __ ___   ___  ___| | __   | |   | |
#  `--. \/ __| '_ \| '__/ _ \ / _ \/ __| |/ /   | |   | |
# /\__/ / (__| | | | | | (_) |  __/ (__|   <   _| |_  | |
# \____/ \___|_| |_|_|  \___/ \___|\___|_|\_\  \___/  \_/

"""
Settings class for OAuth
"""
import os


class OAuthSettings:
    """
    Settings for OAuth
    """

    env_key_client_id = "OAUTH_CLIENT_ID"
    env_key_client_secret = "OAUTH_CLIENT_SECRET"
    env_key_jwks_uri = "OAUTH_JWKS_URI"
    env_key_scope = "OAUTH_SCOPE"
    env_key_oauth_metadata_url = "OAUTH_METADATA_URL"

    def __init__(self):
        self.oauth_client_id: str = os.environ.get(self.env_key_client_id)
        self.oauth_client_secret: str = os.environ.get(
            self.env_key_client_secret)
        self.oauth_jwks_uri: str = os.environ.get(self.env_key_jwks_uri)
        self.oauth_scope: str = os.environ.get(self.env_key_scope)
        self.oauth_metadata_url: str = os.environ.get(
            self.env_key_oauth_metadata_url)


oauth_settings = OAuthSettings()
