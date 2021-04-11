from tkinter import *
from Api_Communication import search_information

column = 0
resultList: list = []


def enterButton(reset_button, global_result_frame, choice_country):
    global column
    global resultList

    if len(choice_country) == 0 or column >= 4:
        return

    data: dict = search_information(choice_country)
    if len(list(data)) == 57:
        return

    if column == 0:
        reset_button.pack(expand=True, pady=20)

    resultFrame = Frame(global_result_frame, bd=1, relief='solid', bg='white')
    resultFrame.grid(column=column, row=1, padx=10, ipadx=30, ipady=45)

    countryLabel = Label(resultFrame, text=data['country'], bg='white', font=('Courrier', 15), fg='#4065A4')
    countryLabel.pack(expand=True)
    populationLabel = Label(resultFrame, text=data['population'] + "habitants", bg='white', font=('Courrier', 10), fg='#4065A4')
    populationLabel.pack(expand=True)
    total_testsLabel = Label(resultFrame, text=data['total_tests'] + "personnes testées", bg='white',
                             font=('Courrier', 10), fg='#4065A4')
    total_testsLabel.pack(expand=True)

    recovered_casesLabel = Label(resultFrame, text="Rétablies : " + data['recovered_cases'], bg='white',
                                 font=('Courrier', 10), fg='#2DDC6C')
    recovered_casesLabel.pack(expand=True)

    active_casesLabel = Label(resultFrame, text="Cas confirmés : " + data['active_cases'], bg='white',
                              font=('Courrier', 10), fg='#B4B90D')
    active_casesLabel.pack(expand=True)
    new_casesLabel = Label(resultFrame, text="Nouveaux cas : " + data['new_cases'], bg='white',
                           font=('Courrier', 10), fg='#B4B90D')
    new_casesLabel.pack(expand=True)
    critical_casesLabel = Label(resultFrame, text="Cas critique : " + data['critical_cases'], bg='white',
                                font=('Courrier', 10), fg='#E51322')
    critical_casesLabel.pack(expand='True')

    deathsLabel = Label(resultFrame, text="Décédés : " + data['total_deaths'], bg='white',
                        font=('Courrier', 10), fg='#E51322')
    deathsLabel.pack(expand=True)
    new_deathsLabel = Label(resultFrame, text="Décédés récemment: " + data['new_deaths'], bg='white',
                            font=('Courrier', 10), fg='#E51322')
    new_deathsLabel.pack(expand=True)

    total_casesLabel = Label(resultFrame, text="Au total, " + data['total_cases'] + "ont été contaminés", bg='white',
                             font=('Courrier', 10))
    total_casesLabel.pack(expand=True)

    column += 1

    resultList.append(resultFrame)


def reset():
    global resultList
    global column
    column = 0
    for i in resultList:
        i.destroy()
