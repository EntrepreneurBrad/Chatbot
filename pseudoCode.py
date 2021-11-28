'''
//make list of suitable words for the computer to determine which department the user is after

    drone_words ← ['drone', 'dji', 'mavic']

    gaming_words ← ['gaming', 'playstation', 'ps4', 'ps3', 'ps5', 'xbox', 'nintendo']

    computer_words ← ['computer', 'apple', 'windows', 'mac', 'laptops', 'desktop', 'surface']


// Give welcome.

    Say "Welcome to Barvey Corman - your leading computers, gaming and drone retailer!"

    Asks "To competently assist you, could you please explain your needs today:

    Assigns a variable name - userInput to user response after this question

    Analyses userInput using Textblob

// First check sentiment in case of irate customer.

    If polarity of userInput < -0.2

        directs to ← 'manager' and says "Hi! I'm the manager. I can see that your clearly annoyed. Let me swiftly assist you so that I can hopefully make your day better!"


// Search for a response for a word relating to a specific department - in this case its drones.

    If drone_words in userInput

         DroneWords == True (to keep track of what department the user wants)

        Directs to more questions function


    Else

        Say "Sorry. I'm unable to detect what your needs are..." and then repeats function so that the user can input their needs


//Once the user is past the setup phase they go to the moreInfo phase - this is where the user is asked more questions

    Says: "To get a better idea of how I can assist you further, please type the corresponding word:"
        - For pricing information, type 'Pricing'
        - For warranty based assistance, type 'Warranty'
        - To place an order, type 'Order'
        - To enquire about stock, type 'Stock'
        - If your purpose of today's call are not due to the reasons above, type 'Other'

    The users response is taken and assigned the variable name assistanceAnswer


//Depending on the category that the user picked they will be directed to a different function

    //Example of this for pricing

        if "pricing" in assistanceAnswer: 
	        Says "Please wait while I get some pricing information."

            Directs to pricing func

//Once past this phase, the users original response used in understanding what department they are interested in (also known as the 'gamingWords' var first assigned at the start)

//Continuing on with my examples with pricing, I will do so (but there are numerous other functions like warranty, order, stock, which are all coded slightly differently, but are structually similar)

Pricing Func:
    if computerWords == true: (there are two other of these for drones and gaming)

        Say: "To get a better idea of how I can assist you further, please type the corresponding word:"

        Then say: 
        - For stock information on the New MacBook Air, type '1'
		- For stock information on the New MacBook Pro, type '2'
        - For stock information on the New iMac, type '3'
		- For stock information on the Microsoft Surface, type '4'
		- For stock information on the Windows PC, type '5'
        - If your product is not above, type 'Other'

        //Asks user for response names computerAnswer

        //Then numerous if statements are used:

        //Example for option 1
            if computerAnswer == "1":
			    "We have 14 Macbook Air's in stock"

                Directs user back to start of program so that they can get anymore assistance

'''