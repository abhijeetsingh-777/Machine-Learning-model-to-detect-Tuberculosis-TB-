# 🩻 TB-Detection-Hybrid-Model

> **A Medical AI System for the Early Detection of Tuberculosis from Chest X-Rays using Hybrid Feature Descriptors.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Overview
Tuberculosis (TB) is a serious infectious disease that affects the lungs. Early detection is critical but often difficult due to a shortage of radiologists in developing regions. 

This project implements a **Hybrid Deep Learning Model** that combines **Transfer Learning** (MobileNetV2) with **Hand-Engineered Features** (Gabor Filters & Canny Edge Detection). By feeding the AI not just the raw image, but also texture and structural edge data, the model achieves superior accuracy compared to standard CNNs.

## 🚀 Key Features
* **Hybrid Architecture:** Merges Deep Learning features with classical Computer Vision techniques.
* **High Accuracy:** Achieved **97.5% Validation Accuracy** on the test set.
* **Real-Time Diagnosis App:** Includes a user-friendly Jupyter Notebook interface (`Run_TB_App.ipynb`) with an upload button for instant prediction.
* **Lightweight:** Uses MobileNetV2, making it suitable for future edge/IoT deployment.

## 🧠 Methodology
Based on the research paper *"Early detection of tuberculosis using hybrid feature descriptors and deep learning network"*, this project processes images in three specific layers:

1.  **Layer 1 (Original):** The resized grayscale X-ray.
2.  **Layer 2 (Texture):** Applied **Gabor Filter** to highlight lung tissue textures and abnormalities.
3.  **Layer 3 (Structure):** Applied **Canny Edge Detection** to emphasize the rib cage and lung boundaries.

These three layers are stacked into a composite image and fed into a pre-trained **MobileNetV2** network for classification.

## 📊 Results
| Metric | Score |
| :--- | :--- |
| **Validation Accuracy** | **97.50%** |
| **Validation Loss** | 0.07 |
| **Training Epochs** | 10 |

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/AkshatMishra123/Machine-Learning-model-to-detect-TB.git](https://github.com/AkshatMishra123/Machine-Learning-model-to-detect-TB.git)
cd Machine-Learning-model-to-detect-TB
