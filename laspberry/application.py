#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from collections import deque
import threading

# 핀번호 상수 선언 ----------------------------------------------------------------
R_LED_PIN = 21
R_PUSH_PIN   = 22
TRIG_PIN   = 17
ECHO_PIN   = 27
BUZ=4
BLUE_PIN     = 6
PINK_PIN     = 13
YELL_PIN     = 19
ORAN_PIN     = 26

# 엔트리 포인트함수선언-----------------------------------------------------------

def buz():
    cnt=0
    while True:
            
        if cnt%10 is 0:
            GPIO.output(BUZ, GPIO.HIGH)
            cnt=0
        else:
            GPIO.output(BUZ, GPIO.LOW)
        time.sleep(1)
        cnt+=1
            
def step():
    sig=deque([1,0,0,1])    
    while True:
        GPIO.output(BLUE_PIN,sig[0])
        GPIO.output(PINK_PIN,sig[1])
        GPIO.output(YELL_PIN,sig[2])
        GPIO.output(ORAN_PIN,sig[3])
        time.sleep(0.01)
        sig.rotate(-1)
        
def button():
    while True:
        if GPIO.input(R_PUSH_PIN) == GPIO.LOW :
            GPIO.output(TRIG_PIN, GPIO.HIGH)
            time.sleep(0.00001)   #10us
            GPIO.output(TRIG_PIN, GPIO.LOW)

    # Echo핀으로 반사되어오는 초음파 시간 계산
    # HIGH신호 시작 == 마지막 LOW신호 시간
            while GPIO.input(ECHO_PIN) == GPIO.LOW:
                pulse_begin =time.time()

    # HIGH신호 끝 == 마지막 HIGH신호 시간     
            while GPIO.input(ECHO_PIN) == GPIO.HIGH:
                pulse_end =time.time()

    #초음파 신호 발사 후 돌아온 왕복 시간  
            duration = float(pulse_end - pulse_begin)
            distance = (340 * (duration/2) ) * 100;
            print(distance)
            if distance>30:
                GPIO.output(R_LED_PIN,GPIO.HIGH)
            else:
                GPIO.output(R_LED_PIN,GPIO.LOW)
            
        else:
            GPIO.output(R_LED_PIN,GPIO.LOW)
        time.sleep(1)
            
def main(args):
    
    # 핀 명명 방식 설정
    
    GPIO.setmode(GPIO.BCM)
    
    # 초기화
    GPIO.setup([BLUE_PIN,PINK_PIN,YELL_PIN,ORAN_PIN,BUZ,TRIG_PIN,R_LED_PIN], GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup([R_PUSH_PIN,ECHO_PIN], GPIO.IN)
 
    # 기능구현
    try:
        th1=threading.Thread(target=step)
        th2=threading.Thread(target=buz)
        th3=threading.Thread(target=button)
        th1.start()
        th2.start()
        th3.start()
        th1.join()
        th2.join()
        th3.join()
    

    except KeyboardInterrupt:
        # 리소스 시스템에 반환
        GPIO.cleanup()                       

    return 0
            

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
