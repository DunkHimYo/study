#!/usr/bin/env python
# -*- coding: utf-8 -*-
#- Moduel Laoding..---------------------------------------------------------------
import sys
import time
import datetime
import tm1637
import time
# 엔트리 포인트함수선언-----------------------------------------------------------
def main(args): # 초기화
    FND = tm1637.TM1637(3,2,tm1637.BRIGHT_TYPICAL)
    FND.Clear()
    FND.SetBrightnes(1)
    # 기능구현
    try:
        while True: #현재 시간 정보
            now= datetime.datetime.now()
            hour= now.hour
            minute= now.minute
            second= now.second
            currenttime=[ int(hour / 10), hour % 10, int(minute / 10), minute % 10 ]
            FND.Show(currenttime)
            FND.ShowDoublepoint(second % 2)
            time.sleep(1)
    except KeyboardInterrupt:
        print("END FND")
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
