# for i in range(287):
#     print(f" 'Angle{i}',", end=' ')

import cv2
import mediapipe as mp
from math import acos, sqrt
import os

filen = open('DataAngle2.txt', 'w')
def culc_ugol(x1, y1, x2, y2, x3, y3):
    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    ugol = acos((c ** 2 + b ** 2 - a ** 2) / (2 * c * b))
    return ugol

filen.write('Id,')
filen.write('Pose,')
for i in range(13):
  filen.write(f'Angle{i},')
filen.write('D_11_12,')
filen.write('D_23_24')




def imageVector(path, f):
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

        filen.write('\n')
        filen.write(f)
        filen.write(',')
        filen.write(papka)
        filen.write(',')
        for i in range(len(PointToAngle)):
            filen.write(str(culc_ugol(results.pose_landmarks.landmark[PointToAngle[i][0]].x,
                                        results.pose_landmarks.landmark[PointToAngle[i][0]].y,
                                        results.pose_landmarks.landmark[PointToAngle[i][1]].x,
                                        results.pose_landmarks.landmark[PointToAngle[i][1]].y,
                                        results.pose_landmarks.landmark[PointToAngle[i][2]].x,
                                        results.pose_landmarks.landmark[PointToAngle[i][2]].y)))
            filen.write(',')
    filen.write(str(sqrt((results.pose_landmarks.landmark[11].x - results.pose_landmarks.landmark[12].x )**2 + (
                                        results.pose_landmarks.landmark[11].y - results.pose_landmarks.landmark[12].y)**2)))
    filen.write(',')
    filen.write(str(sqrt((results.pose_landmarks.landmark[23].x - results.pose_landmarks.landmark[24].x) ** 2 + (
            results.pose_landmarks.landmark[23].y - results.pose_landmarks.landmark[24].y) ** 2)))

for papka in ['p1', 'p2', 'p3', 'p4', 'p5', 'p7', 'p8', 'p10']:
   for f in os.listdir('dataset/' + papka):
        path = 'dataset/' + papka + '/' + f
        imageVector(path, f)