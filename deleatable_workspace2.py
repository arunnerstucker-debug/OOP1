fourthC = Toplevel(self.first)
        fourthC.geometry("500x400")

        text = Label(fourthC, text="Choose a date: ", font=("Ariel", 14))
        text.place(x=100, y=50)

        global textDate,

        textDate = Text(fourthC, width=35, height=2)
        textDate.place(x=100, y=150)

        BEnter = Button(fourthC, text="Enter", width=10, height=5, command=lambda: self.button_Pushed("EnterC"))
        BEnter.place(x=100, y=250)

        button = []
        date = []
        av = []

        for x in range(len(HDresser())):
            av.append(list(HDresser[x].availability.keys()))
            for y in range(len(x.availability())):
                button.append(Button(fourthC, text=y, width=10, height=5, command=lambda:self.button_Pushed(HDresser[x].availability.keys[y])))
                Button[y].place(x=,y=)
