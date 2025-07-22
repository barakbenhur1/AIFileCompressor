import os
import zlib
import torch
from git_utils import ensure_repo, commit_and_push_model

MODEL_FILE = os.path.join(os.path.dirname(__file__), os.pardir, "model", "shared_model.pt")

def compress_file(filepath: str):
    ensure_repo()
    with open(filepath, "rb") as f:
        data = f.read()
    # maximum compression
    payload = zlib.compress(data, level=9)
    warning = None
    if len(payload) > len(data):
        warning = "⚠️ Compressed larger than original; storing original bytes."
        payload = data
    # save model (placeholder logic)
    # ... (existing model save & push)
    os.makedirs(os.path.dirname(MODEL_FILE), exist_ok=True)
    try:
        model = torch.load(MODEL_FILE)
    except:
        model = None
    # Placeholder: no training for demo
    torch.save(model, MODEL_FILE)
    commit_and_push_model()
    # write .aic
    base = os.path.splitext(os.path.basename(filepath))[0]
    out_name = f"{base}.aic"
    with open(out_name, "wb") as f:
        name_bytes = os.path.basename(filepath).encode()
        f.write(len(name_bytes).to_bytes(2, "big"))
        f.write(name_bytes)
        f.write(payload)
    return out_name, warning

def decompress_file(aic_path: str) -> str:
    ensure_repo()
    with open(aic_path, "rb") as f:
        name_len = int.from_bytes(f.read(2), "big")
        orig_name = f.read(name_len).decode()
        payload = f.read()
    data = zlib.decompress(payload)
    with open(orig_name, "wb") as f:
        f.write(data)
    return orig_name
