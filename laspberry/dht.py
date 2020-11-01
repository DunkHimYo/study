#!/usr/bin/python
# -*- coding: utf-8 -*-
import Adafruit_DHT
import time
# 핀번호 상수 선언 ----------------------------------------------------------------
DHT_PIN = 22
# 엔트리 포인트함수선언-----------------------------------------------------------
def main(args): # 초기화
    DHT_TYPE = Adafruit_DHT.DHT11
    # 기능구현
    try:
        while True:
            hum, temp=Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)
            if hum is not None and temp is not None:
                print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temp, hum))
            else: print('Failed to get reading. Try again!')
    except KeyboardInterrupt:
        print(" KeyboardInterrupt")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
