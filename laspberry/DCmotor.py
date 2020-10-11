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
 GPIO.setup(A_DCM_PIN, GPIO.OUT) GPIO.setup(B_DCM_PIN, GPIO.OUT)

 # 기능구현
 try: 
  while True: 
   run_motor(GPIO.HIGH, GPIO.LOW) 
   print("--CW--")
   time.sleep(2)
   run_motor(GPIO.LOW, GPIO.HIGH) 
   print("--CCW--") 
   time.sleep(2)
   run_motor(GPIO.LOW, GPIO.LOW) 
   print("--STOP-") 
   time.sleep(2)
 except KeyboardInterrupt: # 리소스 시스템에 반환
  GPIO.cleanup()

 return 0
def run_motor(a_value, b_value): 
 GPIO.output(A_DCM_PIN, a_value) 
 GPIO.output(B_DCM_PIN, b_value)
if __name__ == '__main__': import sys
 sys.exit(main(sys.argv))
