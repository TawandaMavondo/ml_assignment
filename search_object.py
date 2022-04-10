import cv2
from cv2 import VideoCapture
import streamlit as st
from object_detection import ObjectDetection
FRAME_FOLDER = 'static/frames'
VIDEO_PATH = './temp/upload.mp4'
object_detection = ObjectDetection()


def search(object: str,video_bytes):

    video_capture = VideoCapture(video_bytes)
    frame_number = 0
    # try:
    while video_capture.isOpened():
        status, frame = video_capture.read()
        if status:
            status, label, frame = object_detection.detect(
                frame=frame, search_key=object)
            st.write(label)
            if status:
                st.markdown(label)
                return status, label, frame
        else:
            pass
        frame_number += 1
    # except:
    #     return 0

    video_capture.release()
    cv2.destroyAllWindows()
    return None
