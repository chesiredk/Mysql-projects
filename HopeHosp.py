import PySimpleGUI as sg
import mysql.connector

dbms = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="Dc762019",
                               database="hope_hosp")
myCursor = dbms.cursor()

sg.theme('Black')
sg.set_options(font='Courier 16')

PatientsData = []
myCursor.execute("SELECT * FROM hope_hosp.PATIENT")
for i in myCursor:
    PatientsData.append(list(i))
headersPatients = ['PatientID', 'FirstName', 'LastName', 'Phone', 'Gender', 'EmergencyContact', 'ConditionDetails',
                   'AdmissionDate']

DepartmentData = []
myCursor.execute("SELECT * FROM hope_hosp.DEPARTMENT")
for j in myCursor:
    DepartmentData.append(list(j))
headersDepartment = ['DepartmentID', 'DepatmentName', 'DepartmentHead', 'OfficeNumber', 'OfficePhone']

DoctorsData = []
myCursor.execute("SELECT * FROM hope_hosp.DOCTOR")
for k in myCursor:
    DepartmentData.append(list(k))
headersDoctor = ['DoctorID', 'Fristname', 'LastName', 'DepartmentID']

NursesData = []
myCursor.execute("SELECT * FROM hope_hosp.NURSE")
for l in myCursor:
    DepartmentData.append(list(l))
headersNurse = ['NurseID', 'FristName', 'LastName', 'DepartmentID']

FacultyData = []
myCursor.execute("SELECT * FROM hope_hosp.FACULTY")
for m in myCursor:
    DepartmentData.append(list(m))
headersFaculty = ['FacultyID', 'FirstName', 'LastName', 'DepartmentID']


# functions that update new data on to the display tables on refreshing
def refresh_patients():
    dbms2 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="Dc762019",
                                    database="hope_hosp")
    myCursor2 = dbms2.cursor()
    data = []
    myCursor2.execute("SELECT * FROM hope_hosp.patient;")
    for j in myCursor2:
        data.append(list(j))
    window1['-table1-'].Update(values=data)
    sg.popup("Patients Updated")


def refresh_departments():
    dbms2 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="Dc762019",
                                    database="hope_hosp")
    myCursor2 = dbms2.cursor()
    data1 = []
    myCursor2.execute("SELECT * FROM hope_hosp.department;")
    for j in myCursor2:
        data1.append(list(j))
    window1['-table2-'].Update(values=data1)
    sg.popup("Departments Updated")


def refresh_doctors():
    dbms2 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="Dc762019",
                                    database="hope_hosp")
    myCursor2 = dbms2.cursor()
    data2 = []
    myCursor2.execute("SELECT * FROM hope_hosp.doctor;")
    for j in myCursor2:
        data2.append(list(j))
    window1['-table3-'].Update(values=data2)
    sg.popup("Doctors Updated")


def refresh_nurses():
    dbms2 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="Dc762019",
                                    database="hope_hosp")
    myCursor2 = dbms2.cursor()
    data3 = []
    myCursor2.execute("SELECT * FROM hope_hosp.nurse;")
    for j in myCursor2:
        data3.append(list(j))
    window1['-table4-'].Update(values=data3)
    sg.popup("Nurses Updated")


def refresh_faculty():
    dbms2 = mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="Dc762019",
                                    database="hope_hosp")
    myCursor2 = dbms2.cursor()
    data4 = []
    myCursor2.execute("SELECT * FROM hope_hosp.faculty;")
    for j in myCursor2:
        data4.append(list(j))
    window1['-table5-'].Update(values=data4)
    sg.popup("Nurses Updated")


# clearing form functions
def clear_patients():
    for key in values:
        window1['FirstName'].update('')
        window1['LastName'].update('')
        window1['Phone'].update('')
        window1['Gender'].update('')
        window1['EmergencyContact'].update('')
        window1['ConditionDetails'].update('')
        window1['AdmissionDate'].update('')
    return None


