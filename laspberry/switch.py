#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 핀번호 상수 선언 ----------------------------------------------------------------
R_PUSH_PIN   = 4
R_LED_PIN     = 16

# 엔트리 포인트함수선언-----------------------------------------------------------
def main(args):
     # 핀 명명 방식 설정
    GPIO.setmode(GPIO.BCM)
    # 초기화
    GPIO.setup(R_PUSH_PIN, GPIO.IN)   
    GPIO.setup(R_LED_PIN,  GPIO.OUT)    
    GPIO.output(R_LED_PIN, GPIO.LOW)

    # 기능구현
    try:
        while True:
            if GPIO.input(R_PUSH_PIN) == GPIO.LOW :
                GPIO.output(R_LED_PIN, GPIO.HIGH)
                print("Push DOWN")
            else:
                GPIO.output(R_LED_PIN, GPIO.LOW)
                print("Push UP")
                     except KeyboardInterrupt:
        # 리소스 시스템에 반환
        GPIO.cleanup()                       
   return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
