

## **ESP32CAM_HumanClassifier**

ESP32CAM과 딥러닝 모델을 활용하여 사람이 있는지 감지하고 분류하는 프로젝트입니다.




## 📋 개요

- ESP32CAM 보드를 이용해 실시간으로 이미지를 캡처  
- 딥러닝 기반 이미지 분류기를 통해 "사람 있음" vs "사람 없음" 구분  
- 사람인 경우, 해당 인물의 감정 분류 
- 서버-클라이언트 구조 → ESP32CAM에서 이미지를 보내면, 백엔드가 분류 후 결과 리포트  
- 웹 기반 UI 제공 






## ⚙ 구성


```

ESP32CAM_HumanClassifier/  
├── CameraWebServer # ESP32CAM 웹서버 코드  
├── classifier # 이미지 분류 관련 코드  
├── deepLearningModel # 학습된 모델 파일 또는 학습 스크립트  
├── images # 테스트용 이미지 / 예제 이미지  
├── server # 백엔드 서버 코드  
├── service # 분류 서비스 / API  
├── templates # 웹 UI 템플릿 (HTML 등)  
├── test_image # 테스트 이미지 모아둔 디렉토리  
├── util # 공용 유틸리티 함수  
├── app.py # 전체 애플리케이션 실행 진입점  
├── main.py # 메인 로직 실행 파일  
├── main_controller.py # 컨트롤러 역할, 흐름 제어  
└── results.json # 이전 실행 결과 저장용 JSON 파일

```






## 🛠 주요 기술 스택

| 구성 요소 | 기술 / 언어 |
|------------|-------------------|
| 마이크로컨트롤러 | ESP32CAM (C / C++) |
| 이미지 캡처 / 웹서버 | ESP32CAM 자체 웹서버 (CameraWebServer) |
| 딥러닝 분류 | Python 기반 분류기 / 모델 (TensorFlow, PyTorch 등) |
| API / 서버 | Python FastAPI |
| 웹 UI | HTML / Templates |
| 유틸리티 | 공통 유틸리티 함수 / 이미지 전처리 등 |




## 🚀 설치 및 실행
```
1. ESP32CAM 보드에 `CameraWebServer` 코드 업로드  
2. 분류 모델 준비 (deepLearningModel 폴더)  
   - 사전 학습된 모델 파일 복사 또는 학습 스크립트 실행  
3. 서버 세팅  
	터미널에서 
   python uvicorn -m (fastapi 코드 진입점을 적은 파일 이름):app --reload

5.  웹 UI 접속 또는 API 호출
    
    -   브라우저에서 `http://<서버주소>` 접속
        
```


## 📊 실제 실행 예시 

![](https://blog.kakaocdn.net/dna/bdO0uJ/btsO4QBRKv1/AAAAAAAAAAAAAAAAAAAAANDdbPOQduerrC651Wv_XclvQ6CwxgiS_Bu-2p1RawGA/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1759244399&allow_ip=&allow_referer=&signature=VD%2B6odWdT%2F95ZeSYZrdlXvSfTbI%3D)
    




## 🔍 향후 개선 가능성

-   모델 정확도 향상 (더 많은 데이터, augmentation, 더 좋은 네트워크 아키텍처)
    
-   지연(latency) 최적화 — ESP32 내 전처리 또는 경량화된 모델 적용
    
-   보안/인증 추가 — 이미지 전송 및 API 호출 보안
    
-   웹 UI 사용자 경험 개선
    
-   실시간 스트리밍 지원

- **AWS 클라우드 활용**:

	-  ESP32CAM 데이터 S3에 저장 및 Lambda로 실시간 처리
    
	-   AWS IoT Core와 연동하여 원격 모니터링 및 알림 시스템 구축
    
	-   클라우드 기반 API 서버로 확장 가능
    





## 🙋‍♀️ 제작자

-   개발자:
-   Yuna616 : 하드웨어, 웹 서버 프론트/백엔드
-    Leila : 딥러닝 모델 개발
    
개발 기간  25.03.15 ~ 25.06.16

개발 기록 블로그: https://lovebotw049.tistory.com/15
