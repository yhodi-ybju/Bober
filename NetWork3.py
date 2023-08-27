import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import WhichAngle

data = pd.read_csv('DataAngle3.csv', delimiter=',')

X = data[['Angle0',  'Angle1',  'Angle2',  'Angle3',  'Angle4',  'Angle5',  'Angle6',  'Angle7',  'Angle8',  'Angle9',  'Angle10',  'Angle11',  'Angle12', 'D_11_12', 'D_23_24']]
y = data['Pose']


scaler = StandardScaler()
X = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)


print("Accuracy:", accuracy)
PointPose = WhichAngle.PointPoseGet()

PointPose = scaler.fit_transform(PointPose)

y_pose = model.predict(PointPose)
print(y_pose)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# y_prob = model.predict_proba(y)
# print("Probabilities for all y:", y_prob)
# print(y_pose)
