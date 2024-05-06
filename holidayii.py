#This programm calculates a user's total holiday cost, which includes:
#Plane cost, hotel cost and car rental cost:

try:                                                #This is the try function to handle any errors.
    def rental_cost(num_days , price_car):
        return num_days*price_car                   #This will determine the car rental price.

    def hotel_cost(num_nights , night_price):
        return num_nights*night_price               #This will determine the cost of the hotel.


    def plane_cost(city_flight):                    #This will determine the plane cost.  

        ny_flight = city_flight*1.1                 #This is calculated at 1.1 * the city flihgt price
        ldn_flight =city_flight*1.2                 #This is calculated at 1.1 * the city flight price

        if holiday == "new york":
            return ny_flight
        
        elif holiday == "london":
            return ldn_flight
        
        else:
            print("Please enter a country from the list")


    def travel_option():                            #This function will give the options that are available for Holiday.
        print("These are your given Travel Options:")
        print()                                     #This provides a space in the text.
        print("new york = the cost for holiday to new york")
        print("london = the cost for holiday to london")
        print("c = close, book holiday later!")
        print()                                     #This provides a space in the text.
    
    #This will collect the input from the user and calculate the total cost for the holiday
        
    print("This program will calculate the total cost of your holiday!")
    print()                                         #This provides a space in the text.

    holiday = "x"                                   #holiday variable set to X to store user input.
    travel_option()
    while holiday != "c":                           #while loop to process user input.
        holiday=input("Please enter the city you would like to visit!")

        if holiday== "new york":
            num_days=int(input("Please enter the number of days"))
            price_car=int(input("How much will you rent a car for?"))
            num_nights=int(input("Please enter how many night you will spend in the hotel!"))
            night_price=int(input("What is the price per night?"))
            city_flight =int(input("Please enter the cost of your flight!"))
            print ("This is the plane cost for new york:", round(plane_cost(city_flight),2))
            print("Total cost for new york is:$", (rental_cost(num_days , price_car)) + hotel_cost(num_nights , night_price) + plane_cost(city_flight))

            travel_option()                         #This returns the values of the travel_option function.

        elif holiday =="london":
            num_days=int(input("Please enter the number of days"))
            price_car=int(input("How much will you rent a car for?"))
            num_nights=int(input("Please enter how many night you will spend in the hotel!"))
            night_price=int(input("What is the price per night?"))
            city_flight=int(input("Please enter the cost of your flight!"))
            print ("This is the plane cost for london:", round(plane_cost(city_flight),2))
            print("Total cost for london is:£", (rental_cost(num_days , price_car)) + hotel_cost(num_nights , night_price) + plane_cost(city_flight))

            travel_option()                         #This returns the values of the travel_option function.
        
        elif holiday == "c":
            print("")
        else:                                        #Else statement for input that are not an option.
            print("That is not a valid input!")

            travel_option()                          #This returns the values of the travel_option function.       

except Exception as e :                              #This is the exception function function t handle any errors.
    print("Please ensure you are entering integer values!")
    print("Please enter a country from the list!")