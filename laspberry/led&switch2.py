#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# 핀번호 상수 선언 ----------------------------------------------------------------
PUSH_PINS  =[4, 17]
LED_PINS    =[16, 20]

# 엔트리 포인트함수선언-----------------------------------------------------------
def main(args):
     # 핀 명명 방식 설정
    GPIO.setmode(GPIO.BCM)

    # 초기화
    for i in [0,1]:
        GPIO.setup(PUSH_PINS[i], GPIO.IN)   
        GPIO.setup(LED_PINS[i],  GPIO.OUT)    
        GPIO.output(LED_PINS[i], GPIO.LOW)

    # 기능구현
    try:
        while True:
            for i in [0,1]:
                if GPIO.input(PUSH_PINS[i]) == GPIO.LOW :
                    GPIO.output(LED_PINS[i], GPIO.HIGH)
                    print("Push DOWN & LED ON")
                else:
                    GPIO.output(LED_PINS[i], GPIO.LOW)
                    print("Push UP & LED OFF")
            
    except KeyboardInterrupt:
        # 리소스 시스템에 반환
        GPIO.cleanup()                       
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
