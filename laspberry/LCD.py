#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi_I2C_driver
import time

# 핀번호 상수 선언 ----------------------------------------------------------
LCD_ADDR = 0x27


# 엔트리 포인트함수선언-----------------------------------------------------
def main(args):
    # 초기화
    lcd = RPi_I2C_driver.lcd(LCD_ADDR)
    # 기능구현
    try:
        while True:
            # Print a message to the LCD.
            lcd.clear()
            lcd.printdata("Hello, ")
            time.sleep(1)
            # At 0.5c second interval " World!!!" Print
            lcd.printdata(" World!", 0.5)
            time.sleep(1)
            for i in range(16):
                # Move the screen to the right 
                lcd.scrollDisplayLeft()
                time.sleep(0.4)
            for i in range(16):
                # Move the screen to the right 
                lcd.scrollDisplayRight()
                time.sleep(0.4)
    except KeyboardInterrupt:
        print(" KeyboardInterrupt")

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
