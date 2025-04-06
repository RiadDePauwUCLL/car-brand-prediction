# Car Price Production: what's the approach?

> - **Car Price prediction**: using images & datasets.
> 	- **Convolutional Neural Networks & Computer Vision**
> 	- **NumPy, PyTorch, Pandas, Matplotlib, Seaborn, TensorFlow/Keras**
> 	- **Deep Learning, Transfer Learning & Machine Learning**

- We are going to focus **primarily on using pictures of cars & a probable mix of datasets online**. We would be using some sort of image classification.
- We are going to find a way on making predictions with a decent accuracy for the prices of the cars. It's important that the prices are going to be fair.
- Have a visual approach with datasets aka data visualization, hence e.g. Pandas & Matplotlib/Seaborn.
- Being able to separate diverse data coming from all over world, e.g. currency or car brands.


---

## The scope of the CNN 

The most important part of the project is understanding that how the CNN is going to proceed on classifying the vehicles. *It should also be able to distinguish if it's a car or not.*

- Car Brands(Tesla, BMW, Toyota)
- Car Models(X6M, Model T, Supra)
- Car Types(SUV, Coupe, Sports)
- Car Features(electric, gasoline, race-car like a F1-car,...)

Understanding the differences is important & key for the CNN, else we won't be able to determine a decent & accurate prediction regarding the price of that specific car.

### Collection & preparation of the data

The sole focus is going to be on the images, sure, but let's make it easier for the CNN & combine it with existing dataset. Having more context on vehicles might genuinely help the AI understanding how to figure out what the price of a car can be.

- Existing Datasets
- Scraped Images: let's try to use as much copyright-free pictures as possible
- Data Augmentation


### What kind of CNN Model are we talking about?

So here's the fun part. We have 2 ways of doing this, depending on the level of the complexity.

- Train from Scratch: Use a large dataset(100k+ images).
- Use Transfer Learning: Small dataset & a fine-tune a pretrained model like any of these 3:
	- Resnet50
	- VGG16
	- EfficientNet

Here's an example I found online that uses TensorFlow/Keras with Transfer Learning:
```python
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model

# Load pre-trained ResNet50
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze base model layers
for layer in base_model.layers:
    layer.trainable = False

# Add custom classification head
x = Flatten()(base_model.output)
x = Dense(512, activation='relu')(x)
x = Dense(128, activation='relu')(x)
output = Dense(num_classes, activation='softmax')(x)

# Build model
model = Model(inputs=base_model.input, outputs=output)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train on your dataset
model.fit(train_data, epochs=10, validation_data=val_data)

```


### Train & fine-tune the model

- Using [^1]***Categorical Cross Entropy*(CCE)^^** loss for multi-class classification.
- Adjust learning rate & use early stopping to prevent overfitting.
- Use a GPU (depending on the pc, NVIDIA CUDA or AMD) to make the training faster.

> [!NOTE]
> 
> ###### Mathematical Representation of Categorical Cross-Entropy
> 
> The categorical cross-entropy formula is expressed as:
> 
> ![image](https://github.com/user-attachments/assets/26dec808-2eea-4c5b-a8a8-e653a0e5eb46)
> 
> Where:
> 
> - L(y,y^)L(y,y^​) is the categorical cross-entropy loss.
> - yiyi​ is the true label (0 or 1 for each class) from the one-hot encoded target vector.
> - y^iy^​i​ is the predicted probability for class ii.
> - CC is the number of classes.
> ---
> Source: https://www.geeksforgeeks.org/categorical-cross-entropy-in-multi-class-classification/


### Evaluation & Deployment

Testing the model out on images & datasets. Figuring out how to constantly improve it & maybe even have a possibility of deploying it in the future.

### For the deployment
- Converting to TensorFlow Lite on edge devices
- Using a REST API like Flask or FastAPI


----

## The scope of the Data Import & Preprocessing

The title says it all. We need to correctly import the data & make sure we clean it before starting up any work with it.


### What's the take here?

Having some data to help making the model learn & predict a more accurate price regarding a specific car. The more confident/precise it is, the better.

### What are the steps?

1. Data Importation: making sure it's valid & up-to-date.
2. Cleaning the data: dropping missing/incorrect & duplicated data from rows & columns.
3. Data Visualization: Visualize the connections & coalitions of all columns with each-other. 
4. Compiling & Training the models: Splitting the preprocessed data & finding out the best possible models.
5. Evaluation: Feeding the data into a deep learning model & then proceed with a comparison of prices of the datasets with the predictions of the images themselves.


---

## How will the process go?

For now, I just have it figured out to what I'm going to use and how I'm going to proceed. But it's definitely a great start. 

What we might also have to try out, is to make a better visual representation of how this model is going to show the output of it's own work. 
**I will try to make a website where you can proceed with uploading the image of a car & make it predict the price of that specific car.**


---

## How to start & use

Make sure you download the images and **save them inside the /images folder**(**Have at least 10GB on ur disk free**, or else the models won't be able to process the data):
- https://drive.google.com/file/d/1TZC1AHUvbeDF70HcpLYZ5xL3_J07PKV0/view?usp=sharing
- Create an .env file... **WIP**


---

## Sources

> [!NOTE]
> 
> **Image Classification using CNN**
> - https://www.analyticsvidhya.com/blog/2020/02/learn-image-classification-cnn-convolutional-neural-networks-3-datasets/
> - https://www.kaggle.com/code/anandhuh/image-classification-using-cnn-for-beginners
> - https://www.geeksforgeeks.org/image-classifier-using-cnn/
> 

> [!NOTE]
> Datasets
> - https://github.com/YBIFoundation/Dataset/blob/main/Car%20Price.csv
> - https://public.opendatasoft.com/explore/dataset/all-vehicles-model/table/?sort=modifiedon
>
> 
> Images
> - Mostly scraped from https://www.pexels.com/search/audi%20car/
> - Rest of images we're found through random datasets online, mainly copyright free.

---

## Annotations

[^1]: It's known as a softmax loss or log loss, a commonly used function in machine learning. It's particularly used for classification problems. It measures the difference between the predicted probability distribution & the actual (true) distribution of classes. 
	**TL;DR Function helps a ML model to determine how true the predictions are from the true labels, guiding it into learning to make more accurate predictions.**