def clear_departments():
    for key in values:
        window1['DepatmentName'].update('')
        window1['DepartmentHead'].update('')
        window1['OfficeNumber'].update('')
        window1['DepartmentPhone'].update('')
    return None


def clear_doctors():
    for key in values:
        window1['FristName'].update('')
        window1['LastName'].update('')
        window1['DepartmentID'].update('')
    return None


def clear_nurses():
    for key in values:
        window1['FristName'].update('')
        window1['LastName'].update('')
        window1['DepartmentID'].update('')
    return None


def clear_faculty():
    for key in values:
        window1['FirstName'].update('')
        window1['LastName'].update('')
        window1['DepartmentID'].update('')
    return None


# Submitting functions
def submit_patient():
    FirstName = values['FirstName']
    if FirstName == '':
        sg.popup_error('Missing FirstName')
    LastName = values['LastName']
    if LastName == '':
        sg.popup_error('Missing LastName')
    Phone = values['Phone']
    if Phone == '':
        sg.popup_error('Missing Phone')
    Gender = values['Gender']
    if Gender == '':
        sg.popup_error('Missing Gender')
    EmergencyContact = values['EmergencyContact']
    if EmergencyContact == '':
        sg.popup_error('Missing EmergencyContact')
    ConditionDetails = values['ConditionDetails']
    if ConditionDetails == '':
        sg.popup_error('Missing Condition Details')
    AdmissionDate = values['AdmissionDate']
    if AdmissionDate == '':
        sg.popup_error('Missing Admission Date')
    else:
        try:
            command = "INSERT INTO hope_hosp.patient(FirstName, LastName, Phone, Gender, EmergencyContact," \
                      " ConditionDetails, AdmissionDate) VALUES (" + "'" + values['FirstName'] + "'" + ", " + \
                      "'" + values['LastName'] + "'" + ", " + "'" \
                      + values['Phone'] + "'" + ", " + "'" + values['Gender'] + "'" + ", " + "'" + values[
                          'EmergencyContact'] \
                      + "'" + ", " + "'" + values['ConditionDetails'] + "'" + ", " + "'" + values[
                          'AdmissionDate'] + "'" + ");"
            print(command)
            myCursor.execute(command)
            dbms.commit()
            choice = sg.popup_ok_cancel('Please confirm Entry')
            if choice == 'OK':
                clear_patients()
                sg.popup_quick('Patient Entered')
            else:
                sg.popup_ok('Edit Entry')
        except:
            sg.popup('Kindly Check your Entries; possible foreign key constraint')


def submit_department():
    DepatmentName = values['DepatmentName']
    if DepatmentName == '':
        sg.popup_error('Missing DepartmentName')
    DepartmentHead = values['DepartmentHead']
    if DepartmentHead == '':
        sg.popup_error('Missing DepartmentHead')
    OfficeNumber = values['OfficeNumber']
    if OfficeNumber == '':
        sg.popup_error('Missing OfficeNumber')
    DepartmentPhone = values['DepartmentPhone']
    if DepartmentPhone == '':
        sg.popup_error('Missing Department Phone')
    else:
        try:
            command = "INSERT INTO hope_hosp.department(DepatmentName, DepartmentHead, OfficeNumber, DepartmentPhone) " \
                      "VALUES (" + "'" + values['DepatmentName'] + "'" + ", " + \
                      "'" + values['DepartmentHead'] + "'" + ", " + "'" + values['OfficeNumber'] + "'" + ", " + "'" + \
                      values['DepartmentPhone'] \
                      + "'" + ");"
            print(command)
            myCursor.execute(command)
            dbms.commit()
            choice = sg.popup_ok_cancel('Please confirm Entry')
            if choice == 'OK':
                clear_departments()
                sg.popup_quick('Department Entered')
            else:
                sg.popup_ok('Edit Entry')
        except:
            sg.popup('Kindly Check your Entries; possible foreign key constraint')


