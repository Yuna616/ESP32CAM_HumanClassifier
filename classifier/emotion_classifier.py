# classifier/emotion_classifier.py

from classifier.image_classifier import ImageClassifier
from util.config import EMOTION_MODEL_PATH, EMOTION_LABELS_PATH

class EmotionClassifier(ImageClassifier):
    def __init__(self):
        super().__init__(EMOTION_MODEL_PATH, EMOTION_LABELS_PATH)

    def predict(self, input_img):
        idx, conf = super().predict(input_img)
        raw_label = " ".join(self.class_names[idx].split(" ")[1:])
        label = raw_label.replace("emotion", "").strip()
        return label, conf
