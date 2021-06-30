from pathlib import Path
import platform
import traceback
import json
import sys
import os


try:
    port = int(os.environ.get("PORT", "8080"))
except Exception as e:
    print(e)
    port = -1
if not 1 <= port <= 65535:
    print(
        "Please make sure the PORT environment variable is an integer between 1 and 65535"
    )
    sys.exit(1)

try:
    api_id = int(os.environ["API_ID","1813445"])
    api_hash = os.environ["API_HASH","8f45dabd56be5ad1619df16af9eca560"]
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    index_settings_str = os.environ["INDEX_SETTINGS","{\n"index_all": false,\n"index_private":false,\n"index_group": false,\n"index_channel": true,\n"exclude_chats": [],\n"include_chats": ["-1001404974777"]\n}"].strip()
    index_settings = json.loads(index_settings_str)
except:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = os.environ["SESSION_STRING","BQBImQwNKi7sah7jXUvXUrwM3bYktU0Qw2DeBSNxwYuDXjTJUIJOBEpJKtZ6TnpJp6rk3SVKJtbsgFIVinrcXgeN68ixk2LGA1GxFv_tO8OjC8668XqgOF0QAW-uvQeC4DghoIhN-Oh_S97iezfkNUAv9Uzv_nOpYNCwioJ0plARRLpvkZm5eAC3IGti9i3efvkCCKL30-U_GAuovVum8s6-4csnvMStIHYeiC69jsOQIjDdIaPvfIAAWDXG4vtJlZaZkfhi6M1BACNtlu0-NssFe3kZ8LYuQTrId0NXbxCOF5jvkoGL3bnkP_Me3FWGb5cWCE66JeiJU4Xx9p9yVGZLU2K9uQA"]
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
block_downloads = bool(os.environ.get("BLOCK_DOWNLOADS"))
results_per_page = int(os.environ.get("RESULTS_PER_PAGE", "20"))
logo_folder = Path("./Temp/logo/" if platform.system() == "Windows" else "/tmp/logo")
if not logo_folder.exists():
    logo_folder.mkdir(parents=True)
username = os.environ.get("TGINDEX_USERNAME", "")
password = os.environ.get("PASSWORD", "")
SHORT_URL_LEN = int(os.environ.get("SHORT_URL_LEN", 3))
authenticated = bool(username and password)
SESSION_COOKIE_LIFETIME = int(os.environ.get("SESSION_COOKIE_LIFETIME") or "60")
try:
    SECRET_KEY = os.environ["SECRET_KEY"]
    if len(SECRET_KEY) != 32:
        raise ValueError("SECRET_KEY should be exactly 32 charaters long")
except (KeyError, ValueError):
    if authenticated:
        traceback.print_exc()
        print("\n\nPlease set the SECRET_KEY environment variable correctly")
        sys.exit(1)
    else:
        SECRET_KEY = ""