def submit_doctor():
    FristName = values['FristName']
    if FristName == '':
        sg.popup_error('Missing  FirstName')
    LastName = values['LastName']
    if LastName == '':
        sg.popup_error('Missing LastName')
    DepartmentID = values['DepartmentID']
    if DepartmentID == '':
        sg.popup_error('Missing DepartmentID')
    else:
        try:
            command = "INSERT INTO hope_hosp.doctor(FristName, LastName, DepartmentID) " \
                      "VALUES (" + "'" + values['FristName'] + "'" + ", " + \
                      "'" + values['LastName'] + "'" + ", " + "'" + values['DepartmentID'] \
                      + "'" + ");"
            print(command)
            myCursor.execute(command)
            dbms.commit()
            choice = sg.popup_ok_cancel('Please confirm Entry')
            if choice == 'OK':
                clear_doctors()
                sg.popup_quick('Doctor Entered')
            else:
                sg.popup_ok('Edit Entry')
        except:
            sg.popup('Kindly Check your Entries; possible foreign key constraint')


def submit_nurse():
    FristName = values['FristName']
    if FristName == '':
        sg.popup_error('Missing  FirstName')
    LastName = values['LastName']
    if LastName == '':
        sg.popup_error('Missing LastName')
    DepartmentID = values['DepartmentID']
    if DepartmentID == '':
        sg.popup_error('Missing DepartmentID')
    else:
        try:
            command = "INSERT INTO hope_hosp.nurse(FristName, LastName, DepartmentID) " \
                      "VALUES (" + "'" + values['FristName'] + "'" + ", " + \
                      "'" + values['LastName'] + "'" + ", " + "'" + values['DepartmentID'] \
                      + "'" + ");"
            print(command)
            myCursor.execute(command)
            dbms.commit()
            choice = sg.popup_ok_cancel('Please confirm Entry')
            if choice == 'OK':
                clear_nurses()
                sg.popup_quick('Nurse Entered')
            else:
                sg.popup_ok('Edit Entry')
        except:
            sg.popup('Kindly Check your Entries; possible foreign key constraint')


def submit_faculty():
    FirstName = values['FirstName']
    if FirstName == '':
        sg.popup_error('Missing  FirstName')
    LastName = values['LastName']
    if LastName == '':
        sg.popup_error('Missing LastName')
    DepartmentID = values['DepartmentID']
    if DepartmentID == '':
        sg.popup_error('Missing DepartmentID')
    else:
        try:
            command = "INSERT INTO hope_hosp.faculty(FirstName, LastName, DepartmentID) " \
                      "VALUES (" + "'" + values['FirstName'] + "'" + ", " + \
                      "'" + values['LastName'] + "'" + ", " + "'" + values['DepartmentID'] \
                      + "'" + ");"
            print(command)
            myCursor.execute(command)
            dbms.commit()
            choice = sg.popup_ok_cancel('Please confirm Entry')
            if choice == 'OK':
                clear_faculty()
                sg.popup_quick('Faculty/Staff Entered')
            else:
                sg.popup_ok('Edit Entry')
        except:
            sg.popup('Kindly Check your Entries; possible foreign key constraint')


# GUI  layouts
patientTable_layout = [
    [sg.T('PATIENTS:')],
    [sg.Table(headings=headersPatients, values=PatientsData, display_row_numbers=True, enable_events=True,
              justification='center', key='-table1-')],
    [sg.Button("Refresh Patients", key='-refreshP-', expand_x=True)],
    [sg.Button("Exit", expand_x=True)]
]
departmentTable_layout = [
    [sg.T('DEPARTMENTS:')],
    [sg.Table(headings=headersDepartment, values=DepartmentData, display_row_numbers=True, enable_events=True,
              justification='center', key='-table2-')],
    [sg.Button("Refresh Departments", key='-refreshD-', expand_x=True)],
    [sg.Button("Exit", key='-exit-', expand_x=True)]
]
doctorsTable_layout = [
    [sg.T('DOCTORS:')],
    [sg.Table(headings=headersDoctor, values=DoctorsData, display_row_numbers=True, enable_events=True,
              justification='center', key='-table3-')],
    [sg.Button("Refresh Doctors", key='-refreshDr-', expand_x=True)],
    [sg.Button("Exit", key='-exit-', expand_x=True)]
]
nursesTable_layout = [
    [sg.T('NURSES:')],
    [sg.Table(headings=headersNurse, values=NursesData, display_row_numbers=True, enable_events=True,
              justification='center', key='-table4-')],
    [sg.Button("Refresh Nurses", key='-refreshNur-', expand_x=True)],
    [sg.Button("Exit", key='-exit-', expand_x=True)]
]
facultiesTable_layout = [
    [sg.T('FACULTY&STAFF:')],
    [sg.Table(headings=headersFaculty, values=FacultyData, display_row_numbers=True, enable_events=True,
              justification='center', key='-table5-')],
    [sg.Button("Refresh Faculty", key='-refreshF-', expand_x=True)],
    [sg.Button("Exit", key='-exit-', expand_x=True)]
]

