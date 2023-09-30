# GenderClassification
## Data

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
