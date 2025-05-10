# Car Image Classification Project

![Car Classification Banner](https://miro.medium.com/v2/resize:fit:1400/0*tH9evuOFqk8F41FG.png)

## 📋 Overview
This project implements a deep learning model that can identify **120 different car brands** from images with 75% accuracy. Built on ResNet50 architecture, the model excels at distinguishing between visually similar car models under varied lighting conditions and camera angles.

## 📁 Project Structure

- `car-classifierv1.ipynb`: Original model training implementation
- `car-classifier.ipynb`: Improved version with advanced training techniques
- `test-model.ipynb`: Tools for evaluating and visualizing model predictions
- `csv-prep.ipynb`: Data preparation and CSV processing utilities
- `price-predictor.ipynb`: Experimental price prediction component
- `/models/`: Directory for storing trained model weights
- `/cache/`: Cached preprocessed data and training states
- `/data/`: Processed image data organized by class
- `/images/`: Raw car image datasets

## 🚗 Features

- **Multi-class Image Classification** - Identifies car brands from standard images
- **Transfer Learning** - Leverages pre-trained ResNet50 model fine-tuned on car data
- **Advanced Data Processing** - Uses comprehensive augmentation and class balancing
- **Progressive Training** - Employs gradual layer unfreezing for optimal learning

## 🔧 Technical Implementation

### Data Processing
- **Smart Brand Detection** - Automatically extracts car brands from filenames
- **Balanced Dataset Creation** - Uses stratified splitting for representative data distribution
- **Enhanced Augmentation** - Implements rotations, flips, color shifts, and erasing
- **Performance Optimization** - Employs caching mechanism for faster data loading

![image](https://github.com/user-attachments/assets/e359fac9-ceeb-4b21-9e7e-c1bbd33ede8f)

### Model Architecture
```python
nn.Sequential(
    nn.Linear(2048, 2048),
    nn.BatchNorm1d(2048),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(2048, 1024),
    nn.BatchNorm1d(1024),
    nn.ReLU(),
    nn.Dropout(0.3),
    nn.Linear(1024, num_classes)
)
```

### Advanced Training Techniques
- **Class-weighted Loss** - Addresses class imbalance in training data
- **Optimized Learning Rate** - Uses OneCycleLR scheduler
- **Gradient Accumulation** - Enables larger effective batch sizes

## 📊 Performance & Visualization

- **75% Accuracy** across 120 car brands
- **Interactive Testing Tools**:
  - Confusion matrix visualization
  - Random image classification with confidence scores
  - External image testing
  - Confidence threshold analysis

## 🖥️ Setup Requirements

### Recommended Hardware
- **RAM**: 8GB minimum
- **CPU**: Intel i5 9000+ / i7 9000+ / AMD Ryzen 5 5000+
- **GPU**: NVIDIA GTX 1660 4GB or AMD Radeon RX 6000+ series

### Installation Instructions

1. **Installation**
   ```bash
   git clone https://github.com/RiadDePauwUCLL/car-brand-prediction.git
   cd car-brand-prediction
   ```

2. **Download Required Files**
   - Get all necessary files from [this Google Drive folder](https://drive.google.com/drive/folders/1k8kXTguWizL66vKi5Zhq11R6zXZ9i8tI?usp=sharing)
   - Place `75acc.pth` model in the $./models/$ folder
   - Add cached files to the cache directory
   - Extract the `cars5` folder to images (It's over 10GB, make sure you have at least 15GB free)

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Process Cached Transforms**
   - Open test-model.ipynb
   - Run the **Data preparation** section
   - Wait for caching to complete (20 min to 2 hours depending on hardware)

5. **Start Model Evaluation**
   - Proceed to the **Model evaluation** section
   - Test with provided or custom images

## 🔍 Applications

- **Automated Vehicle Identification** in images and video
- **Demographic Analysis** of vehicle distribution
- **Integration** into larger monitoring systems
- **Educational Tool** for demonstrating deep learning techniques

---

*Developed with PyTorch, TorchVision, and PyTorch DirectML*