PatientForm_layout = [
    [sg.T('Patient File')],
    [sg.T('FirstName'), sg.Push(), sg.I(size=(30, 5), key='FirstName')],
    [sg.T('LastName'), sg.Push(), sg.I(size=(30, 5), key='LastName')],
    [sg.T('Phone'), sg.Push(), sg.I(size=(30, 5), key='Phone')],
    [sg.T('Gender'), sg.Push(), sg.Combo(size=(30, 5), values=['Male', 'Female', 'Trans-sexual', 'Other'],
                                         key='Gender')],
    [sg.T('EmergencyContact'), sg.Push(), sg.I(size=(30, 5), key='EmergencyContact')],
    [sg.T('Condition Details'), sg.Push(), sg.I(size=(50, 5), key='ConditionDetails')],
    [sg.T('AdmissionDate'), sg.Push(), sg.I(size=(30, 5), key='AdmissionDate')],
    [sg.Button('Submit', key='-submit-', expand_x=True), sg.Button('Clear', key='-clear-', expand_x=True),
     sg.Button('Exit', key='-exit-', expand_x=True)]
]
DepartmentForm_layout = [
    [sg.T('Department File')],
    [sg.T('DepatmentName'), sg.Push(), sg.I(size=(30, 5), key='DepatmentName')],
    [sg.T('DepartmentHead'), sg.Push(), sg.I(size=(30, 5), key='DepartmentHead')],
    [sg.T('OfficeNumber'), sg.Push(), sg.I(size=(30, 5), key='OfficeNumber')],
    [sg.T('DepartmentPhone'), sg.Push(), sg.I(size=(30, 5), key='DepartmentPhone')],
    [sg.Button('Submit', key='-submit-', expand_x=True), sg.Button('Clear', key='-clear-', expand_x=True),
     sg.Button('Exit', key='-exit-', expand_x=True)]
]
DoctorsForm_layout = [
    [sg.T('Doctors File:')],
    [sg.T('FristName'), sg.Push(), sg.I(size=(30, 5), key='FristName')],
    [sg.T('LastName'), sg.Push(), sg.I(size=(30, 5), key='LastName')],
    [sg.T('DepartmentID'), sg.Push(), sg.I(size=(30, 5), key='DepartmentID')],
    [sg.Button('Submit', key='-submit-', expand_x=True), sg.Button('Clear', key='-clear-', expand_x=True),
     sg.Button('Exit', key='-exit-', expand_x=True)]
]
NursesForm_layout = [
    [sg.T('Nurses File:')],
    [sg.T('FristName'), sg.Push(), sg.I(size=(30, 5), key='FristName')],
    [sg.T('LastName'), sg.Push(), sg.I(size=(30, 5), key='LastName')],
    [sg.T('DepartmentID'), sg.Push(), sg.I(size=(30, 5), key='DepartmentID')],
    [sg.Button('Submit', key='-submit-', expand_x=True), sg.Button('Clear', key='-clear-', expand_x=True),
     sg.Button('Exit', key='-exit-', expand_x=True)]
]
FacultyForm_layout = [
    [sg.T('Faculties File:')],
    [sg.T('FirstName'), sg.Push(), sg.I(size=(30, 5), key='FirstName')],
    [sg.T('LastName'), sg.Push(), sg.I(size=(30, 5), key='LastName')],
    [sg.T('DepartmentID'), sg.Push(), sg.I(size=(30, 5), key='DepartmentID')],
    [sg.Button('Submit', key='-submit-', expand_x=True), sg.Button('Clear', key='-clear-', expand_x=True),
     sg.Button('Exit', key='-exit-', expand_x=True)]
]

