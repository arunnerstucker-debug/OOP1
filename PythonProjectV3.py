import tkinter as tk
from tkinter import *
import pickle
import os

client = []
HDresser = []
dates = []
c = 0
h = 0
time_slots = ["9:00","9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "1:00", "1:30", "2:00", "2:30", "3:00",
              "3:30", "4:00", "4:30"]

class Client:
    def __init__(self):
        self.CID = c
        self.username = ""
        self.password = ""
        self.key = 0
        self.appointment = {}
    def add_Client(self, uname, pword):
        self.username = uname
        self.password = pword
    def book_Appointment(self, date, TimeSlot, Hname):
        key = "A" + str(self.key)
        self.appointment.update({key:{"date":date, "time":TimeSlot, "Hair-Dresser":Hname}})
        self.key += 1
    def cancel_Appointment(self, key):
        del self.appointment[key]


class Hair_Dresser:
    def __init__(self):
        self.HID = h
        self.username = ""
        self.password = ""
        self.dates = []
        self.availability = {}
        self.appointments = {}
        self.breaks = {}
        self.key = 0
    def set_Up_Availability(self, date):
        self.availability.update({date:["9:00","9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "1:00", "1:30",
                                        "2:00", "2:30", "3:00", "3:30", "4:00", "4:30"]})
        self.dates.append(date)
        self.breaks.update({date:[]})
    def add_Hair_Dresser(self, uname, pword):
        self.username = uname
        self.password = pword
    def increase_Availability(self, date, TimeSlot):
        self.dates.append(date)
        self.availability[date].append(TimeSlot)
        self.breaks[date].remove(TimeSlot)
    def add_Appointment(self, date, TimeSlot, client):
        self.availability[date].remove(TimeSlot)
        key = "A" + str(self.key)
        self.appointments.update({key:{"date": date,"time":TimeSlot, "client": client}})
    def decrease_Availability(self, date, TimeSlot):
        self.availability[date].remove(TimeSlot)
        self.breaks[date].append(TimeSlot)
    def cancel_Appointment(self, appointment, date, TimeSlot):
        del self.appointments[appointment]
        self.availability[date].append(TimeSlot)





