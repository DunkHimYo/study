#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from collections import deque

# 핀번호 상수 선언 ----------------------------------------------------------------
BLUE_PIN     = 6
PINK_PIN     = 13
YELL_PIN     = 19
ORAN_PIN     = 26

# 엔트리 포인트함수선언-----------------------------------------------------------
def main(args):
    sig=deque([1,0,0,1])
    step=1000
    dir=1

    # 핀 명명 방식 설정
    GPIO.setmode(GPIO.BCM)
    
    # 초기화
    GPIO.setup(BLUE_PIN, GPIO.OUT)
    GPIO.setup(PINK_PIN, GPIO.OUT)  
    GPIO.setup(YELL_PIN, GPIO.OUT)
    GPIO.setup(ORAN_PIN, GPIO.OUT)
    # 기능구현
    try:
        while True:
            for cnt in range(0,step):
                GPIO.output(BLUE_PIN,sig[0])
                GPIO.output(PINK_PIN,sig[1])
                GPIO.output(YELL_PIN,sig[2])
                GPIO.output(ORAN_PIN,sig[3])
                time.sleep(0.01)
                sig.rotate(dir)
            dir=dir*-1

    except KeyboardInterrupt:
        # 리소스 시스템에 반환
        GPIO.cleanup()                       

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