main_layout = [
    [sg.Button('Display PATIENTS', key='-viewP-')],[sg.Button('Enter Patients', key='-enterP-')],
    [sg.Button('Display DEPARTMENTS', key='-viewD-')], [sg.Button('Department Registration', key='-enterD-')],
    [sg.Button('Display DOCTORS', key='-viewDr-')], [sg.Button('Doctor Registration', key='-enterDr-')],
    [sg.Button('Display NURSES', key='-viewN-')], [sg.Button('Nurses Registration', key='-enterN-')],
    [sg.Button('Display FACULTY', key='-viewF-')], [sg.Button('Enter Faculty', key='-enterF-')],
    [sg.Button('Exit', key='-exit-')]
]

# -MAIN-
while True:
    window = sg.Window("HOPE HOSPITAL", main_layout)
    event, values = window.read()
    if event in (sg.WIN_CLOSED or '-exit-'):
        break
    if event == '-viewP-':
        window1 = sg.Window("", patientTable_layout)
        event, values = window1.read()
        if event == 'Exit':
            window1.close()
        if event == '-refreshP':
            refresh_patients()
    if event == '-enterP-':
        window1 = sg.Window("Patient Record Form", PatientForm_layout)
        event, values = window1.read()
        if event == '-submit-':
            submit_patient()
        if event == '-clear-':
            clear_patients()
        if event == '-exit-':
            window1.close()
    if event == '-viewD-':
        window1 = sg.Window("Departments:", departmentTable_layout)
        event, values = window1.read()
        if event == '-exit-':
            window1.close()
        if event == '-refreshD-':
            refresh_departments()
    if event == '-enterD-':
        window1 = sg.Window("Department File:", DepartmentForm_layout)
        event, values = window1.read()
        if event == '-submit-':
            submit_department()
        if event == '-clear-':
            clear_departments()
        if event == '-exit-':
            window1.close()
    if event == '-viewDr-':
        window1 = sg.Window("Doctors:", doctorsTable_layout)
        event, values = window1.read()
        if event == '-exit-':
            window1.close()
        if event == '-refreshDr-':
            refresh_doctors()
    if event == '-enterDr-':
        window1 = sg.Window("Doctors File:", DoctorsForm_layout)
        event, values = window1.read()
        if event == '-submit-':
            submit_doctor()
        if event == '-clear-':
            clear_doctors()
        if event == '-exit-':
            window1.close()
    if event == '-viewN-':
        window1 = sg.Window("Nurses:", nursesTable_layout)
        event, values = window1.read()
        if event == '-exit-':
            window1.close()
        if event == '-refreshNur-':
            refresh_nurses()
    if event == '-enterN-':
        window1 = sg.Window("Nurses File:", NursesForm_layout)
        event, values = window1.read()
        if event == '-submit-':
            submit_nurse()
        if event == '-clear-':
            clear_nurses()
        if event == '-exit-':
            window1.close()
    if event == '-viewF-':
        window1 = sg.Window("Faculty&Staff:", facultiesTable_layout)
        event, values = window1.read()
        if event == '-exit-':
            window1.close()
        if event == '-refreshF-':
            refresh_faculty()
    if event == '-enterF-':
        window1 = sg.Window("Faculty&Staff:", FacultyForm_layout)
        event, values = window1.read()
        if event == '-submit-':
            submit_faculty()
        if event == '-clear-':
            clear_faculty()
        if event == '-exit-':
            window1.close()

window.close()
