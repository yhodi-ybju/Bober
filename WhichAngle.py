import cv2
import mediapipe as mp
from math import acos
import os
import CutVideo
import numpy as np

def culc_ugol(x1, y1, x2, y2, x3, y3):
    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    ugol = acos((c ** 2 + b ** 2 - a ** 2) / (2 * c * b))
    return ugol

# for papka in ['p1', 'p2', 'p3', 'p4', 'p5', 'p7', 'p8', 'p10']:
#     d = {}
#     for f in os.listdir('dataset/' + papka):
#         image = cv2.imread('dataset/' + papka + '/' + f)




# for papka in ['p1', 'p2', 'p3', 'p4', 'p5', 'p7', 'p8', 'p10']:
#      for f in os.listdir('dataset/' + papka):


def PointPoseGet(filename):
    # # video_file = 'video.mp4'
    # d = []
    # filename, _ = os.path.splitext(video_file)
    #
    # filename += "-opencv"
    # CutVideo.main(video_file)
    d = []
    name = CutVideo.GetPath(filename)
    path = f'C:\\Users\\capbr\\PycharmProjects\\pythonProject\\{name}'

    for f in os.listdir(path):
        Nmepath = path + '\\' + f
        # print(Nmepath)
        d.append(imageVector(Nmepath))
    return d
def imageVector(path):
    image =cv2.imread(path)
    # Инициализация пайплайна обнаружения скелета человека
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

        # Запуск пайплайна на изображении
    with mp_pose.Pose(static_image_mode=True) as pose:
            # Преобразование изображения в формат RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Получение результатов обнаружения скелета
        results = pose.process(image_rgb)
        lst = [0, 11, 12, 13, 14, 15, 16, 23, 24, 26, 25, 27, 28]

        PointToAngle=[(0,11,14), (0,11,16), (0,11,24), (0,13,15), (0,13,16), (0,13,23), (0,13,24), (0,13,26), (0,13,27), (0,13,28),(0,23,24), (11,13,15), (11,13,26), (11,23,26)]

        lstAns = []
        for i in range(len(PointToAngle)):
            lstAns.append(culc_ugol(results.pose_landmarks.landmark[PointToAngle[i][0]].x,
                                        results.pose_landmarks.landmark[PointToAngle[i][0]].y,
                                        results.pose_landmarks.landmark[PointToAngle[i][1]].x,
                                        results.pose_landmarks.landmark[PointToAngle[i][1]].y,
                                        results.pose_landmarks.landmark[PointToAngle[i][2]].x,
                                        results.pose_landmarks.landmark[PointToAngle[i][2]].y))

    return lstAns