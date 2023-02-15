import pandas as pd
import numpy as np


# get whole student information from excel by creating dataframe
def getStudentInfo():
    student_info = pd.read_excel('Students.xlsx')
    # print(type(studentInfo))
    # print(student_info)
    return student_info


sInfo = getStudentInfo()
# print(sInfo)


def getStudentMarks():
    df = getStudentInfo()
    marks = df[['Name', 'First_Year',
                'Second_Year', 'Third_Year', 'Fourth_Year']]
    return marks

# marks = getStudentMarks()
# print(marks)


def getTotalMarks():
    df = getStudentInfo()
    dict = {}
    for index, row in df.iterrows():
        name = row['Name']
        marks_first = row['First_Year']
        marks_second = row['Second_Year']
        marks_third = row['Third_Year']
        marks_fourth = row['Fourth_Year']
        marks = marks_first+marks_second+marks_third+marks_fourth
        dict[name] = marks
    return dict


def getPercentage():
    dict = getTotalMarks()
    for name, marks in dict.items():
        percentage = ((marks/400)*100)
        dict[name] = percentage
    return dict


percentage = getPercentage()
# print(percentage)


def gethighestMarks():
    pass


def getHighestMarksOfStudent():
    pass


def changeEmailid():
    pass


def changeMarks():
    pass


def setPercentage(percentage):
    df = getStudentInfo()
    percentage = getPercentage()
    # for name , percent in percentage.items()
    for index, row in df.iterrows():
        name = row['Name']
        if name in percentage:
            percent = percentage[name]
            df.loc[index, 'Percentage'] = percent
    df.to_excel('Students.xlsx', index=False)


s = setPercentage(percentage)
