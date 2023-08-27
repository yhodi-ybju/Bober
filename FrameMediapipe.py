# import cv2
# import mediapipe as mp
# from math import acos
# import os
#
# filen = open('DataAngle.txt', 'w')
# def culc_ugol(x1, y1, x2, y2, x3, y3):
#     a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
#     c = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
#     ugol = acos((c ** 2 + b ** 2 - a ** 2) / (2 * c * b))
#     return ugol
#
# # for papka in ['p1', 'p2', 'p3', 'p4', 'p5', 'p7', 'p8', 'p10']:
# #     d = {}
# #     for f in os.listdir('dataset/' + papka):
# #         image = cv2.imread('dataset/' + papka + '/' + f)
#
# filen.write('Id,')
# filen.write('Pose,')
# for i in range(287):
#     filen.write(f'Angle{i},')
#
#
# # for papka in ['p1', 'p2', 'p3', 'p4', 'p5', 'p7', 'p8', 'p10']:
# #      for f in os.listdir('dataset/' + papka):
#
# mp_drawing = mp.solutions.drawing_utils
# mp_pose = mp.solutions.pose
#
# video_file = 'video2.mp4'
# filename, _ = os.path.splitext(video_file)
#
# filename += "-opencv"
# # main(video_file)
#
# path = 'C:\\Users\\capbr\\PycharmProjects\\pythonProject\\' + filename
#
#
#             lst = [0, 11, 12, 13, 14, 15, 16, 23, 24, 26, 25, 27, 28]
#
#             filen.write('\n')
#             filen.write('frame0-00-00.33.jpg')
#             filen.write(',')
#             filen.write('p1')
#             filen.write(',')
#             for i in range(len(lst) - 2):
#                 for j in range(i + 1, len(lst) - 1):
#                     for k in range(j + 1, len(lst)):
#                         filen.write(str(culc_ugol(results.pose_landmarks.landmark[lst[i]].x,
#                                        results.pose_landmarks.landmark[lst[i]].y,
#                                        results.pose_landmarks.landmark[lst[j]].x,
#                                        results.pose_landmarks.landmark[lst[j]].y,
#                                        results.pose_landmarks.landmark[lst[k]].x,
#                                        results.pose_landmarks.landmark[lst[k]].y)))
#                         filen.write(',')
#         #     down_width = 800
#         #     down_height = 1000
#         #     down_points = (down_width, down_height)
#         #     image = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)
#         #
#         #     # Отображение скелета на изображении
#         #     annotated_image = image.copy()
#         #     mp_drawing.draw_landmarks(
#         #         annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
#         #
#         # # Отображение результата
#         # cv2.imshow('Skeleton Detection', annotated_image)
#         # cv2.waitKey(0)
#         # cv2.destroyAllWindows()