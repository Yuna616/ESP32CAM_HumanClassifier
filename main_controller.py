# controller/main_controller.py

from classifier.human_classifier import HumanClassifier
from classifier.emotion_classifier import EmotionClassifier
from service.result_sender import ResultSender
from util.config import CONFIDENCE_THRESHOLD
import cv2

class MainController:
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.human_classifier = HumanClassifier()
        self.emotion_classifier = EmotionClassifier()
        self.sender = ResultSender()

    def run(self):
        # 1. 이미지 전처리 및 사람 감지
        try:
            input_img, original_img = self.human_classifier.preprocess(self.image_path)
        except FileNotFoundError:
            print("이미지 파일을 찾을 수 없습니다.")
            return

        human_label, human_conf = self.human_classifier.predict(input_img)

        if human_label == "no human":
            print("이미지에 사람이 없습니다.")
            result_text = f"{human_label} ({human_conf * 100:.1f}%)"
            self.human_classifier.show_result(original_img, result_text)  # 시각화 추가
            if human_conf >= CONFIDENCE_THRESHOLD:
                self.sender.send(self.image_path, human_label, human_conf)
            else:
                print(f"[전송 생략] 신뢰도 {human_conf:.2f} < 기준치")
        else:
            # 2. 감정 분류 수행
            emotion_label, emotion_conf = self.emotion_classifier.predict(input_img)
            result_text = f"{human_label} : {emotion_label} ({emotion_conf * 100:.1f}%)"
            self.emotion_classifier.show_result(original_img, result_text)

            if emotion_conf >= CONFIDENCE_THRESHOLD:
                self.sender.send(self.image_path, emotion_label, emotion_conf)
            else:
                print(f"[전송 생략] 신뢰도 {emotion_conf:.2f} < 기준치")