#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 핀번호 상수 선언 ----------------------------------------------------------------
PIR_PIN   = 27
R_LED_PIN = 16

# 엔트리 포인트함수선언-----------------------------------------------------------
def main(args):
    # 핀 명명 방식 설정
    GPIO.setmode(GPIO.BCM)
    
    # 초기화
    GPIO.setup(PIR_PIN, GPIO.IN)   
    GPIO.setup(R_LED_PIN, GPIO.OUT)   
   
    # 기능구현
    try:
        while True:
            if GPIO.input(PIR_PIN) == GPIO.HIGH :
                GPIO.output(R_LED_PIN, GPIO.HIGH)
                print("Detected")
            else:
                GPIO.output(R_LED_PIN, GPIO.LOW)
                print("------")
            
            time.sleep(1)

    except KeyboardInterrupt:
        # 리소스 시스템에 반환
        GPIO.cleanup()        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
