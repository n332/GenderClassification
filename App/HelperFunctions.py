import numpy as np

import os
import matplotlib.pyplot as plt
import PIL
import tensorflow as tf

from PIL import Image


import time

import cv2

model = tf.keras.models.load_model('TheFinalModelGenderClassification9680.h5')

def GenderPrediction (imagePath):
  '''
  input : imagePath --> String
  output: img -> np array,
          gender --> String

  '''
  img = tf.keras.preprocessing.image.load_img(imagePath, target_size=(100,100))
  img_array = tf.keras.preprocessing.image.img_to_array(img)
  img_batch = np.expand_dims(img_array, axis=0)

  predictions = model.predict(img_batch)
  label = np.argmax(predictions)



  if label == 0:
    gender = 'female'
  else:
    gender = 'male'

  return img, gender

def SearchForFaces(imagePath):

  image = cv2.imread(imagePath)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
  faces = faceCascade.detectMultiScale(
      gray,
      scaleFactor=1.3,
      minNeighbors=3,
      minSize=(30, 30)
  )

  return faces

def GenderClassificationSystem(imagePath):

  image = cv2.imread(imagePath)

  faces = SearchForFaces(imagePath)


  img_dict = {}


  if len(faces) != 0:
    print("[INFO] Found {0} Faces.".format(len(faces)))

    i = 0

    for (x, y, w, h) in faces:

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi_color = image[y:y + h, x:x + w]

        cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)


        img, gender = GenderPrediction (str(w) + str(h) + '_faces.jpg')

        pathForApp = 'static/faces/'+str(i)+'faceDirectly.jpg'
        
        img.save(pathForApp)

        img_dict[i] = (gender,pathForApp)

        i = i+1

    status = cv2.imwrite('faces_detected.jpg', image)
    print("Faces Detected: ")
    Detected_faces = Image.open("faces_detected.jpg")

    plt.imshow(Detected_faces)
    plt.axis('off')
    plt.show()

  else:
    img, gender = GenderPrediction (imagePath)

    pathForApp = 'static/faces/faceDirectly.jpg'

    img.save(pathForApp)
    
    img_dict[0] = (gender,pathForApp)


  return img_dict

