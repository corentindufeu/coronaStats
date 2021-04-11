from tkinter import *
from buttonsScripts import enterButton, reset

window = Tk()

window.title("Information sur le covid en temp réel")
window.iconbitmap("./icone.ico")
window.geometry('1300x700')
window.minsize(500, 350)
window.configure(bg='#334')

inputsFrame = Frame(window, bg='white', bd=1, relief='solid')
inputsFrame.pack(expand=True)
choiceCountry = Entry(inputsFrame, font=('Courrier', 15))
choiceCountry.pack(expand=True, pady=80, padx=40, ipadx=100)
startButton = Button(inputsFrame, text="Entrer", width=30, height=2, command=lambda: enterButton(resetButton,
                                                                                                 globalResultFrame,
                                                                                                 choiceCountry.get()))
startButton.pack(expand=True, pady=20)

globalResultFrame = Frame(window, bg='#334')
globalResultFrame.pack(expand=True)

resetButton = Button(inputsFrame, text="Recommencer", width=20, height=2, command=lambda: reset())

window.mainloop()
