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
    if len(data) == 57:
        return

    if column == 0:
        reset_button.pack(expand="True", pady="20")

    resultFrame = Frame(global_result_frame, bd=1, relief="solid", bg="white")
    resultFrame.grid(column=column, row=1, padx='5')

    countryLabel = Label(resultFrame, text=data['country'], bg="white", font=('Courrier', 20))
    countryLabel.pack(expand='True')
    populationLabel = Label(resultFrame, text=data['population'], bg="white", font=('Courrier', 10))
    populationLabel.pack(expand='True')

    casesLabel = Label(resultFrame, text=data['active_cases'] + "Total des cas", bg="white", font=('Courrier', 10))
    casesLabel.pack(expand='True')
    casesLabel = Label(resultFrame, text=data['critical_cases'] + "Cas critique", bg="white", font=('Courrier', 10))
    casesLabel.pack(expand='True')
    casesLabel = Label(resultFrame, text=data['recovered_cases'] + "Rétablies", bg="white", font=('Courrier', 10))
    casesLabel.pack(expand='True')
    casesLabel = Label(resultFrame, text=data['1M_pop_cases'] + "/1M de contaminés", bg="white", font=('Courrier', 10))
    casesLabel.pack(expand='True')
    casesLabel = Label(resultFrame, text=data['total_cases'] + "Au total", bg="white", font=('Courrier', 10))
    casesLabel.pack(expand='True')

    new_deathsLabel = Label(resultFrame, text=data['new_deaths'] + "Morts", bg="white", font=('Courrier', 10))
    new_deathsLabel.pack(expand='True')
    new_deathsLabel = Label(resultFrame, text=data['total_deaths'] + "Total de morts", bg="white",
                            font=('Courrier', 10))
    new_deathsLabel.pack(expand='True')
    pop_deathsLabel = Label(resultFrame, text=data['1M_pop_deaths'] + "/1M d'habitants'", bg="white",
                            font=('Courrier', 10))
    pop_deathsLabel.pack(expand='True')
    total_testsLabel = Label(resultFrame, text=data['total_tests'] + "de personnes testés", bg="white",
                             font=('Courrier', 10))
    total_testsLabel.pack(expand='True')

    column += 1

    resultList.append(resultFrame)


def reset():
    global resultList
    global column
    column = 0
    for i in resultList:
        i.destroy()
