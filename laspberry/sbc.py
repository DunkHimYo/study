#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import picamera as camera
import RPi.GPIO as GPIO
import os
import threading
# 핀번호 상수 선언 ----------------------------------------------------------------
SERVO_PIN = 4 # PWM
P_BUZZER_PIN = 21
# 엔트리 포인트함수선언-----------------------------------------------------------
degrre=0

def buz():
 # 초기화
     global degrre
     GPIO.setup(P_BUZZER_PIN, GPIO.OUT)
     GPIO.output(P_BUZZER_PIN, GPIO.LOW)
 # PWM객체생성
     passiveBuzzer=GPIO.PWM(P_BUZZER_PIN, 440) # Frequency제어
     passiveBuzzer.start(50)
     while True:
         passiveBuzzer.ChangeFrequency(convert_Freq(degrre))
         time.sleep(0.5)
         
def convert_Freq(degree):
 deg_min=0.0
 deg_max=180.0
 freq_min=262.0
 freq_max=525.0
 return ((degree-deg_min)*(freq_max-freq_min)/(deg_max-deg_min)+freq_min)

def picture():
    global degrre
    file_cnt=1
    cam=camera.PiCamera() # PiCamera객체생성
    while True:
        if degrre%10 is 0:
            cam.capture("/home/pi/Pictures/cam{0}.jpg".format(file_cnt))
            file_cnt += 1

def servo():
    global degrre
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    servo_PWM=GPIO.PWM(SERVO_PIN, 100)
    servo_PWM.start(0)
    while True:
        for degrre in range(0,181): # Servo Motor 이동각도
            duty_cycle=convert_duty(float(degrre)) #각도 해당 듀티계산
            servo_PWM.ChangeDutyCycle(duty_cycle) #듀티 적용
            time.sleep(0.006)
                
def convert_duty(degree):
 deg_min=0.0
 deg_max=180.0
 duty_min=0.0
 duty_max=28.0
 return ((degree-deg_min)*(duty_max-duty_min)/(deg_max-deg_min)+duty_min)
    
def main(args): # 핀 명명 방식 설정
    GPIO.setmode(GPIO.BCM)
    
    try:
        th1=threading.Thread(target=servo)
        th2=threading.Thread(target=picture)
        th3=threading.Thread(target=buz)
        th1.start()
        th2.start()
        th3.start()
        th1.join()
        th2.join()
        th3.join()
    except KeyboardInterrupt:
        servo_PWM.stop() # 리소스 시스템에 반환
        GPIO.cleanup()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
