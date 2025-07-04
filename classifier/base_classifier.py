# classifier/base_classifier.py

from abc import ABC, abstractmethod
import numpy as np
import cv2

class BaseClassifier(ABC):
    def __init__(self, model, class_names):
        self.model = model
        self.class_names = class_names

    @abstractmethod
    def predict(self, input_img):
        pass

    def preprocess(self, img_path):
        img = cv2.imread(img_path)
        if img is None:
            raise FileNotFoundError(f"이미지를 불러올 수 없습니다: {img_path}")
        resized_img = cv2.resize(img, (224, 224))
        input_img = resized_img.astype(np.float32) / 255.0
        input_img = np.expand_dims(input_img, axis=0)
        return input_img, img

    def show_result(self, original_img, label):
        display_img = cv2.resize(original_img, (500, 500))
        cv2.putText(display_img, label, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 255, 0), 2)
        cv2.imshow("결과", display_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
