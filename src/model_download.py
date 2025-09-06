
from dotenv import load_dotenv
import os
from pathlib import Path
from huggingface_hub import snapshot_download


load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN")

project_root = Path(__file__).resolve().parents[1]
local_dir = project_root / "model"
local_dir.mkdir(parents=True, exist_ok=True)

snapshot_download(
    repo_id="google/gemma-3-4b-it",
    local_dir=local_dir,
    token=token,
    local_dir_use_symlinks=False,
)

