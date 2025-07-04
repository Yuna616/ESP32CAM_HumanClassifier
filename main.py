# main.py

import requests
import numpy as np
import cv2
from main_controller import MainController
from util.config import  ESP32_CAM_URL, SERVER_URL


def get_image_from_esp32(url: str, save_path: str) -> bool:
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("ESP32로부터 이미지 다운로드 실패")
            return False
        np_arr = np.frombuffer(response.content, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if img is None:
            print("이미지 디코딩 실패")
            return False
        cv2.imwrite(save_path, img)
        return True
    except Exception as e:
        print("이미지 다운로드 중 오류 발생:", e)
        return False


def main():
    image_path = "esp32_image.jpg"
    #1. ESP32에서 이미지 다운로드
    if not get_image_from_esp32(ESP32_CAM_URL, image_path):
        return

    # image_path = "test_image/test5_surprise.jpeg"

    # 2. 메인 컨트롤러 실행
    controller = MainController(image_path)
    controller.run()


if __name__ == "__main__":
    main()
