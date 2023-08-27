import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import WhichAngle

data = pd.read_csv('DataAngle.csv', delimiter=',')

X = data[['Angle2',  'Angle4',  'Angle6',  'Angle22',  'Angle23',  'Angle24',  'Angle25',  'Angle26',  'Angle28',  'Angle29',  'Angle51',  'Angle77',  'Angle81',  'Angle106']]
y = data['Pose']


scaler = StandardScaler()
X = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

PointPose = WhichAngle.PointPoseGet()

PointPose = scaler.fit_transform(PointPose)

print("Accuracy:", accuracy)
y_pose = model.predict(PointPose)
print(y_pose)

# y_prob = model.predict_proba(y)
# print("Probabilities for all y:", y_prob)
# print(y_pose)
