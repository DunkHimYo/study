#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
# 핀번호 상수 선언 ---------------------------------------------------------------- 
A_DCM_PIN = 25
B_DCM_PIN = 1
# 엔트리 포인트함수선언----------------------------------------------------------- 
def main(args):
  # 핀 명명 방식 설정
  GPIO.setmode(GPIO.BCM)
  # 초기화
  GPIO.setup(A_DCM_PIN, GPIO.OUT) 
  GPIO.setup(B_DCM_PIN, GPIO.OUT)
  # PWM 객체 생성 및 동작 시작
  a_PWM=GPIO.PWM(A_DCM_PIN, 100)
  a_PWM.start(0)
  # 기능구현
  try: 
    while True: 
      for i in range(0, 100, 2): 
      a_PWM.ChangeDutyCycle(i) 
      GPIO.output(B_DCM_PIN, GPIO.LOW) 
      print("Duty : {0}".format(i)) 
      time.sleep(0.1)
  except KeyboardInterrupt: # 리소스 시스템에 반환
    a_PWM.stop() GPIO.cleanup()
  return 0
if __name__ == '__main__': 
  import sys
  sys.exit(main(sys.argv))
