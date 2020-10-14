#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import warnings
# 핀번호 상수 선언 -------------------------------------------------------- 
P_BUZZER_PIN = 5
# 도(0), 레(1), 미(2), 파(3), 솔(4), 라(5), 시(6), 도(7)
scales =[0, 262, 294, 330, 350, 393, 440, 495, 525]
# 엔트리 포인트함수선언----------------------------------------------------- 
def main(args): 
  warnings.filterwarnings("ignore")
  # 핀 명명 방식 설정
  GPIO.setmode(GPIO.BCM)
  # 초기화
  GPIO.setup(P_BUZZER_PIN, GPIO.OUT) 
  GPIO.output(P_BUZZER_PIN, GPIO.LOW)
  # PWM객체생성
  passiveBuzzer=GPIO.PWM(P_BUZZER_PIN, 440) # Frequency제어
  passiveBuzzer.start(50) # Duty Rate 설정
  # 기능구현
  try: 
    while True: 
      for i in range(1, 8): 
        passiveBuzzer.ChangeFrequency(scales[i]) time.sleep(0.5) # 0.5초
  except KeyboardInterrupt: # 리소스 시스템에 반환
    GPIO.cleanup()
  return 0
if __name__ == '__main__': 
  import sys
  sys.exit(main(sys.argv))
