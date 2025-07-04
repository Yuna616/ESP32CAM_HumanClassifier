# classifier/image_classifier.py

import tensorflow as tf
import numpy as np
import cv2
from classifier.base_classifier import BaseClassifier


class ImageClassifier(BaseClassifier):
    def __init__(self, model_path, labels_path):
        # 모델 및 라벨 불러오기
        model = tf.keras.models.load_model(model_path, compile=False)
        with open(labels_path, "r", encoding="utf-8") as f:
            class_names = [line.strip() for line in f.readlines()]

        super().__init__(model, class_names)

    def predict(self, input_img):
        prediction = self.model.predict(input_img)

        # Keras 모델 출력이 dict 형태일 수 있음
        if isinstance(prediction, dict):
            prediction = list(prediction.values())[0]

        predicted_class = int(np.argmax(prediction))
        confidence = float(prediction[0][predicted_class])
        return predicted_class, confidence
