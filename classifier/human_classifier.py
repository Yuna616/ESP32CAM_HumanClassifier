
from classifier.image_classifier import ImageClassifier
from util.config import HUMAN_MODEL_PATH, HUMAN_LABELS_PATH

class HumanClassifier(ImageClassifier):
    def __init__(self):
        super().__init__(HUMAN_MODEL_PATH, HUMAN_LABELS_PATH)

    def predict(self, input_img):
        idx, conf = super().predict(input_img)
        label = " ".join(self.class_names[idx].strip().lower().split(" ")[1:])
        return label, conf
