import pandas as pd, re

filePath = "consented_builtprogramming.xlsx"
column1Name = "Student"
column2Name = "ID"

data = pd.read_excel(filePath, engine="openpyxl")
ids = data[column2Name].tolist()

# res = dict(zip(ids, studentNames)
def getStudentNames():
    studentNames = data[column1Name].tolist()
    studentNames = [re.sub(",| ", "", studentName) for studentName in studentNames]
    studentNames = [studentName.lower() for studentName in studentNames]
    return studentNames

