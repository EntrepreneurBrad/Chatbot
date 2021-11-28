import textblob  #importing textBlob to allow for positive or negative tone to be detected
import time #allows for the print messages to be delayed

numOfInstances = 0 #a couonter for everytime the cycle restarts - changing how the computer asks for the user to input their assistance

computerWordState = False #var used to give unique responses depending on Department
gamingWordState = False #var used to give unqiue responses depending on Department
droneWordState = False #var used to give unqiue responses depdning on Department


def placeOrder(): #a function to ask the user for their details when they choose to buy something
	print(
	    "I am now going to take your details for the payment and for shipping \n"
	)
	firstName = input("Please input your first name: ").title()
	lastName = input("Please input your last name: ").title()

	print("Thanks " + str(firstName) + "! Now for your shipping address!")
	houseNum = input("Please input your house number: ")
	street = input("Please input your street name: ")
	suburb = input("Please input your suburb: ")
	postCode = input("Please input your postcode: ")

	print("So it looks like we'll be shipping to " + houseNum + " " + street +
	      " " + suburb + " " + postCode + "!\n")
	print("Now for payment...")

	number = input("Please input the 16 digit credit card number: ")
	name = input("Please input the name on the card: ")
	expiry = input("Please input the cards expiry date: ")
	CVV = input("Please input the cards CVV: ")

	print("Perfect " + firstName + "! " +
	      "You should recieve that in 2-5 business days!")
	userInputFunc()


