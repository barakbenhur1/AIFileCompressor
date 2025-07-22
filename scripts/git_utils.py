import os
from git import Repo, GitCommandError

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
GITHUB_REPO_URL = "https://github.com/barakbenhur1/AIFileCompressor.git"
MODEL_PATH = os.path.join(PROJECT_ROOT, "model", "shared_model.pt")

def ensure_repo():
    # Clone if not present, else pull
    if not os.path.isdir(os.path.join(PROJECT_ROOT, ".git")):
        Repo.clone_from(GITHUB_REPO_URL, PROJECT_ROOT)
    else:
        repo = Repo(PROJECT_ROOT)
        try:
            repo.remotes.origin.pull()
        except GitCommandError as e:
            print(f"[git_utils] Warning: pull failed: {e}")

def commit_and_push_model():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        # Fallback to reading from .token file
        token_path = os.path.join(PROJECT_ROOT, ".token")
        if os.path.isfile(token_path):
           token = open(token_path).read().strip()
        else:
            raise RuntimeError("GITHUB_TOKEN not found in env var or .token file")
    if not token:
        raise RuntimeError("GITHUB_TOKEN not set")
    repo = Repo(PROJECT_ROOT)
    repo.git.add(MODEL_PATH)
    repo.index.commit("Update shared_model.pt")
    remote = GITHUB_REPO_URL.replace("https://", f"https://{token}@")
    repo.remotes.origin.set_url(remote)
    repo.remotes.origin.push()