class Window:
    def __init__(self):
        self.first = Tk()
        self.button = []
        self.username = ""
        self.password = ""
        self.dates = []
        self.date = ""
        self.time = ""
        self.user_index = 0
    def button_Pushed(self, x):
        global HDresser
        print(x)
        self.button.append(x)
        if x in ("Client", "Hair-Dresser"):
            #self.first.withdraw()
            self.second_Page()
        elif x in ("Sign-In", "Sign-Up"):
            self.third_Page()
        elif x == "Enter":
            self.username = TUsername.get(1.0, "end-1c")
            self.password = TPassword.get(1.0, "end-1c")
            print(self.username)
            print(self.password)
            self.user_Entry()
        elif x == "VA":
            print("View Appointments")
            self.fifth_Page_HV()
        elif x == "EA":
            print("Edit Appointments")
            self.fifth_Page_HE()
        elif x == "EnterH":
            self.date = textDate.get(1.0, "end-1c")
            print(self.date)
            if self.date in HDresser[self.user_index].dates:
                self.sixth_Page_HE()
            else:
                HDresser[self.user_index].set_Up_Availability(self.date)
                self.sixth_Page_HE()
        else:
            for n in self.dates:
                if x == n:
                    self.date = n
                    print(self.date)
                    self.fifth_Page_C()
    def user_Entry(self):
        global c, h
        if self.button[0] == "Client" and self.button[1] == "Sign-Up":
            client.append(Client())
            client[c].add_Client(self.username, self.password)
            self.user_index = c
            c += 1
            self.fourth_Page_C()
        elif self.button[0] == "Client" and self.button[1] == "Sign-In":
            for x, user in enumerate(client):
                if self.username == user.username and self.password == user.password:
                    self.user_index = x
                    self.fourth_Page_C()
                else:
                    self.third_Page()
        elif self.button[0] == "Hair-Dresser" and self.button[1] == "Sign-Up":
            HDresser.append(Hair_Dresser())
            HDresser[h].add_Hair_Dresser(self.username, self.password)
            print(HDresser[h].username, HDresser[h].password)
            self.user_index = h
            h += 1
            self.fourth_Page_H()
        elif self.button[0] == "Hair-Dresser" and self.button[1] == "Sign-In":
            for x in range(len(HDresser)):
                if self.username == HDresser[x].username and self.password == HDresser[x].password:
                    self.user_index = x
                    self.fourth_Page_H()
                else:
                    self.third_Page()
    def schedule(self, n, time):
        global HDresser
        print("schedule")

        HDresser[n].add_Appointment(self.date, time, client[self.user_index].username)
        client[self.user_index].book_Appointment(self.date, time, HDresser[n].username)
        self.time = time

        self.sixth_Page_C(n)
    def file_Storage(self):
        global HDresser, client, c, h

        for x in HDresser:
            print(x.username, " will be entered into Hinfo.dat")
        with open("Hinfo.dat", "wb") as fileH:
            pickle.dump(HDresser, fileH)
            fileH.close()

        for y in client:
            print(y.username, "will be entered into Cinfo.dat")
        with open("Cinfo.dat", "wb") as fileC:
            pickle.dump(client, fileC)
            fileC.close()

        with open("Iinfo.dat", "wb") as fileI:
            pickle.dump(h, fileI)
            fileI.close()

        with open("IIinfo.dat", "wb") as fileII:
            pickle.dump(c, fileII)
            fileII.close()

    def first_Page(self):
        self.first.geometry("400x200")
        opening_Function()
        self.first.protocol("WM_DELETE_WINDOW", self.file_Storage)

        BClient = Button(self.first, text='Client', width=20, height=5,
                         command=lambda: self.button_Pushed("Client"))  # will eventually result in the numberC page path
        BClient.place(x=40, y=50)

        BHair_Dresser = Button(self.first, text='Hair-Dresser', width=20, height=5, command=lambda: self.button_Pushed(
            "Hair-Dresser"))  # will eventually result in the numberH page path
        BHair_Dresser.place(x=210, y=50)

        self.first.mainloop()
    def second_Page(self):
        second = Toplevel(self.first)
        second.geometry("400x200")

        BSign_In = Button(second, text='Sign In', width=20, height=5, command=lambda: self.button_Pushed("Sign-In"))
        BSign_In.place(x=40, y=50)

        BSign_Up = Button(second, text='Sign Up', width=20, height=5, command=lambda: self.button_Pushed("Sign-Up"))
        BSign_Up.place(x=210, y=50)
    def third_Page(self):
        third = Toplevel(self.first)
        third.geometry("600x500")

        text = Label(third, text="Input your username and password bellow: ", font=("Ariel", 14))
        text.place(x=100, y=50)

        global TUsername, TPassword

        TUsername = Text(third, width=35, height=2)
        TUsername.place(x=100, y=150)

        TPassword = Text(third, width=35, height=2)
        TPassword.place(x=100, y=250)

        BEnter = Button(third, text="Enter", width=10, height=5, command=lambda: self.button_Pushed("Enter"))
        BEnter.place(x=100, y=350)
    def fourth_Page_C(self):
        fourthC = Toplevel(self.first)
        fourthC.geometry("700x800")

        text = Label(fourthC, text="Choose Date below: ", font=("Ariel", 14))
        text.place(x=50, y=50)

        global textDate, dates
        button = []
        date = []

        for x in range(len(HDresser)):
            d = list(HDresser[x].availability.keys())
            date = list(set(date + d))
        self.dates = date

        for x, d in enumerate(date):
            b = Button(fourthC, text=d, width=10, height=5,
                       command=lambda day = d: self.button_Pushed(day))
            button.append(b)
            if x < 6:
                y = 150
            elif x < 12:
                y = 250
            elif x < 18:
                y = 350
            elif x < 24:
                y = 450
            elif x < 30:
                y = 550
            elif x < 36:
                y = 650
            b.place(x=50 + 100 * x, y=y)

    def fourth_Page_H(self):
        fourthH = Toplevel(self.first)
        fourthH.geometry("400x200")

        BViewAppointments = Button(fourthH, text='View Appointments', width=15, height=5,
                                   command=lambda: self.button_Pushed("VA"))  # will take to the fifthHV page
        BViewAppointments.place(x=75, y=50)

        BEditAvailability = Button(fourthH, text='Edit Availability', width=15, height=5,
                                   command=lambda: self.button_Pushed("EA"))  # will take to the fifthHE page
        BEditAvailability.place(x=200, y=50)
    def fifth_Page_C(self):
        #add a scroll bar or fix the scaling somehow???
        fifthC = Toplevel(self.first)
        fifthC.geometry("500x1700")

        global HDresser, time_slots
        text = []
        btime = []
        button_index = 0

        text.append(Label(fifthC, text=self.date, font=('Ariel', 14)))
        text[0].place(x=50, y=50)

        for x, slot in enumerate(time_slots):
            print(slot)
            text.append(Label(fifthC, text=time_slots[x], font=('Ariel', 14)))
            text[x+1].place(x=50, y=(200*x+150))
            extra_index = 0
            for y, H in enumerate(HDresser):
                print(H)
                for z, A in enumerate(H.availability[self.date]):
                    print(A)
                    if A == slot:
                        print(A)
                        btime.append(Button(fifthC, text = H.username, width= 10, height = 5, command=lambda index=y, s=slot:
                        self.schedule(index, s)))
                        btime[button_index].place(x=(100*extra_index +50),y=(200*x+250))
                        button_index += 1
                        extra_index += 1
    def fifth_Page_HE(self):
        fifthHE = Toplevel(self.first)
        fifthHE.geometry("500x600")

        text = Label(fifthHE, text="Enter Date below: ", font=("Ariel", 14))
        text.place(x=100, y=50)

        global textDate
        textDate = Text(fifthHE, width=35, height=2)
        textDate.place(x=100, y=150)

        BEnter = Button(fifthHE, text="Enter", width=10, height=5, command=lambda: self.button_Pushed("EnterH"))
        BEnter.place(x=100, y=250)

        BBack = Button(fifthHE, text="Back", width=10, height=5, command=lambda: self.fourth_Page_H())
        BBack.place(x=100, y=350)

    def fifth_Page_HV(self):
        fifthHV = Toplevel(self.first)
        fifthHV.geometry("300x800")

        global HDresser
        text = []
        count = 0

        text.append(Label(fifthHV, text="booked appointments: ", font=('Ariel', 14)))
        text[0].place(x=50, y=50)
        for key, appointment in HDresser[self.user_index].appointments.items():
            print(appointment["date"], appointment["time"], appointment["client"])
            text.append(Label(fifthHV, text=(appointment["date"] + " " + appointment["time"] + "\n" + appointment["client"]),
                              font=('Ariel', 14)))
            text[count+1].place(x=50, y=25*count+175)
            count += 1

        BBack = Button(fifthHV, text="back", width=10, height=5, command=lambda: self.fourth_Page_H())
        BBack.place(x=200, y=50)

    def sixth_Page_C(self, n):
        sixthC = Toplevel(self.first)
        sixthC.geometry("500x600")

        global HDresser
        text = []

        text.append(Label(sixthC, text="You have booked an appointment for: ", font=("Ariel", 14)))
        text[0].place(x=50,y=25)
        text.append(Label(sixthC, text=self.date, font=("Ariel", 14)))
        text[1].place(x=50,y=75)
        text.append(Label(sixthC, text="at: ", font=("Ariel", 14)))
        text[2].place(x=50,y=125)
        text.append(Label(sixthC, text=self.time, font=("Ariel", 14)))
        text[3].place(x=50,y=175)
        text.append(Label(sixthC, text="with: ", font=("Ariel", 14)))
        text[4].place(x=50,y=225)
        text.append(Label(sixthC, text=HDresser[n].username, font=("Ariel", 14)))
        text[5].place(x=50,y=275)


        BBack = Button(sixthC, text="Back", width=10, height=5, command=self.fifth_Page_C)
        BBack.place(x=100,y=375)
    def sixth_Page_HE(self):
        sixthHE = Toplevel(self.first)
        sixthHE.geometry("1700x650")

        global HDresser, time_slots
        B1 = []
        B2 = []
        B3 = []

        Label(sixthHE, text="select a time to block off for " + self.date + ": ", font=('Ariel', 14)).place(x=50, y=10)
        Label(sixthHE, text="select an appointment to cancel:", font=('Ariel', 14)).place(x=50, y=190)
        Label(sixthHE, text="Add a time to your availability: ", font=("Ariel", 14)).place(x=50, y=370)

        # this is still not fully fleshed out. It deletes availability but does not result in any buttons for breaks or appointments or breaks when returning to the date.
        for x, time in enumerate(HDresser[self.user_index].availability[self.date]):
            b = Button(sixthHE, text=time, width=10, height=5,
                       command=lambda t=time: HDresser[self.user_index].decrease_Availability(self.date, t))
            B1.append(b)
            b.place(x=100 * x + 50, y=50)

        for y, (Akey, appt) in enumerate(HDresser[self.user_index].appointments.items()):
            if appt["date"] == self.date:
                b = Button(sixthHE, text=(appt["time"] + "\n" + appt["client"]), width=10, height=5,
                       command=lambda k=Akey, t=appt["time"]: HDresser[self.user_index].cancel_Appointment(k, self.date, t))
                B2.append(b)
                b.place(x=100 * y + 50, y=240)

        for z, time in enumerate(HDresser[self.user_index].breaks[self.date]):
            b = Button(sixthHE, text=time, width=10, height=5,
                       command=lambda t=time: HDresser[self.user_index].increase_Availability(self.date, t))
            B3.append(b)
            b.place(x=100 * z + 50, y=420)

        BBack = Button(sixthHE, text="Back", width=10, height=5, command=lambda: self.fifth_Page_HE())
        BBack.place(x=50, y=550)

def opening_Function():
    global HDresser, client, h, c

    if os.path.getsize("Hinfo.dat") > 0:
        with open("Hinfo.dat", "rb") as fileSH:
            HDresser = pickle.load(fileSH)
        print("HDresser: ", HDresser)
    if os.path.getsize("Cinfo.dat") > 0:
        with open("Cinfo.dat", "rb") as fileSC:
            client = pickle.load(fileSC)
        print("client: ", client)

    if os.path.getsize("Iinfo.dat") > 0:
        with open("Iinfo.dat", "rb") as fileIH:
            h = pickle.load(fileIH)
            fileIH.close()
        print("h: ", h)

    if os.path.getsize("IIinfo.dat") > 0:
        with open("IIinfo.dat", "rb") as fileIC:
            c = pickle.load(fileIC)
            fileIC.close()
        print("c: ", c)


#main code
w = Window()
w.first_Page()