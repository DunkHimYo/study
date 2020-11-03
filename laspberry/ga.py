#!/usr/bin/python
# -*- coding: utf-8 -*-
# 라이브러리 로딩 ----------------------------------------------------------
import spidev # SPI Module
import time
# 핀번호 상수 선언 --------------------------------------------------------
SPI_CE = 0 # MCP3008연결된 CE번호
POTEN_CHANNEL = 0
# 엔트리 포인트함수선언-----------------------------------------------------
def main(args):
    # 초기화
    spi=spidev.SpiDev()
    spi.open(0,SPI_CE)
    spi.max_speed_hz=1000000 # 1MHz
# 기능구현
    try:
         while True:
             adc=spi.xfer2([1, (8+POTEN_CHANNEL) <<4, 0])
             val=((adc[1]&0x03)<<8)+adc[2]
             print( "Potentionmeter is {0}".format(int(val)) )
    except KeyboardInterrupt:
        spi.close() # 리소스 시스템에 반환

    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
