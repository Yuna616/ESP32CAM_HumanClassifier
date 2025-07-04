# util/config.py

# 사람 인식 모델 경로
HUMAN_MODEL_PATH = "deepLearningModel/converted_keras_human_nohuman/keras_model.h5"
HUMAN_LABELS_PATH = "deepLearningModel/converted_keras_human_nohuman/labels.txt"

# 감정 인식 모델 경로
EMOTION_MODEL_PATH = "deepLearningModel/converted_keras_emotion/keras_model.h5"
EMOTION_LABELS_PATH = "deepLearningModel/converted_keras_emotion/labels.txt"

# ESP32-CAM에서 캡처 이미지 요청할 URL
ESP32_CAM_URL = "http://172.30.1.13/capture"

# FastAPI 서버의 이미지 저장 엔드포인트
SERVER_URL = "http://127.0.0.1:8000/save"

CONFIDENCE_THRESHOLD  = 0.9