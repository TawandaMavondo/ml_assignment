import cv2
from keras.applications.imagenet_utils import decode_predictions

# import keras
from keras.models import load_model

# import tensorflow as tf
import numpy as np
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

FRAME_FOLDER = "static/frames"


class ObjectDetection:
    def __init__(self):
        # Import Inceptionv3 model pretrained with adjusted weights
        self.model = load_model("inceptionv3.h5", compile=False)
        pass

    def detect(self, frame, search_key: str):
        img = self.process_image(frame=frame)
        prediction = self.model.predict(img)
        pred_text = decode_predictions(prediction, top=10)

        for (i, (imagentID, label, prob)) in enumerate(pred_text[0]):
            label = "{}: {:.2f}%".format(label, prob * 100)

        return label.__contains__(search_key.lower()), label, frame

    def process_image(self, frame):
        img = cv2.resize(frame, (299, 299))
        img = img.astype(np.float32)
        img = np.expand_dims(img, axis=0)
        img /= 255.0
        return img
