import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os
import NetWork4
import WhichAngle

filen = open('Answer.txt', 'w')
filen.write('Name')
lst=[1,2,3,4,5,7,8,10]
for i in lst:
    filen.write(f';P{i}')
filen.write('\n')

path = 'C:\\Users\\capbr\\PycharmProjects\\pythonProject\\VideoDataSet'
for f in os.listdir(path):
    filen.write(f)
    # filen.write(';')
    poses= NetWork4.get_poses(path + '\\' + f)
    for i in lst:
        filen.write(f'; {poses.index(f"p{i}", 1)}')
    filen.write('\n')




