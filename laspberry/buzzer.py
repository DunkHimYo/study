#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 핀번호 상수 선언 ----------------------------------------------------------------
A_BUZ_PIN = 0  

# 엔트리 포인트함수선언-----------------------------------------------------------
def main(args):
    # 핀 명명 방식 설정
    GPIO.setmode(GPIO.BCM)

    # 초기화
    GPIO.setup(A_BUZ_PIN, GPIO.OUT)    
    GPIO.output(A_BUZ_PIN, GPIO.LOW)

    # 기능구현
    try:
        while True:
            GPIO.output(A_BUZ_PIN, GPIO.HIGH)
            print("BUZZER ON")
            time.sleep(1)

            GPIO.output(A_BUZ_PIN, GPIO.LOW)
            print("BUZZER OFF")
            time.sleep(1)
                except KeyboardInterrupt:
        # 리소스 시스템에 반환
        GPIO.cleanup()                       
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
