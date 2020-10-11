import RPi.GPIO as GPIO
import time

# 핀번호 상수 선언 ----------------------------------------------------------------
TRIG_PIN   = 23
ECHO_PIN   = 24

# 엔트리 포인트함수선언-----------------------------------------------------------
def main(args):
    # 핀 명명 방식 설정
    GPIO.setmode(GPIO.BCM)

    # 초기화
    GPIO.setup(TRIG_PIN, GPIO.OUT)   
    GPIO.setup(ECHO_PIN, GPIO.IN)  
    GPIO.setup(TRIG_PIN, GPIO.LOW) 

    # 기능구현
    try:
        while True:
            print("Distance : %3.0fcm" %get_distance())
            time.sleep(1)     #1초
    except KeyboardInterrupt:
        # 리소스 시스템에 반환
        GPIO.cleanup()                       

    return 0
def get_distance():
    # 초음파 발사 신호 전달
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)   #10us
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Echo핀으로 반사되어오는 초음파 시간 계산
    # HIGH신호 시작 == 마지막 LOW신호 시간
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_begin=time.time()

    # HIGH신호 끝 == 마지막 HIGH신호 시간     
    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end=time.time()

    #초음파 신호 발사 후 돌아온 왕복 시간	
    duration = float(pulse_end - pulse_begin)
    distance = (340 * (duration/2) ) * 100;

    return distance

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
