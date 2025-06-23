import gdown
import os

def download_from_drive(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_path, quiet=False)

os.makedirs("models", exist_ok=True)

# 👇 Replace with your real file IDs from Drive
download_from_drive("1z6TqdC1fa8hCc9__4YKFRBxagOlswstv", "models/model_caption.h5")
download_from_drive("1VNQ0jx1z7Si4xanmKLQbFiqZh1pZncCL", "models/maskrcnn_finetuned.pth")
