# 🧠 Image Captioning + Instance Segmentation (COCO 2017)

This project combines two powerful deep learning pipelines:

- 📸 **Image Captioning** using TensorFlow (EfficientNetB0 + LSTM)
- 🟣 **Instance Segmentation** using PyTorch (Mask R-CNN)
- 🔗 Integrated: Given any input image, it generates a caption and overlays object masks.

> No model files are stored in the repo — they are downloadable via Google Drive.

---

## 🧰 Tech Stack

### 🧠 Deep Learning Frameworks
- **TensorFlow 2.x** – for image captioning (EfficientNetB0 + LSTM)
- **PyTorch** – for instance segmentation (Mask R-CNN with torchvision)

### 🖼️ Computer Vision
- **EfficientNetB0** – CNN feature extractor
- **LSTM** – decoder for caption generation
- **Mask R-CNN (ResNet50 FPN)** – pretrained on COCO for instance segmentation

### 📊 Dataset
- **COCO 2017** – used for both captioning (`captions_train2017.json`) and segmentation (`instances_train2017.json`)

### 📦 Supporting Libraries
- `numpy`, `opencv-python`, `matplotlib` – image handling and visualization
- `pycocotools` – for parsing COCO annotations
- `gdown` – for downloading large model files from Google Drive




