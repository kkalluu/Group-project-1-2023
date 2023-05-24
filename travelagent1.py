#Travel Agent - Group Project 1
#Authors: Kaitlyn Lum
#Date: May 21, 2023


#Travel bot will help user create a trip based on their input using the program. 


#greeting for user 
print('Welcome! I am your friendly travel agent bot.\nI will ask you some questions, and make a\n'\
'recommendation based on your answer.\nIf you are interested , I will provide you\n'\
'with a one - time password to create a user\naccount on our website .\n')


#Ask user for name and will say "Hello dear " + the name of user
name=input("What is your name? --> ")
print("Hello dear " + name + " !\n")


#Ask user for age
age=input("What is your age? --> ")
age_int=int(age)


#calculates the discount if user is a senior (over 64 in age)
senior_discount=0
if age_int > 64:
    senior_discount=(age_int-64)/100
    print("""Great ! We offer a senior discount.\nFor every year over 64 , you get 1% off .""")
else: senior_discount=0

 
#Ask how many nights user will stay on vacation
number_of_nights=input("\nFor how many nights do you want to stay? --> ")
number_of_nights_int= int(number_of_nights)


#Asks user what activities they would like to do on this trip
cultural_activities= input("Do you like culture and classical music?\nPlease answer y/n. --> ")
beach_activities= input("Do you like beaches and surfing?\nPlease answer y/n. --> ")


#decides which destination for vacation is best for the user based preferences for activities
#activity input lets us know which combination they of y and n they inputted for the activities question asked above
if cultural_activities == "y" and beach_activities == "y" :
    actvities_input=1

elif cultural_activities =="y" and beach_activities == "n":
    actvities_input=2

elif cultural_activities=="n" and beach_activities =="y" :
    actvities_input=3

elif cultural_activities=="n" and beach_activities == "n" :
    actvities_input=4


#calculates the total cost of the trip if user likes culture and beaches. Suggests the more expensive trip to user
if actvities_input==1:

    flight_vienna=997.93
    nights_in_vienna_cost=number_of_nights_int*143.84
    trip_total_vienna=(flight_vienna+nights_in_vienna_cost)*(1-senior_discount)
    trip_vienna_total_rounded=round(trip_total_vienna,2)

    flight_bali=849.93
    nights_in_bali_cost=number_of_nights_int*235.35
    trip_total_bali=(flight_bali+nights_in_bali_cost)*(1-senior_discount)
    trip_total_bali_rounded=round(trip_total_bali,2)

    if trip_total_vienna > trip_total_bali:        
        print("How about a trip to Vienna?")
        trip_total_vienna_rounded=round(trip_total_vienna,2)
        print("total cost will be $" ,trip_vienna_total_rounded)

    else:        
        print("How about a trip to Bali?\nYour total cost of the trip will be $", trip_total_bali_rounded)


#calculates trip total cost if user likes culture but not beaches...suggests to go to Vienna to user
elif actvities_input ==2:
    flight_vienna=997.93
    nights_in_vienna_cost=number_of_nights_int*143.84
    trip_total_vienna=(flight_vienna+nights_in_vienna_cost)*(1-senior_discount)
    trip_vienna_total_rounded=round(trip_total_vienna,2)
    print("your trip total to Vienna will be $",trip_vienna_total_rounded)


#calculates trip total cost if user likes beaches but not culture...suggests to go to Bali to user
elif actvities_input ==3:
    flight_bali=849.93
    nights_in_bali_cost=number_of_nights_int*235.35
    trip_total_bali=(flight_bali+nights_in_bali_cost)*(1-senior_discount)
    trip_total_bali_rounded=round(trip_total_bali,2)
    print("your trip total to Bali will be $",trip_total_bali_rounded)


#Tells user travel bot has no trips to offer because user doesn't like culture nor beaches
else:print("I am sorry, we don't have any trips to offer at this point.")
