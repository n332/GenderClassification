# GenderClassification
The objective of this project is to develop a Convolutional Neural Network (CNN) model that can accurately classify images into two categories: male and female. To prepare the images for classification, OpenCV (CV2) is utilized to crop faces from the images. The classification process is based on a simple CNN algorithm

## methodology
To prepare the images for classification, OpenCV (CV2) is utilized to crop faces from the images.
The classification process is based on a simple CNN algorithm

![FaceDetected](Pic/face_Detected.png)

![(Pic/1.png)](https://github.com/n332/GenderClassification/blob/main/Pic/1.png) ![Pic/2.png](https://github.com/n332/GenderClassification/blob/main/Pic/2.png) ![Pic/3.png](https://github.com/n332/GenderClassification/blob/main/Pic/3.png) ![Pic/4.png](https://github.com/n332/GenderClassification/blob/main/Pic/4.png) ![Pic/5.png](https://github.com/n332/GenderClassification/blob/main/Pic/5.png)

## Data
[Dataset on kaggle]([Model/TheFinalModelGenderClassification9680.h5](https://www.kaggle.com/datasets/cashutosh/gender-classification-dataset/))
- Training :47009

![Training](Pic/trainDist.png)
  
- Validation: 11649
  
![Validation](Pic/ValDist.png)
  
  *Note : This set is splited to : 2,336 for testing and 9,313 for validation
- Samples:

![Samples](Pic/Samples.png) 

## Training

### Augmentation
- RandomFlip("horizontal")
- RandomRotation(0.1)
- RandomZoom(0.1)
- RandomBrightness(factor=0.2)
- RandomContrast(factor=0.2)

### Callbacks
- LearningRateScheduler
- EarlyStopping (monitor='val_loss', patience=3)

### Model Architecture
![Model Architecture](Pic/Archi.png)


### Compilation Parameters
- Adam : initial_lr = 0.0001, Drop = 0.1, Every 10 epochs
- loss : Categorical Cross Entropy
- metric : 'Accuracy'
- epochs : 19

### Training and Validation Matrices
![Training and Validation Matrices](Pic/download.png)

- Tranining Acc : 0.0904
- Training loss : 0.9680
- Validation Acc : 0.0802
- Validation loss : 0.9695

## results
- Accuracy: 1.0
- Precision: 1.0
- Recall: 1.0
- F1-score: 1.0
- Confusion matrix:
  
![Cm](Pic/Cm.png)

## Links:
[Model File](Model/TheFinalModelGenderClassification9680.h5)

[Simple Flask Web App](App)

[Demo](https://drive.google.com/file/d/1zOo7D97CnysHc5TCuo03xhSi8YhYhey8/view?usp=sharing)
  
