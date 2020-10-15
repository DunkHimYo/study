#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import picamera as camera
import RPi.GPIO as GPIO
import os
# 핀번호 상수 선언 ---------------------------------------------------------------- 
R_PUSH_PIN = 4
# 엔트리 포인트함수선언----------------------------------------------------------- 
def main(args): # 핀 명명 방식 설정
 GPIO.setmode(GPIO.BCM)
 # 초기화
 GPIO.setup(R_PUSH_PIN, GPIO.IN) # Push Switch
 cam=camera.PiCamera() # PiCamera객체생성
 # 기능구현
 try: 
  file_cnt=1
  print(" === Red Push Switch down! === ")
  while True: 
    if GPIO.input(R_PUSH_PIN) == GPIO.LOW : 
    print("Take a picture!") 
    cam.start_preview(fullscreen=False, window=(100, 20, 640, 480)) 
    time.sleep(3) # 3sec
    cam.capture("/home/pi/Pictures/cam{0}.jpg".format(file_cnt)) 
    cam.stop_preview()
    file_cnt += 1
    os.system("ls /home/pi/Pictures/") #촬영이미지 확인

 except KeyboardInterrupt: # 리소스 시스템에 반환
  GPIO.cleanup()

 return 0
if __name__ == '__main__': 
  import sys
  sys.exit(main(sys.argv))
