#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
# 핀번호 상수 선언 ----------------------------------------------------------------
R_LED_PIN = 36
G_LED_PIN = 38
B_LED_PIN = 40    
# 엔트리 포인트함수선언-----------------------------------------------------------
def main(args):
    # 핀 명명 방식 설정
    GPIO.setmode(GPIO.BOARD)
    
    # 초기화
    GPIO.setup(R_LED_PIN, GPIO.OUT)
    GPIO.setup(G_LED_PIN, GPIO.OUT)
    GPIO.setup(B_LED_PIN, GPIO.OUT)
    
    GPIO.output(R_LED_PIN, GPIO.LOW)
    GPIO.output(G_LED_PIN, GPIO.LOW)
    GPIO.output(B_LED_PIN, GPIO.LOW)
    time.sleep(1)
    
    # 기능구현
    GPIO.output(R_LED_PIN, GPIO.HIGH)
    print(“RED LED ON”)
    time.sleep(1)

    GPIO.output(R_LED_PIN, GPIO.LOW)
    print(“RED LED OFF”)
    time.sleep(1)

    GPIO.output(G_LED_PIN, GPIO.HIGH)
    print(“GREEN LED ON”)
    time.sleep(1)

    GPIO.output(G_LED_PIN, GPIO.LOW)
    print(“GREEN LED OFF”)
    time.sleep(1)

    GPIO.output(B_LED_PIN, GPIO.HIGH)
    print(“BLUE LED ON”)
    time.sleep(1)

    GPIO.output(B_LED_PIN, GPIO.LOW)
    print(“BLUE LED OFF”)
    time.sleep(1)

    # 리소스 시스템에 반환
    GPIO.cleanup()                       

    return 0

if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
