# service/result_sender.py

import requests
import os
import datetime
from util.config import SERVER_URL

class ResultSender:
    def __init__(self, server_url=SERVER_URL):
        self.server_url = server_url

    def send(self, image_path: str, label: str, confidence: float):
        timestamp = datetime.datetime.now().isoformat()

        try:
            with open(image_path, "rb") as img_file:
                files = {
                    "image": (os.path.basename(image_path), img_file, "image/jpeg")
                }
                data = {
                    "label": label,
                    "confidence": confidence,
                    "timestamp": timestamp
                }

                response = requests.post(self.server_url, files=files, data=data)

                if response.status_code == 200:
                    print(f"[서버 전송 성공] 라벨: {label}, 신뢰도: {confidence:.2f}")
                    print("응답 메시지:", response.json())
                else:
                    print(f"[서버 전송 실패] 상태 코드: {response.status_code}")
                    print("응답 내용:", response.text)

        except Exception as e:
            print(f"[오류] 서버 전송 중 예외 발생: {e}")
