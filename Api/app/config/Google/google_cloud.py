from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# ---------------- Credenciales ----------------
CLIENT_ID = "555554215317-dq8qrikftndl1ho2cm2r6i8cld22qpca.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REFRESH_TOKEN = "1//04OeAPQNBemsZCgYIARAAGAQSNwF-L9Irh03GfDEQbgcE0kttR7Glr3OjAaxawh9uutJCMePtC39KLNYrKRYvu_fbiMt7kqSm7o0"

creds = Credentials(
    None,
    refresh_token=REFRESH_TOKEN,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    token_uri="https://oauth2.googleapis.com/token"
)

drive_service = build("drive", "v3", credentials=creds)
docs_service = build("docs", "v1", credentials=creds)


