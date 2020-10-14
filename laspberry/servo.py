#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
# 핀번호 상수 선언 -------------------------------------------------------- 
SERVO_PIN = 12 # PWM
# 엔트리 포인트함수선언----------------------------------------------------- 
def main(args): # 핀 명명 방식 설정
  GPIO.setmode(GPIO.BCM)
  # 초기화
  GPIO.setup(SERVO_PIN, GPIO.OUT) # PWM설정
  servo_PWM=GPIO.PWM(SERVO_PIN, 100) 
  servo_PWM.start(0)
  # 기능구현
  try: 
    while True: 
      for degrre in range(0,181,10): # Servo Motor 이동각도
        duty_cycle=convert_duty(float(degrre)) #각도 해당 듀티계산
        servo_PWM.ChangeDutyCycle(duty_cycle) #듀티 적용
        time.sleep(1)
  except KeyboardInterrupt: 
    servo_PWM.stop() # 리소스 시스템에 반환
    GPIO.cleanup()
  return 0
#각도에 해당하는 듀티비 계산
def convert_duty(degree): 
  freq=100.0
  deg_min=0.0
  deg_max=180.0
  duty_min=5.0
  duty_max=22.0
  return ((degree-deg_min)*(duty_max-duty_min)/(deg_max-deg_min)+duty_min)
if __name__ == '__main__': 
  import sys
  sys.exit(main(sys.argv))
