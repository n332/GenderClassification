# GenderClassification
This project is aimed at building a CNN model to classify between two classes (male and female) given an image.
## Data
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
- loss = Categorical Cross Entropy
- metric = 'Accuracy'

### Training and Validation Matrices
![Training and Validation Matrices](Pic/download.png)

## results
- Accuracy: 1.0
- Precision: 1.0
- Recall: 1.0
- F1-score: 1.0
- Confusion matrix:
  
![Cm](Pic/Cm.png)
  
