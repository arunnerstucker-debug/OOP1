#This program is meant to take in the input of the hair-dresser's availability and apply that to a calendar.
#Object-oriented programing:
#Info that we might need:
#   - Hair Dresser
#       - HDID
#       - Name
#       - Times available
#           - Day
#           - Hour
#           - half hour
#           - Y/N available
#   - Customer
#       - Customer ID???
#       - Customer Name
#       - Customer Payment info
#            - Account number???
#            - Credit card Info
#               - Credit Card Security code?
#               - credit card expiration date
#               - Credit card number#
#            - Bank???
#   - Hours of the Salon
#       - Day
#       -

#
availability = ({"hair_Dresser_Name":{"9:00am":"True = available", "9:30am":"false = booked", "etc":"yep"}})


for i in range(8, 16, 0.5):
    timeh1 = bool(input(f"Enter whether or not you are available for the military hour {i}:00 till {i}:30"))
    timeh2 = bool(input(f"Enter 1 if you are available for the military hour {i}:30 till {i+1}:00"))
    if timeh1 == 1:
