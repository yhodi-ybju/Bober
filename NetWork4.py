import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import time
import WhichAngle

def get_poses(Filename):
    data = pd.read_csv('C:\\Users\\capbr\\PycharmProjects\\pythonProject\\DataAngle.csv', delimiter=',')

    X = data[['Angle2', 'Angle4', 'Angle6', 'Angle22', 'Angle23', 'Angle24', 'Angle25', 'Angle26', 'Angle28', 'Angle29',
              'Angle51', 'Angle77', 'Angle81', 'Angle106']]
    y = data['Pose']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    start_time = time.time()

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    model = LogisticRegression(multi_class='multinomial', solver='lbfgs')
    model.fit(X_train, y_train)

    PointPose = WhichAngle.PointPoseGet(Filename)
    PointPose = scaler.fit_transform(PointPose)

    y_pose = model.predict(PointPose)
    # print(y_pose)

    y_prob = model.predict_proba(PointPose)
    # print("Probabilities for all y: ")
    # for i in range(len(y_prob)):
    #     print("Element", i + 1, y_prob[i])

    transcript = ['p1', 'p2', 'p3', 'p4', 'p5', 'p7', 'p8', 'p10']
    poses = []
    maxFrame = int(len(y_prob) / 10)
    curPos = 0
    CountFrame = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(y_prob) - 1):
        while (curPos < 7):
            if (y_prob[i][curPos] > y_prob[i][curPos + 1] and CountFrame[curPos] < maxFrame):
                poses.append(transcript[curPos])
                CountFrame[curPos] += 1
            else:
                curPos += 1
                poses.append(transcript[curPos])

        if (CountFrame[7] < maxFrame):
            poses.append(transcript[7])
        else:
            poses.append(' ')
            break

    return(poses)

    # if curPos < len(transcript):
    #     poses.append(transcript[curPos])
    # else:
    #     poses.append('_')

# print(poses)
# return poses

#
# filen = open('Answer.txt', 'w')
# filen.write('Name')
# lst=[1,2,3,4,5,7,8,10]
# for i in lst:
#     filen.write(f',P{i}')
#
# def get_cvs(poses):
#     filen.write(Filename)





# X = data[['Angle2',  'Angle4',  'Angle6',  'Angle22',  'Angle23',  'Angle24',  'Angle25',  'Angle26',  'Angle28',  'Angle29',  'Angle51',  'Angle77',  'Angle81',  'Angle106']]
# y = data['Pose']
#
#
# scaler = StandardScaler()
# X = scaler.fit_transform(X)
#
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# model = LogisticRegression(max_iter=1000)
# model.fit(X_train, y_train)
#
#
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
#
#
# print("Accuracy:", accuracy)
# PointPose = WhichAngle.PointPoseGet()
#
# PointPose = scaler.fit_transform(PointPose)
#
# y_pose = model.predict(PointPose)
# print(y_pose)
#
# y_pose = model.predict_proba(PointPose)
# print("Probability for each pose class:", y_pose)
#
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
#
# while True:
#     point_pose_input = input("Enter the values for PointPose: ")
#     point_pose_values = point_pose_input.split()
#     point_pose_values = [float(val) for val in point_pose_values]
#     point_pose = pd.DataFrame([point_pose_values], columns=['Angle2',  'Angle4',  'Angle6',  'Angle22',  'Angle23',  'Angle24',  'Angle25',  'Angle26',  'Angle28',  'Angle29',  'Angle51',  'Angle77',  'Angle81',  'Angle106'])
#     point_pose = scaler.transform(point_pose)
#
#     y_pose = model.predict_proba(point_pose)
#     pose_vals = model.classes_
#     print("Probability for each pose class:\n")
#     for pose, prob in zip(pose_vals, y_pose[0]):
#         print(f"{pose}: {prob}\n")
#
#     continue_input = input("Do you want to continue (yes/no)? ")
#     if continue_input.lower() != 'yes':
#         break
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)
