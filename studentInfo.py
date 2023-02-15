import pandas as pd
import numpy as np


# get student data from excel

def getStudentData():
    s_data = pd.read_excel('Students.xlsx')
    return s_data


# print(getStudentData())

# get names of students from excel

def getStudentNames():
    s_data = getStudentData()
    names = s_data['Name']

    return names


# print(getStudentNames())

# get students current college year


def getStudentsYear():
    s_data = getStudentData()
    years = list(s_data.Year)
    names = list(s_data.Name)
    total_marks_year = {}
    for name in names:
        for year in years:
            total_marks_year[name] = {'Year': year}
    return total_marks_year


# print(getStudentsYear())


# get yearly marks of students

def getStudentsMarks():
    df = getStudentData()
    marks = df[['Name', 'First_Year',
                'Second_Year', 'Third_Year', 'Fourth_Year']]
    return marks


# print(getStudentsMarks())


# get total marks of students till previous year

def getTotalMarks():
    df = getStudentData()
    df = df.fillna(value=0)
    total_marks = {}
    for index, row in df.iterrows():
        name = row['Name']
        marks_first = row['First_Year']
        marks_second = row['Second_Year']
        marks_third = row['Third_Year']
        marks_fourth = row['Fourth_Year']
        marks = marks_first+marks_second+marks_third+marks_fourth
        total_marks[name] = marks
    return total_marks


# print("Total marks are:\n")
# print(getTotalMarks())


# get percentage of each student

def getPercentage():
    total_marks = getTotalMarks()
    s_data = getStudentData()
    years = list(s_data.Year)
    i = 0
    percentage = {}
    for name, marks in total_marks.items():
        year = years[i]
        percent = ((marks/(year*100))*100)
        percentage[name] = round((float(percent)), 2)
        i += 1
    return percentage


# print("percentage is:\n")
# print(getPercentage())


# set the percentage in excel file


def setPercentage():
    percentage = getPercentage()
    df = getStudentData()
    for name, percent in percentage.items():
        for index, row in df.iterrows():
            name = row['Name']
            if name in percentage:
                percent = percentage[name]
                df.loc[index, 'Percentage'] = percent
    df.to_excel('Students.xlsx', index=False)
    return True


# set_percenrage = setPercentage()
# print(set_percenrage)


# get names of students whose percentage is more than 90

def getTopStudents():
    s_data = getStudentData()
    percentage = s_data[s_data['Percentage'] > 90]
    topStudent = percentage[['Name', 'Percentage']]
    return topStudent


# print(getTopStudents())


# get students details using roll no


def getStudentDetails(rollNo):
    s_data = getStudentData()
    s_details = s_data[s_data['Roll_No'] ==
                       rollNo][['Name', 'Email_ID', 'Age']]

    return s_details


roll_no = int(input("Enter Roll no: "))
print(getStudentDetails(roll_no))


def gethighestMarks():
    pass


def getHighestMarksEachYear():
    pass


# change email id of a student


def changeEmailid():
    pass


# change marks of students of given year


def changeMarks(name, year, newMarks):
    pass
