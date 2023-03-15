import cv2

## 함수 선언부



## 전역 변수부
src = None # 원본 이미
dst1, dst2, dst3 = None, None, None # 영상처리한 결과


## 메인 코드
src = cv2.imread('c:/images/picture24.jpg') # 이미지 읽기

dat1 = grayScale(scr)
dat2 = cannyEdge(scr)



cv2.imshow('Src', src) # 화면 출력
cv2.imshow('Dts1', dts1) # 화면 출력
cv2.imshow('Dts2', dts2) # 화면 출력

## 마무리
cv2.waitkey(0)
cv2.destoryAllWindow()
