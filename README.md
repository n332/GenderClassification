# GenderClassification
The aim of this project is to construct a Convolutional Neural Network (CNN) model that is capable of accurately distinguishing between male and female categories, given an image of a human.

## Project Structure
```bash
├───App
│   ├───static
│   │   └───faces
│   ├───templates
├───Code
├───Model
└───Pic
```

## Methodology
To prepare the images for classification, OpenCV (CV2) is utilized to crop faces from the images.
The classification process is based on a simple CNN algorithm

![FaceDetected](Pic/face_Detected.png)


![Pic](Pic/download.png)

## Data
[Dataset on kaggle]([Model/TheFinalModelGenderClassification9680.h5](https://www.kaggle.com/datasets/cashutosh/gender-classification-dataset/))
- Training :47009

![Training](Pic/trainDist.png)
  
- Validation: 11649
  
![Validation](Pic/ValDist.png)
  
  *Note : This set is splited to : 2,336 for testing and 9,313 for validation*
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
![Training and Validation Matrices](Pic/res.png)

- Tranining loss : 0.0904
- Training Acc : 0.9680
- Validation loss : 0.0802
- Validation lAcc : 0.9695

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
  
