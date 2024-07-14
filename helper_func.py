from config import GIT_USER_NAME, GIT_REPO_NAME, GIT_PAT
import requests
import base64
from datetime import datetime
import requests

def encode_to_base64(input_string):
    input_bytes = input_string.encode("utf-8")
    encoded_bytes = base64.b64encode(input_bytes)
    encoded_string = encoded_bytes.decode("utf-8")
    return encoded_string


def get_file_sha():
    github_username = GIT_USER_NAME
    repo_name = GIT_REPO_NAME
    path = "registered.txt"
    url = f"https://api.github.com/repos/{github_username}/{repo_name}/contents/{path}"
    headers = {
        "Authorization": f"Bearer {GIT_PAT}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("sha")
    else:
        return None

def setup_github_and_push():
    existing_sha = get_file_sha()
    github_username = GIT_USER_NAME
    repo_name = GIT_REPO_NAME
    path = "registered.txt"
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    commit_message = f"{current_time}"
    url = f"https://api.github.com/repos/{github_username}/{repo_name}/contents/{path}"
    headers = {
        "Authorization": f"Bearer {GIT_PAT}",
        "Accept": "application/vnd.github+json",
    }
    if existing_sha is None:
        with open(path, "rb") as file:
            content = file.read().decode("utf-8")
            encoded_content=encode_to_base64(content)
            data = {
                "message": f"{commit_message}",
                "content": encoded_content,
                "branch": 'main',
            }
    else:
        with open(path, "rb") as file:
            content = file.read().decode("utf-8")
            encoded_content=encode_to_base64(content)
            data = {
                "message": f"{commit_message}",
                "content": encoded_content,
                "branch": 'main',
                "sha": existing_sha
            }
    
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 201:
        return True
    if response.status_code == 200:
        return True
    else:
        return False
   
def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time

def register_device(device_id):
    try:
        registered_ids = set() 
        with open("registered.txt", "r") as file:
            for line in file:
                registered_ids.add(line.strip())

        if device_id not in registered_ids:
            with open("registered.txt", "a") as file:
                file.write(f"{device_id}\n")
            setup_github_and_push()
            return True
        return True

    except Exception as e:
        print(e)
        return False

async def progress(current, total):
    print(f"{current * 100 / total:.1f}%")
