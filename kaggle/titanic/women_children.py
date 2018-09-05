# women and children first

import csv
import os

os.chdir("C:/Users/Heitor/Desktop/emacs-24.3/bin/code-practice/kaggle/titanic/")

with open('test.csv') as inp, open('womench.csv', 'w') as outp:
    testreader = csv.reader(inp)
    next(testreader)  # skip header

    print('PassengerId,Survived', file=outp)

    for row in testreader:
        id = int(row[0])
        sex = row[3]
        try:
            age = float(row[4])
        except ValueError:
            age = 99

        if sex == 'female' or age < 18:
            survived = 1
        else:
            survived = 0

        print('{},{}'.format(id, survived), file=outp)

        