def pricingInfo(): #if user says that they want pricing info on products
	if computerWordState == True: #if their original response had to do with the commputer Department
		time.sleep(0.5)
		print("")
		print(
		    "To get a better idea of how I can assist you further, please type the corresponding word:"
		)
		time.sleep(0.5)
		print("- For pricing information on the New MacBook Air, type '1'")
		time.sleep(0.5)
		print("- For pricing information on the New MacBook Pro, type '2'")
		time.sleep(0.5)
		print("- For pricing information on the New iMac, type '3'")
		time.sleep(0.5)
		print("- For pricing information on the Microsoft Surface, type '4'")
		time.sleep(0.5)
		print("- For pricing information on the Windows PC, type '5'")
		time.sleep(0.5)
		print("- If your product is not above, type 'Other'")
		time.sleep(0.5)
		computerAnswer = input("").lower() #asks user for which product they want priing info on
		print("")

		if computerAnswer == "1": #if user typed 1 above
			print(
			    "The price of the New Macbook Air is reduced from $1699 to $1499 AUD"
			)
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "2":
			print("The price of the New Macbook Pro starts from $1999 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "3":
			print(
			    "The price of the New iMac is reduced from $1919 to $1699 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "4":
			print("The price of the Microsoft Surface is $1199 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "5":
			print("The price of the Windows PC is on sale for $999 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "other":
			print("Please hold while I transfer you to an expert...")
			print("")
			print(
			    "==============================================================="
			)
			time.sleep(1)
			userInputFunc()

		else:
			pricingInfo() #redo's the pricing question again if user response not match any Number

	if gamingWordState == True: #REFER TO comments of  pricingInfo Computers Func comments (as that code is almost identical to this)
		time.sleep(0.5)
		print("")
		print(
		    "To get a better idea of how I can assist you further, please type the corresponding word:"
		)
		time.sleep(0.5)
		print("- For pricing information on the New PS5, type '1'")
		time.sleep(0.5)
		print("- For pricing information on the New Xbox 1, type '2'")
		time.sleep(0.5)
		print("- For pricing information on the PS4, type '3'")
		time.sleep(0.5)
		print("- For pricing information on the Nintendo Swicth, type '4'")
		time.sleep(0.5)
		print("- For pricing information on the Forza Horizon Game, type '5'")
		time.sleep(0.5)
		print("- If your product is not above, type 'Other'")
		time.sleep(0.5)
		computerAnswer = input("").lower()
		print("")

		if computerAnswer == "1":
			print("The price of the New PS5 is $699 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "2":
			print("The price of the New Xbox 1 starts from $395 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "3":
			print("The price of the PS4 is reduced from $519 to $499 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "4":
			print("The price of the Nintendo Switch is $265 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "5":
			print(
			    "The price of the Fortza Horizon Game is on sale for $89 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "other":
			print("Please hold while I transfer you to an expert...")
			print("")
			print(
			    "==============================================================="
			)
			time.sleep(1)
			userInputFunc()

		else:
			pricingInfo()

	if droneWordState == True: #REFER TO comments of  pricingInfo Computers Func comments (as that code is almost identical to this)
		time.sleep(0.5)
		print("")
		print(
		    "To get a better idea of how I can assist you further, please type the corresponding word:"
		)
		time.sleep(0.5)
		print("- For pricing information on the DJI Mavic Pro, type '1'")
		time.sleep(0.5)
		print("- For pricing information on the DJI Mavic Mini, type '2'")
		time.sleep(0.5)
		print("- For pricing information on the DJI Mavic Air 2, type '3'")
		time.sleep(0.5)
		print("- If your product is not above, type 'Other'")
		time.sleep(0.5)
		computerAnswer = input("").lower()
		print("")

		if computerAnswer == "1":
			print("The price of the DJI Mavic Pro starts from $1699 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "2":
			print("The price of the DJI Mavic Mini is $1199 AUD")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "3":
			print(
			    "The price of the DJI Mavic Air 2 is reduced from $1919 to $1899 AUD"
			)
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "other":
			print("Please hold while I transfer you to an expert...")
			print("")
			print(
			    "==============================================================="
			)
			time.sleep(1)
			userInputFunc()

		else:
			pricingInfo()


def warrantyInfo(): #if user wants to know info on warranty
	if computerWordState == True: #REFER TO comments of  pricingInfo Computers Func comments (as that code is almost identical to this)
		time.sleep(0.5)
		print("")
		print(
		    "To get a better idea of how I can assist you further, please type the corresponding word:"
		)
		time.sleep(0.5)
		print("- For warranty information on the New MacBook Air, type '1'")
		time.sleep(0.5)
		print("- For warranty information on the New MacBook Pro, type '2'")
		time.sleep(0.5)
		print("- For warranty information on the New iMac, type '3'")
		time.sleep(0.5)
		print("- For warranty information on the Microsoft Surface, type '4'")
		time.sleep(0.5)
		print("- For warranty information on the Windows PC, type '5'")
		time.sleep(0.5)
		print("- If your product is not above, type 'Other'")
		time.sleep(0.5)
		computerAnswer = input("").lower()
		print("")

		if computerAnswer == "1":
			print("The New Macbook Air has a 2-year warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "2":
			print("The New Macbook Pro has a 3-year warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "3":
			print("The New iMac is has a lifetime warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "4":
			print("The Microsoft Surface has a 3-year warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "5":
			print("The Windows PC has a 6-month warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "other":
			print("Please hold while I transfer you to an expert...")
			print("")
			print(
			    "==============================================================="
			)
			time.sleep(1)
			userInputFunc()

		else:
			warrantyInfo()

	if gamingWordState == True: #REFER TO comments of  pricingInfo Computers Func comments (as that code is almost identical to this)
		time.sleep(0.5)
		print("")
		print(
		    "To get a better idea of how I can assist you further, please type the corresponding word:"
		)
		time.sleep(0.5)
		print("- For warranty information on the New PS5, type '1'")
		time.sleep(0.5)
		print("- For warranty information on the New Xbox 1, type '2'")
		time.sleep(0.5)
		print("- For warranty information on the PS4, type '3'")
		time.sleep(0.5)
		print("- For warranty information on the Nintendo Swicth, type '4'")
		time.sleep(0.5)
		print("- For warranty information on the Forza Horizon Game, type '5'")
		time.sleep(0.5)
		print("- If your product is not above, type 'Other'")
		time.sleep(0.5)
		computerAnswer = input("").lower()
		print("")

		if computerAnswer == "1":
			print("The New PS5 has a 75-day warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "2":
			print("The New Xbox 1 has a 120-day warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "3":
			print("The PS4 has a 1-year warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "4":
			print("The Nintendo Switch has a 90-day warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "5":
			print("The Fortza Horizon Game has a 60-day warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "other":
			print("Please hold while I transfer you to an expert...")
			print("")
			print(
			    "==============================================================="
			)
			time.sleep(1)
			userInputFunc()

		else:
			warrantyInfo()

	if droneWordState == True: #REFER TO comments of  pricingInfo Computers Func comments (as that code is almost identical to this)
		time.sleep(0.5)
		print("")
		print(
		    "To get a better idea of how I can assist you further, please type the corresponding word:"
		)
		time.sleep(0.5)
		print("- For warranty information on the DJI Mavic Pro, type '1'")
		time.sleep(0.5)
		print("- For warranty information on the DJI Mavic Mini, type '2'")
		time.sleep(0.5)
		print("- For warranty information on the DJI Mavic Air 2, type '3'")
		time.sleep(0.5)
		print("- If your product is not above, type 'Other'")
		time.sleep(0.5)
		computerAnswer = input("").lower()
		print("")

		if computerAnswer == "1":
			print("The DJI Mavic Pro has a 1-year warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "2":
			print("The DJI Mavic Mini has a 3-year warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "3":
			print("The DJI Mavic Air 2 has a 2-year warranty")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "other":
			print("Please hold while I transfer you to an expert...")
			print("")
			print(
			    "==============================================================="
			)
			time.sleep(1)
			userInputFunc()

		else:
			pricingInfo()


def stockInfo(): #if user wants info on stock
	if computerWordState == True: #REFER TO comments of  pricingInfo Computers Func comments (as that code is almost identical to this)
		time.sleep(0.5)
		print("")
		print(
		    "To get a better idea of how I can assist you further, please type the corresponding word:"
		)
		time.sleep(0.5)
		print("- For stock information on the New MacBook Air, type '1'")
		time.sleep(0.5)
		print("- For stock information on the New MacBook Pro, type '2'")
		time.sleep(0.5)
		print("- For stock information on the New iMac, type '3'")
		time.sleep(0.5)
		print("- For stock information on the Microsoft Surface, type '4'")
		time.sleep(0.5)
		print("- For stock information on the Windows PC, type '5'")
		time.sleep(0.5)
		print("- If your product is not above, type 'Other'")
		time.sleep(0.5)
		computerAnswer = input("").lower()
		print("")

		if computerAnswer == "1":
			print("We have 14 Macbook Air's in stock")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "2":
			print("We have 82 of the New Macbook Pro's in stock")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "3":
			print("We have 34 New iMac's in stock")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "4":
			print("We are out of stock for the Microsoft Surface")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "5":
			print(
			    "We have limited supplies for the Windows PC. Currently, they are on pre-order"
			)
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "other":
			print("Please hold while I transfer you to an expert...")
			print("")
			print(
			    "==============================================================="
			)
			time.sleep(1)
			userInputFunc()

		else:
			warrantyInfo()

	if gamingWordState == True: #REFER TO comments of  pricingInfo Computers Func comments (as that code is almost identical to this)
		time.sleep(0.5)
		print("")
		print(
		    "To get a better idea of how I can assist you further, please type the corresponding word:"
		)
		time.sleep(0.5)
		print("- For stock information on the New PS5, type '1'")
		time.sleep(0.5)
		print("- For stock information on the New Xbox 1, type '2'")
		time.sleep(0.5)
		print("- For stock information on the PS4, type '3'")
		time.sleep(0.5)
		print("- For stock information on the Nintendo Swicth, type '4'")
		time.sleep(0.5)
		print("- For stock information on the Forza Horizon Game, type '5'")
		time.sleep(0.5)
		print("- If your product is not above, type 'Other'")
		time.sleep(0.5)
		computerAnswer = input("").lower()
		print("")

		if computerAnswer == "1":
			print("We have 74 New PS5's in stock")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "2":
			print("We have 21 New Xbox 1's in stock")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "3":
			print("We only have 2 PS4's in stock")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "4":
			print("We are out of stock for the Nintendo Switch")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "5":
			print("We have 24 Fortza Horizon Game's in stock")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "other":
			print("Please hold while I transfer you to an expert...")
			print("")
			print(
			    "==============================================================="
			)
			time.sleep(1)
			userInputFunc()

		else:
			warrantyInfo()

	if droneWordState == True: #REFER TO comments of  pricingInfo Computers Func comments (as that code is almost identical to this)
		time.sleep(0.5)
		print("")
		print(
		    "To get a better idea of how I can assist you further, please type the corresponding word:"
		)
		time.sleep(0.5)
		print("- For stock information on the DJI Mavic Pro, type '1'")
		time.sleep(0.5)
		print("- For stock information on the DJI Mavic Mini, type '2'")
		time.sleep(0.5)
		print("- For stock information on the DJI Mavic Air 2, type '3'")
		time.sleep(0.5)
		print("- If your product is not above, type 'Other'")
		time.sleep(0.5)
		computerAnswer = input("").lower()
		print("")

		if computerAnswer == "1":
			print("We have 2 DJI Mavic Pro's in stock")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "2":
			print("We have 14 DJI Mavic Mini's in stock")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "3":
			print("We have 9 DJI Mavic Air 2's in stock")
			time.sleep(1)
			userInputFunc()

		elif computerAnswer == "other":
			print("Please hold while I transfer you to an expert...")
			print("")
			print(
			    "==============================================================="
			)
			time.sleep(1)
			userInputFunc()

		else:
			pricingInfo()


def orderInfo(): #if user wants to order something
	input("Which product would you like to purchase? ")
	print("")
	print("Perfect! Lets get shipping and payment details sorted...")
	print("")
	time.sleep(1)
	print("One Moment Please")
	print("")
	placeOrder() #directs to placeOrder FUnc (gets details 0 credit card, shipping, etc)


def otherInfo(): #if user doesn't select those cateogories
	print("Please hold while I transfer you to an expert...")
	print("")
	print("===============================================================")
	time.sleep(1)
	userInputFunc() #will begin whole code again


def moreInfo(): #asks user more questions to better assist them
	print("")
	print(
	    "To get a better idea of how I can assist you, please type the corresponding word"
	)
	print("")
	time.sleep(0.5)
	print("- For pricing information, type 'Pricing'")
	time.sleep(0.5)
	print("- For warranty based assistance, type 'Warranty'")
	time.sleep(0.5)
	print("- To place an order, type 'Order'")
	time.sleep(0.5)
	print("- To enquire about stock, type 'Stock'")
	time.sleep(0.5)
	print(
	    "- If your purpose of today's call are not due to the reasons above, type 'Other'"
	)
	time.sleep(0.5)
	assistanceAnswer = input("").lower() #asks user for specific needs

	if "pricing" in assistanceAnswer:  #what product - depends on which category
		print("")
		print("Please wait while I get some pricing information.")
		print("")
		pricingInfo()

	elif assistanceAnswer == "warranty":  #what issues have you had and for what product - depends on which category
		print("")
		print("Please wait while I get some warranty information.")
		warrantyInfo()

	elif assistanceAnswer == "order":  #which product do you want to order, take in details - depends on which category
		print("")
		print("Please wait while I get some information on products.")
		orderInfo()

	elif assistanceAnswer == "stock":  #which product do you want to order - depends on which category
		print("")
		print("Please wait while I get some information on stock.")
		stockInfo()

	elif assistanceAnswer == "other":
		print("")
		input("Please give sufficient information on your needs:")
		time.sleep(0.5)
		print("Please wait while I get some information on products.")
		#otherInfo()

	else:
		moreInfo() #redoes func


def userInputFunc(
):  # this is the func where the user inputs their needs and we respond to them

    global droneWordState, computerWordState, gamingWordState, numOfInstances

    print("")

    if numOfInstances == 0:
        userInput = input("To competently assist you, could you please explain your needs today: \n ").lower()  #asks user to input their needs

    else:
        userInput = input("If there's anything else that I can help you with today just let me know... ").lower()  #asks user to input their needs
		
    userInputTextBlob = textblob.TextBlob(userInput)  #turns the string that they inputted into a textBlob so that its pos/neg tone can be analysed
	

    if userInputTextBlob.sentiment.polarity < 0:  #if tone is negative (less than 0 in polarity), call for manager
        numOfInstances = numOfInstances + 1 #adds to the counter which changes the reponse if the second time ths code starts

        if userInputTextBlob.sentiment.polarity < 0 and userInputTextBlob.sentiment.polarity > -0.3: #if user is partilly annoyed
            print("")
            time.sleep(2)
            print("Hi! I'm the manager. I hope I can make your day better!")
            print("")
            
        if userInputTextBlob.sentiment.polarity < -0.3 and userInputTextBlob.sentiment.polarity > -0.6: #if user is mdly angry
            print("")
            time.sleep(2)
            print("Hi! I'm the manager. I've sensed that your not happy with our services. Hopefully I can change that!")
            print("")

        if userInputTextBlob.sentiment.polarity < -0.6 and userInputTextBlob.sentiment.polarity > -1: #if user is very angry
            print("")
            time.sleep(2)
            print("Hi! I'm the manager. I can see that your clearly annoyed. Let me swiftly assist you so that I can hopefully make your day better!")
            print("")
            
            time.sleep(1)
        
        moreInfo() #takes user to more questions

    elif 'drone' in userInput or 'dji' in userInput or 'mavic' in userInput: #if drone wods in what user responded
        droneWordState = True
        numOfInstances = numOfInstances + 1 #adds to the counter which changes the reponse if the second time ths code starts
        print("")
        print("So I understand that you are interested in the Drone Department")
        print("")
        moreInfo() #takes user to more question

    elif "gaming" in userInput or 'playstation' in userInput or 'ps4' in userInput or 'ps3' in userInput or 'ps5' in userInput or 'xbox' in userInput or 'nintendo' in userInput: #if gaming awords in what the user responded to what they wanted
        gamingWordState = True
        numOfInstances = numOfInstances + 1 #adds to the counter which changes the reponse if the second time ths code starts
        print("")
        print("So I understand that you are interested in the Gaming Department")
        print("")
        moreInfo() #takes user to more questions

    elif "computer" in userInput or "apple" in userInput or "windows" in userInput or 'mac' in userInput or 'laptops' in userInput or 'desktop' in userInput or 'surface' in userInput: #if computer words in what the user responded to what they wanted 
        computerWordState = True
        numOfInstances = numOfInstances + 1 #adds to the counter which changes the reponse if the second time ths code starts
        print("")
        print("So I understand that you are interested in the Computer Department")
        print("")
        moreInfo() #takes user to more questions
        
    else:  #if none of the words/polarity is met:
        print("")
        print("Sorry. I'm unable to detect what your needs are...")
        print("")
        print("=========================================================")
        userInputFunc()  #takes the user to the top of the userInput so that they can input their needs again


def start():  #this is the start of code - funcs are needed to allow for the user to input more than once if the computer is unable to find any words/polarity
    print("")
    print("Welcome to Barvey Corman - your leading computers, gaming and drone retailer!")
    userInputFunc()  #takes to userInput func

start()  #start of code
