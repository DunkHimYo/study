#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import picamera as camera
# 엔트리 포인트함수선언----------------------------------------------------------- 
def main(args):
 # 초기화 - PiCamera객체생성
 cam=camera.PiCamera()
 cam.start_preview() 
 cam.start_recording("/home/pi/Pictures/camVideo01.h264") 
 cam.wait_recording(5) # 5sec
 cam.stop_preview()
 cam.stop_recording()
 return 0
if __name__ == '__main__': import sys
 sys.exit(main(sys.argv))
