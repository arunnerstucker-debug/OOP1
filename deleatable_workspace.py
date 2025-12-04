client = []
HDresser = []
appointment_store = {}
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
        self.availability.update({date:["9:00","9:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "1:00", "1:30", "2:00", "2:30", "3:00",
              "3:30", "4:00", "4:30"]})
        self.breaks.update({date:[]})
        print(self.breaks)
        print(self.availability)
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
        self.appointments.update({key:{"date": date,"Time":TimeSlot, "client": client}})
    def decrease_availability(self, date, TimeSlot):
        self.availability[date].remove(TimeSlot)
        self.breaks[date].append(TimeSlot)
    def cancel_Appointment(self, key):
        date = self.appointments[key]["date"]
        time = self.appointments[key]["Time"]
        del self.appointments[key]
        self.availability[date].append(time)



h1 = Hair_Dresser()
c1 = Client()

h1.add_Hair_Dresser("Abigail", "Stucker")
h1.set_Up_Availability("12/2/2025")
h1.decrease_availability('12/2/2025', "12:00")
h1.decrease_availability('12/2/2025', "12:30")
print("h1 availability: ", h1.availability)
print("h1 appointments: ", h1.appointments)
print("h1 breaks: ", h1.breaks)

c1.add_Client("Isaac", "Stucker")
c1.book_Appointment("12/2/2025", "3:00", h1.username)
h1.add_Appointment("12/2/2025", "3:00", c1.username)
print("h1 availability: ", h1.availability)
print("h1 appointments: ", h1.appointments)
print("h1 breaks: ", h1.breaks)
print("c1 appointment: ", c1.appointment)

h1.increase_Availability("12/2/2025", "12:30")
print("h1 availability: ", h1.availability)
print("h1 appointments: ", h1.appointments)
print("h1 breaks: ", h1.breaks)

appointment_store.update()



