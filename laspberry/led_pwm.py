#!/usr/bin/python
# -*- coding: utf-8 -*-https://github.com/DunkHimYo/study
import RPi.GPIO as GPIO
import time
# 핀번호 상수 선언 ------------------------------------------------------------------------ 
R_LED_PIN = 16
# 엔트리 포인트함수선언------------------------------------------------------------------- 
def main(args): 
  # 핀 명명 방식 설정
  GPIO.setmode(GPIO.BCM)
  # 초기화
  GPIO.setup(R_LED_PIN, GPIO.OUT)
  # PWM객체생성
  ledPWM=GPIO.PWM(R_LED_PIN, 50) 
  ledPWM.start(0)
  # 기능구현
  try: 
    while True: 
      for i in range(0, 50): 
        ledPWM.ChangeDutyCycle(i) # 듀티비 조절로 LED 밝기 조절
        print("Duty : {0}".format(i)) 
        time.sleep(0.07)
  except KeyboardInterrupt: # 리소스 시스템에 반환
    GPIO.cleanup()

 return 0
if __name__ == '__main__': 
  import sys
  sys.exit(main(sys.argv))
