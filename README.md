# Groot-Model-Deploy

### 사용 목적
AI 모델 (꽃 분류)를 사용하기 위한 API 배포 서버
- 기존의 꽃 분류 모델(네이버, PlanSnap ..)등은 어플리케이션에 종속되어 있기 때문에 누구나 사용할 수 있는 API를 만들고자 제작


### 사용 기술
- Flask
- Keras
- Python

### 사용하기 전 받아야할 라이브러리
- tensorflow (2버전 이상)
- flask
- keras
- PIL



### 사용 방법

모델 다운 받기

- https://drive.google.com/file/d/1MhX7lbFkhVgX0DZ82-TPzWLv2g6xvvH0/view?usp=sharing
- 다운 받은 파일은 predict.py 경로와 같은 위치에 저장

(사용하기 전 python 파일 실행)
- URL : http://localhost:5000/predict(POST)
- Content-Type : multipart/form-data
- Body : 사진

위 정보를 담아 REST API 요청
- 응답 결과
  - image : 판별 결과 
  - success : 성공 여부
  
#### tensorflow, Keras등 라이브러리가 없는 곳에서 사용할 경우
Docker 사용
- Docker Image File 만들기 : 
`docker build -t <Tag 이름> .`

- Docker 실행 : 
`docker run -d -p <사용할 port>:5000 <Tag 이름>`
