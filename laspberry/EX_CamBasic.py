#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import picamera as camera
# 엔트리 포인트함수선언----------------------------------------------------------- 
def main(args):
 # 초기화 - PiCamera객체생성
 cam=camera.PiCamera() cam.start_preview() time.sleep(3) # 3sec
 cam.capture("/home/pi/Pictures/cam01.jpg") cam.stop_preview()
 return 0
if __name__ == '__main__': 
 import sys
 sys.exit(main(sys.argv))
