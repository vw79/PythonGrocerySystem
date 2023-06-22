def length(length): #length function
    count = 0
    for _ in length:
        count += 1
    return count

def findIndex(arr, element): #index function
    count = 0
    for i in range(length(arr)):
        if(element.lower() == arr[i].lower()):
            return int(count)
        else:
            count += 1

def start(): #start menu
    logUsername = "new"
    userType = "newCustomer"

    with open ("cart.txt", "w") as file:
        file.write("")

    print("-----------------------------Menu------------------------------------")
    print("Welcome to FRESHCO Online Shopping")
    print("Options:\n\t[1] View Groceries\n\t[2] Login\n\t[3] Register\n\t[4] Exit\n\t")
    option = input("Enter your option [1/2/3/4]: ")
    if(option=="1"):
        viewGroceries(userType, logUsername)
    elif(option=="2"):
        login()
    elif(option=="3"):
        register()
    elif(option=="4"):
        exit()
    else:
        print("Error: Please enter a valid option")
        start()

def viewFood(userType, logUsername,hiddenMenu = False): #open food data and show 
    print("-----------------------------Food-----------------------------------")
    categories = ["ID", "Item", "Price", "Expiry Date", "Stocks Available", "Description"]
    print(f"{categories[0]:5s}{categories[1]:80s}{categories[2]:20s}{categories[3]:20s}{categories[4]:20s}{categories[5]:20s}")

    with open("groceries_food.txt", "r") as file:
        for data in file:
            id, food, price, expiryDate, stocksAvailable, description = data.split("|")
            print(f"{id:5s}{food:80s}{price:20s}{expiryDate:20s}{stocksAvailable:20s}{description:20s}")

        if hiddenMenu:
            pass
        else:     
            if (userType == "customer"):
                print("Options:\n\t[1] Previous Page\n\t[2] Main Menu\n\t[3] Buy\n\t[4] Cart\n\t")
                option = input ("Enter your option [1/2/3/4]: ")
                if (option == "1"):
                    viewGroceries(userType, logUsername)
                elif (option == "2"):
                    customerView(logUsername)
                elif (option == "3"):
                    addCart(userType, logUsername)
                elif (option == "4"):
                    viewCart(userType, logUsername)
                else:
                    print("Error: Please enter a valid option")
                    viewFood(userType, hiddenMenu)
                
            elif (userType == "admin"):
                print("Options:\n\t[1] Previous Page\n\t[2] Main Menu\n\t[3] Search and Edit Groceries\n\t[4] Add Groceries\n\t[5] Remove Groceries\n\t")
                option = input ("Enter your option [1/2/3/4]: ")
                if (option == "1"):
                    viewGroceries(userType, logUsername)
                elif (option == "2"):
                    adminView(logUsername)
                elif (option == "3"):
                    searchStock(logUsername)
                elif (option == "4"):
                    addItem(logUsername)
                elif (option == "5"):
                    removeItem(logUsername)
                else:
                    print("Error: Please enter a valid option")
                    viewFood(userType, hiddenMenu)

            else:
                print("Options:\n\t[1] Previous Page\n\t[2] Main Menu\n\t")
                option = input ("Enter your option [1/2]: ")
                if (option == "1"):
                    viewGroceries(userType, logUsername)
                elif (option == "2"):
                    start()
                else:
                    print("Error: Please enter a valid option")
                    viewFood(userType, hiddenMenu) 
        
def viewMedicine(userType, logUsername, hiddenMenu = False): #open medicine data and show 
    print("----------------------------Medicine--------------------------------")
    categories = ["ID", "Item", "Price", "Expiry Date", "Stocks Available", "Description"]
    print(f"{categories[0]:5s}{categories[1]:80s}{categories[2]:20s}{categories[3]:20s}{categories[4]:20s}{categories[5]:20s}")
    with open("groceries_medicine.txt", "r") as file:                    
        for data in file:
            id, medicine, price, expiryDate, stocksAvailable, description = data.split("|")
            print(f"{id:5s}{medicine:80s}{price:20s}{expiryDate:20s}{stocksAvailable:20s}{description:20s}")
        
        if hiddenMenu:
            pass
        else:     
            if (userType == "customer"):
                print("Options:\n\t[1] Previous Page\n\t[2] Main Menu\n\t[3] Buy\n\t[4] Cart\n\t")
                option = input ("Enter your option [1/2/3/4]: ")
                if (option == "1"):
                    viewGroceries(userType, logUsername)
                elif (option == "2"):
                    customerView(logUsername)
                elif (option == "3"):
                    addCart(userType, logUsername)
                elif (option == "4"):
                    viewCart(userType, logUsername)
                else:
                    print("Error: Please enter a valid option")
                    viewMedicine(userType, hiddenMenu)
                
            elif (userType == "admin"):
                print("Options:\n\t[1] Previous Page\n\t[2] Main Menu\n\t[3] Search and Edit Groceries\n\t[4] Add Groceries\n\t[5] Remove Groceries\n\t")
                option = input ("Enter your option [1/2/3/4]: ")
                if (option == "1"):
                    viewGroceries(userType, logUsername)
                elif (option == "2"):
                    adminView(logUsername)
                elif (option == "3"):
                    searchStock(logUsername)
                elif (option == "4"):
                    addItem(logUsername)
                elif (option == "5"):
                    removeItem(logUsername)
                else:
                    print("Error: Please enter a valid option")
                    viewMedicine(userType, hiddenMenu)

            else:
                print("Options:\n\t[1] Previous Page\n\t[2] Main Menu\n\t")
                option = input ("Enter your option [1/2]: ")
                if (option == "1"):
                    viewGroceries(userType, logUsername)
                elif (option == "2"):
                    start()
                else:
                    print("Error: Please enter a valid option")
                    viewMedicine(userType, hiddenMenu) 
    
def viewDailyNecessities(userType, logUsername): #open daily necessities data and show 
    print("-----------------------Daily Necessities----------------------------")
    categories = ["ID", "Item", "Price", "Expiry Date", "Stocks Available", "Description"]
    print(f"{categories[0]:5s}{categories[1]:80s}{categories[2]:20s}{categories[3]:20s}{categories[4]:20s}{categories[5]:20s}")
    with open("groceries_daily_necessities.txt", "r") as file:     
        for data in file:

            id, dailyNecessities, price, expiryDate, stocksAvailable, description = data.split("|")
            print(f"{id:5s}{dailyNecessities:80s}{price:20s}{expiryDate:20s}{stocksAvailable:20s}{description:20s}")
            
    if (userType == "customer"):
        print("Options:\n\t[1] Previous Page\n\t[2] Main Menu\n\t[3] Buy\n\t[4] Cart\n\t")
        option = input ("Enter your option [1/2/3/4]: ")
        if (option == "1"):
            viewGroceries(userType, logUsername)
        elif (option == "2"):
            customerView(logUsername)
        elif (option == "3"):
            addCart(userType, logUsername)
        elif (option == "4"):
            viewCart(userType, logUsername)
        else:
            print("Error: Please enter a valid option")
            viewDailyNecessities(userType, logUsername)
        
    elif (userType == "admin"):
        print("Options:\n\t[1] Previous Page\n\t[2] Main Menu\n\t[3] Search and Edit Groceries\n\t[4] Add Groceries\n\t[5] Remove Groceries\n\t")
        option = input ("Enter your option [1/2/3/4]: ")
        if (option == "1"):
            viewGroceries(userType, logUsername)
        elif (option == "2"):
            adminView(logUsername)
        elif (option == "3"):
            searchStock(logUsername)
        elif (option == "4"):
            addItem(logUsername)
        elif (option == "5"):
            removeItem(logUsername)
        else:
            print("Error: Please enter a valid option")
            viewDailyNecessities(userType, logUsername)

    else:
        print("Options:\n\t[1] Previous Page\n\t[2] Main Menu\n\t")
        option = input ("Enter your option [1/2]: ")
        if (option == "1"):
            viewGroceries(userType, logUsername)
        elif (option == "2"):
            start()
        else:
            print("Error: Please enter a valid option")
            viewDailyNecessities(userType, logUsername) 
    
def viewAll(userType, logUsername): #view all item in shop
    viewFood(userType,logUsername, hiddenMenu = True)
    viewMedicine(userType, logUsername, hiddenMenu = True) 
    viewDailyNecessities(userType, logUsername) 

def readStocks(): #arrange the database into their corresponding categories #transpose the database so it is to read according to category
    ids, items, prices, expireDates, stockAvailables, descriptions = [], [], [], [], [], []
    with open ("groceries_food.txt","r") as f1, open ("groceries_medicine.txt","r") as f2, open ("groceries_daily_necessities.txt","r") as f3:

        for file in f1,f2,f3: #loop through each tile
            for data in file: #take the data in each file
                id, item, price, expireDate, stockAvailable, description = data.split("|")
                ids.append(id)     
                items.append(item)
                prices.append(price)
                expireDates.append(expireDate)
                stockAvailables.append(stockAvailable)
                descriptions.append(description)
    return ids, items, prices, expireDates, stockAvailables, descriptions

def readCustomerDetails(): #arrange the database into their corresponding categories #transpose the database so it is to read according to category
    usernames, emails, pws, names, genders, dobs, contacts, addresses = [], [], [], [], [], [], [], []
    with open("customer_details.txt", "r") as file:
        for data in file:
            username, email, pw, name, gender, dob, contact, address = data.split("|")
            usernames.append(username)
            emails.append(email)
            pws.append(pw)
            names.append(name)
            genders.append(gender)
            dobs.append(dob)
            contacts.append(contact)
            addresses.append(address)     
    return usernames,emails,pws,names,genders,dobs,contacts,addresses

def addItem(logUsername):
    
    userType = "admin"
    
    print("----------------------------Add Item--------------------------------")
    print("Please key in the information of the product: ")
    category = input("Please select the category by entering the initial:\n\t[f] Food\n\t[m] Medicine\n\t[d] Daily Necessities\n\t").lower()
    addName = input("Product Name: ")
    addPrice = input("Price: ")
    addExpiryDate = input("Expiry Date: ")
    addStocksAvailable = input("Stocks Available: ")
    addDescription = input("Description: ")

    if(category=="f"):
        filename = "groceries_food.txt"
    elif(category=="d"):
        filename = "groceries_daily_necessities.txt"
    elif(category=="m"):
        filename = "groceries_medicine.txt"

    with open(filename, "r") as file:
        rowID = length(file) + 1 #count from 0 so +1

    addItem = f"\n{category}{rowID}|{addName}|{addPrice}|{addExpiryDate}|{addStocksAvailable}|{addDescription}"

    with open(filename, "a") as file:
        file.write(addItem)

    print("Item added")
    print("")
    print("Options:\n\t[1] View Groceries\n\t[2] Main menu\n\t")
    option = input ("Enter your option [1/2]: ")
    if(option=="1"):
        viewGroceries(userType, logUsername)
    elif(option=="2"):
        adminView(logUsername)
    else:
        print("Error, Back to Main Menu")
        adminView(userType, logUsername)

def removeItem(logUsername): #remove item by selecting category 

    userType = "admin"
    
    print("--------------------------Remove Item-------------------------------")
    print("Please select the category by entering the initial:\n\t[f] Food\n\t[m] Medicine\n\t[d] Daily Necessities\n\t")
    category = input("Enter your options: [f/m/d]").lower()

    oldData = []
    ids = []
    if(category=="f"):
        filename = "groceries_food.txt"
    elif(category=="d"):
        filename = "groceries_daily_necessities.txt"
    elif(category=="m"):
        filename = "groceries_medicine.txt"
    
    with open (filename, "r") as file:
        for data in file:
            id, item, price, expdate, stocks, description = data.split("|")
            oldData.append(f"|{item}|{price}|{expdate}|{stocks}|{description}")
            ids.append(id)

            categories = ["ID", "Item", "Price", "Expiry Date", "Stocks Available", "Description"]
            print(f"{categories[0]:5s}{categories[1]:80s}{categories[2]:20s}{categories[3]:20s}{categories[4]:20s}{categories[5]:20s}")
            print(f"{id:5s}{item:80s}{price:20s}{expdate:20s}{stocks:20s}{description:20s}")
 
    deleteId= input("Please enter the item id (only numbers) you would like to remove: ")
    deleteIDRow = findIndex(ids, category + deleteId) 

    with open(filename, "w") as file: 
        for i in range(length(ids)):
            if(i == deleteIDRow):
                continue
            else:
                newData = str(category) + str(i) + oldData[i]
                file.writelines(newData)

    print("Item removed")
    print("")
    print("Options:\n\t[1] View Groceries\n\t[2] Main menu\n\t")
    option = input ("Enter your option [1/2]: ")
    if(option=="1"):
        viewGroceries(userType, logUsername)
    elif(option=="2"):
        adminView(logUsername)
    else:
        print("Error, Back to Main Menu")
        adminView(userType, logUsername)

def searchStock(logUsername): #search stock information for admin

    userType = "admin"

    searchInput = input("Please enter item name to search: ")
    allItemList = []
    with open ("groceries_food.txt","r") as f1, open ("groceries_medicine.txt","r") as f2, open ("groceries_daily_necessities.txt","r") as f3:
        for file in f1,f2,f3:
            for data in file:
                allItemList.append(data.strip("\n"))
    exist = False
    for data in allItemList:
        temp = data.split("|")
        if(searchInput in temp):
            exist = True
            categories = ["ID", "Item", "Price", "expiry Date", "Stocks Available","Description"]
            print(f"{categories[0]:5s}{categories[1]:80s}{categories[2]:20s}{categories[3]:20s}{categories[4]:20s}{categories[5]}")
            print(f"{temp[0]:5s}{temp[1]:80s}{temp[2]:20s}{temp[3]:20s}{temp[4]:20s}{temp[5]}")
            ID = temp[0]
    if(not exist):
        print("No such item")
        searchStock(logUsername)
        
    print("Would you like to edit the item you search?: ")
    option = input ("Enter your option [y/n]").lower()
    if option == "y":
        editGroceries(ID, userType)
    elif option == "n":
        print("Back to Main Menu")
        adminView()
    else:
        print("Invalid input, Back to Main Menu")
        adminView(userType, logUsername)
    
def searchCustomer(logUsername): #search cusrtomer information for admin

    userType = "admin"

    print("--------------------------Searching-------------------------------")
    searchInput = input("Please enter customer's username to search: ")
    exist = False
    print("")

    with open ("customer_details.txt","r") as file:
        for data in file:
            username, email, password, name, gender, dateOfBirth, contact, address = data.split("|")
               
            if(searchInput in username):
                exist = True
                print("--------------------------Found-------------------------------")
                categories = ["Username", "Email", "Password", "Name", "Gender", "DOB", "Phone Number", "Address"]
                print(f"{categories[0]:20s}{categories[1]:30s}{categories[2]:20s}{categories[3]:20s}{categories[4]:20s}{categories[5]:20s}{categories[6]:20s}{categories[7]}")
                print(f"{username:20s}{email:30s}{password:20s}{name:20s}{gender:20s}{dateOfBirth:20s}{contact:20s}{address}")
           
        if(not exist):
            print("--------------------------Error-------------------------------")
            print("Customer does not exist, please try again")

    print("---------------------------------------------------------------------")
    print("Options:\n\t[1] Main Menu\n\t[2] Customer Details\n\t[3] Search Again\n\t")
    option = input ("Enter your option [1/2/3]: ")

    if option == "1":
        adminView(logUsername)     
    elif option == "2":
        customerDetails(userType, logUsername)
    elif option == "3":
        searchCustomer(logUsername)
    else:
        print("Error: Please enter a valid option")
        searchCustomer(logUsername)

def viewGroceries(userType, logUsername): #menu for choosing item category
    print("---------------------------Groceries--------------------------------")
    if userType == "admin":
        print("Options:\n\t[1] Food\n\t[2] Medicine\n\t[3] Daily\n\t[4] Show All\n\t[5] Search and Edit Groceries\n\t")
        option = input ("Enter your option [1/2/3/4/5]: ")
        if(option=="1"):
            viewFood(userType, logUsername)
        elif(option=="2"):
            viewMedicine(userType, logUsername)
        elif(option=="3"):
            viewDailyNecessities(userType, logUsername)
        elif(option=="4"):
            viewAll(userType, logUsername)
        elif(option=="5"):
            searchStock(logUsername)
        else:
            print("Error: Please enter a valid option")
            viewGroceries(userType, logUsername)

    elif userType == "customer" or userType == "newCustomer":
        print("Options:\n\t[1] Food\n\t[2] Medicine\n\t[3] Daily\n\t[4] Show All\n\t")
        option = input ("Enter your option [1/2/3/4]: ")
        if(option=="1"):
            viewFood(userType, logUsername)
        elif(option=="2"):
            viewMedicine(userType, logUsername)
        elif(option=="3"):
            viewDailyNecessities(userType, logUsername)
        elif(option=="4"):
            viewAll(userType, logUsername)
        else:
            print("Error: Please enter a valid option")
            viewGroceries(userType, logUsername)
 
def addCart(userType, logUsername): #buy item & -user input quantity and update stock file
    
    itemIDs = readStocks()[0]
    itemNames = readStocks()[1]
    itemPrices = readStocks()[2]
    stockAvailables = readStocks()[4]

    print("---------------------------------------------------------------------")
    purchaseID = input("Please enter the product ID you wish to purchase: ").lower()
    
    stockID = findIndex(itemIDs, purchaseID) #finding the element index that user input (array, element)
    stockCount = int(stockAvailables[stockID]) #convert to int so can compare, check if out of stock
    
    if(stockCount==0):
        print("Item out of stock")
        addCart(userType, logUsername)
    else:
        print("---------------------------------------------------------------------")
        categories = ["ID", "Item", "Stocks Available"]
        print(f"{categories[0]:5s}{categories[1]:80s}{categories[2]}")
        print  (f"{itemIDs[stockID]:5s}{itemNames[stockID]:80s}{stockAvailables[stockID]}") 

        print("---------------------------------------------------------------------")
        inputQuantity = int(input("Enter your quantity: "))
        if(inputQuantity > stockCount):
            print  ("Please check the quantity remaining and enter again") 
            viewGroceries(userType, logUsername)
        else:
            remainQuantity = stockCount - inputQuantity

            if(purchaseID[0] == "f"):  #decide which data file to modify
                filename = "groceries_food.txt"
            elif(purchaseID[0] == "d"):
                filename = "groceries_daily_necessities.txt"
            elif(purchaseID[0] == "m"):
                filename = "groceries_medicine.txt"
                    
            temp = [] #temporary storage
            with open(filename, "r") as file: 
                content = file.readlines()

            row = int(purchaseID[1:]) #[1:]= only takes the number in the data
            for i in range(length(content)):
                if(i == row):
                    data = content[i]
                    id, item, price, expireDate, stockAvailable, description = data.split("|")
                    newData = f"{id}|{item}|{price}|{expireDate}|{remainQuantity}|{description}"
                    temp.append(newData)
                else:
                    temp.append(content[i].strip('/n'))

        with open (filename, "w") as file1:
            for data in temp:
                file1.writelines(data)

        with open("customer_details.txt", "r") as file: #get customer name
            for data in file:
                customerUsername = data.split("|")[0]

        with open ("cart.txt","a+") as file: #write to cart
            file.write(f"{customerUsername}|{itemIDs[stockID]}|{itemNames[stockID]}|{itemPrices[stockID]}|{inputQuantity}\n")
            print("Item added")

        print("---------------------------------------------------------------------")    
        print("Options:\n\t[1] Back to Groceries Menu\n\t[2] View Cart\n\t[3] Checkout\n\t")
        option = input ("Enter your option [1/2/3]: ")
        if option == "1":
            viewGroceries(userType, logUsername)
        elif option  == "2":
            viewCart(userType, logUsername)
        elif option  == "3":
            checkOut(userType, logUsername)
        else:
            print("Error: Please enter a valid option")
            addCart(userType, logUsername)
      
def viewCart(userType, logUsername):

    customerUsernames, itemIDs, itemNames, itemPrices, itemQuantities = [], [], [], [], []

    with open("cart.txt", "r") as file: #open file and count the length of the file #in 1 loop cannot contain 2 same 'file" as the first time data being counted and the 'file' will become empty
        fileLength = length(file.readlines())

    with open ("cart.txt","r") as file: 
        if(fileLength == 0): # if lenght of file is 0, do this
            print("---------------------------------------------------------------------")
            print("Cart is empty ! Please add something into the cart.")
            viewGroceries(userType, logUsername)
        else:
            for data in file: # else loop through each tile
                customerUsername, itemID, itemName, itemPrice, itemQuantity = data.split("|")
                customerUsernames.append(customerUsername)     
                itemIDs.append(itemID)
                itemNames.append(itemName)
                itemPrices.append(itemPrice)
                itemQuantities.append(itemQuantity)

        print("-----------------------------Cart------------------------------------")
        categories = ["Customer Userame", "Item ID", "Item Name", "Price", "Quantity"]
        print(f"{categories[0]:20s}{categories[1]:20s}{categories[2]:80s}{categories[3]:20s}{categories[4]:20s}")
        for i in range(length(customerUsernames)):
            print(f"{customerUsernames[i]:20s}{itemIDs[i]:20s}{itemNames[i]:80s}{itemPrices[i]:20s}{itemQuantities[i]:20s}") 

        print("---------------------------------------------------------------------")
        print("Options:\n\t[1] Back to Groceries Menu\n\t[2] Checkout\n\t")
        option = input ("Enter your option [1/2]: ") 
        if option == "1":
            viewGroceries(userType, logUsername)
        elif option == "2":
            checkOut(userType, logUsername)
        else:
            print("Error: Please enter a valid option")
            viewCart(userType, logUsername)

def checkOut(userType, logUsername): # chekout, write cart and payment data to purchase history, clear cart file

    cartDetails = []
    print("---------------------------Payment--------------------------------")
    print("Please key in your payment details: ")
    print("Payment method:\n\t[1] Online\n\t[2] Cash on Delivery\n\t[3] Main Menu\n\t")
    option = input("Enter your option [1/2]: ")
    if option == "1":
        paymentOption = "Online"
        print("Please enter your card number: ")
        cardNumber = input("Card number: ")
        print("Please enter CVV: ")
        cardCVV = input("CVV: ")
        print("Details Recorded, Thank you for shopping with us <3")

    elif option == "2":
        paymentOption = "Cash on Delivery"
        cardNumber = "COD"
        cardCVV = "COD"
        print("Details Recorded, Thank you for shopping with us <3")

    elif option == "3":
        if userType == "admin":
            adminView(userType, logUsername)
        elif userType == "customer":
            customerView(userType, logUsername)
    else:
        print("Error: Please enter a valid option")
        checkOut(userType, logUsername)


    with open ("cart.txt","r") as file:
        for data in file:
            cartDetails.append(data.strip('\n'))
                   
    with open ("customer_order_history.txt","a+") as file:
        for i in range(len(cartDetails)):
            file.write(f"{cartDetails[i]}|{paymentOption}|{cardNumber}|{cardCVV}\n")

    print("---------------------------------------------------------------------")
    print("Options:\n\t[1] Main Menu\n\t[2] View Groceries\n\t[3] Purchase History\n\t[4] Exit")
    option = input("Enter your option [1/2/3]: ")
    if option == "1":
        if userType == "admin":
            adminView(userType, logUsername)
        if userType == "customer":
            customerView(userType, logUsername)
    elif option == "2":
        viewGroceries(userType, logUsername)
    elif option == "3":
        purchaseHistory(userType, logUsername)
    elif option == "4":
        exit()
    else:
        print("Error, Back to Main Menu")   
        if userType == "admin":
            adminView(userType, logUsername)
        if userType == "customer":
            customerView(userType, logUsername)
    
def editGroceries(ID, userType):
    
    print("Options:\n\t[1] Edit\n\t[2] Add\n\t[3] Remove\n\t")
    option = input ("Enter your option [1/2/3]: ")
    if option == "1":
        rowInData = int(ID[1:]) - 1
        if(ID[0]=="f"):
            filename = "groceries_food.txt"
        elif(ID[0]=="d"):
            filename = "groceries_daily_necessities.txt"
        elif(ID[0] == "m"):
            filename = "groceries_medicine.txt"
        print("Options:\n\t[1] Price\n\t[2] expiry Date\n\t[3] Stocks Available\n\t[4] Description\n\t")
        editChoice = input("Enter your option [1/2/3/4]: ")
        with open(filename, "r") as file:
            rowCount = 0
            newData = []
            for data in file:
                temp = data.split("|")  
                if(rowCount == rowInData):
                    if(editChoice == "1"):
                        change = input("What you want to change to: ")
                        temp[2] = change
                    elif(editChoice == "2"):
                        change = input("What you want to change to: ")
                        temp[3] = change
                    elif(editChoice == "3"):
                        change = input("What you want to change to: ")
                        temp[4] = change
                    elif(editChoice == "4"):
                        change = input("What you want to change to: ")
                        temp[5] = change
                    else:
                        print("Error: Please enter a valid option")
                        editGroceries(ID, userType)

                    newData.append(f"{temp[0]}|{temp[1]}|{temp[2]}|{temp[3]}|{temp[4]}|{temp[5]}\n")

                else:
                    newData.append(data)
                    
                rowCount += 1
            
        with open(filename, "w") as file:
            for data in newData:
                file.writelines(data)

 


    if userType == "customer":pass
    elif  userType == "admin":pass

def purchaseHistory(userType, logUsername): #show purchase history 
    
    print("-----------------------Purchase History-----------------------------")  
    categories = ["Username", "Item ID", "Item Name", "Item Price", "Quantity", "Payment Option", "Card Number", "CVV"]
    print(f"{categories[0]:10s}{categories[1]:15s}{categories[2]:80s}{categories[3]:20s}{categories[4]:20s}{categories[5]:20s}{categories[6]:20s}{categories[7]}")

    with open ("customer_order_history.txt", "r") as file:
    
        for data in file:
            username, itemID, itemName, itemPrice, quantity, paymentOption, cardNumber, CVV = data.split("|")

            if userType == "admin":
                print(f"{username:10s}{itemID:15s}{itemName:80s}{itemPrice:20s}{quantity:20s}{paymentOption:20s}{cardNumber:20s}{CVV}")
                
            elif userType == "customer":
                if logUsername in username:
                    print(f"{username:10s}{itemID:15s}{itemName:80s}{itemPrice:20s}{quantity:20s}{paymentOption:20s}{cardNumber:20s}{CVV}")
                else:
                    print("You did not purchase anything from the shop before")
                    print("")
                    

    if userType == "admin":
        print("---------------------------------------------------------------------")  
        print("Options:\n\t[1] Main Menu\n\t[2] Search for Customer\n\t")
        option = input("Enter your option [1/2]: ")
        if option == "1":
            adminView(logUsername)
        elif option == "2":
            searchCustomer(logUsername)
        else:
            print("Back to Main Menu")
            adminView(logUsername)
            
    elif userType == "customer":
        print("---------------------------------------------------------------------")        
        print("Back to Main Menu")
        print("")
        customerView(logUsername)

def customerDetails(userType, logUsername): #view customer details
    print("---------------------------Details-----------------------------------")
    with open ("customer_details.txt","r") as file:
  
        categories = ["Username", "Email", "Password", "Name", "Gender", "DOB", "Phone Number", "Address"]
        print(f"{categories[0]:20s}{categories[1]:30s}{categories[2]:20s}{categories[3]:20s}{categories[4]:20s}{categories[5]:20s}{categories[6]:20s}{categories[7]}")

        for data in file:
            username, email, password, name, gender, dateOfBirth, contact, address = data.split("|")
            
            if userType == "admin":
                print(f"{username:20s}{email:30s}{password:20s}{name:20s}{gender:20s}{dateOfBirth:20s}{contact:20s}{address}")

            elif userType == "customer":
                if(logUsername in username):
                    print(f"{username:20s}{email:30s}{password:20s}{name:20s}{gender:20s}{dateOfBirth:20s}{contact:20s}{address}")
               
    if userType == "admin":
        print("---------------------------------------------------------------------")        
        print("Options:\n\t[1] Main Menu\n\t[2] Search for Customer\n\t")
        option = input ("Enter your option [1/2]: ")
        if option == "1":
            adminView(logUsername)
        elif option == "2":
            searchCustomer(logUsername)
        else:
            print("Back to Main Menu")
            adminView(logUsername)

    elif userType == "customer":   
        print("---------------------------------------------------------------------")           
        print("Back to Main Menu")
        print("")
        customerView(logUsername)

def adminView(logUsername): #menu for admin
    print("----------------------------Admin------------------------------------")
    userType = "admin"
    print("Options:\n\t[1] View Groceries\n\t[2] Customer Details\n\t[3] Customer Purchase History\n\t[4] Exit")
    option = input("Enter your option [1/2/3/4]: ")
    if(option=="1"):
        viewGroceries(userType, logUsername)
    elif(option=="2"):
        customerDetails(userType, logUsername)
    elif(option=="3"):
        purchaseHistory(userType, logUsername)
    elif(option=="4"):
        exit()
    else:
        print("Error: Please enter a valid option")  
        adminView(logUsername) 

def customerView(logUsername): #menu for customer
    print("---------------------------Customer----------------------------------")
    userType = "customer"
    print("Options:\n\t[1] View Groceries\n\t[2] Purchase History\n\t[3] Customer Details\n\t[4] Exit")
    option = input("Enter your option [1/2/3/4]: ")
    if(option=="1"):
        viewGroceries(userType, logUsername)
    elif(option=="2"):
        purchaseHistory(userType, logUsername)
    elif(option=="3"):
        customerDetails(userType,logUsername)
    elif(option=="4"):
        exit()
    else:
        print("Error: Please enter a valid option")   
        customerView(logUsername)
  
def register(): #register
    print("--------------------------Registering-------------------------------")
    
    usernames = readCustomerDetails()[0]
    emails = readCustomerDetails()[1]

    username = input("Enter your username: ")
    while(username in usernames):
        print("Username already exists")
        username = input("Enter your username: ")

    email = input("Enter your email: ")
    while(email in emails or "@" not in email or ".com" not in email):
        print("Email already exists or this is not a valid email")
        email = input("Enter your email: ")
    
    pw1 = input("Enter your password:")
    while(length(pw1)<=5):
        print("Password too short")
        pw1 = input("Enter your password:")
    pw2 = input("Enter your comfirmation password: ")
    while(pw1 != pw2):
        print("Passwords not matched")
        pw2 = input("Enter your comfirmation password: ")

    name = input("Enter your full name: ")
    gender = input("Enter your gender (male/female): ")
    dob = input("Enter your date of birth (dd/mm/yyyy): ")
    contact = input("Enter your contact number: ")
    address = input("Enter your address: ")

    with open("customer_details.txt", "a+") as file:
        file.write(f"{username}|{email}|{pw1}|{name}|{gender}|{dob}|{contact}|{address}\n")
    
    print("Register succesfful, returning to menu...")
    start()

def login(): #login (didnt read data correctly)
    print("----------------------------Login------------------------------------")
    logUsername = input("Enter your username: ")
    logPw = input("Enter your password: ")
    admin = False
    customer = False
    
    with open("admin.txt", "r") as file: #admin checking
        for data in file:
            adminUsername, adminEmail, adminPw ,adminName, adminGender, adminDOB, adminContact, adminAddress = data.split("|")
            if(logUsername==adminUsername and logPw==adminPw):
                name = adminName
                admin = True

    with open("customer_details.txt", "r") as file: #customer checking
        for data in file:
            customerUsername = data.split("|")[0]
            customerPw = data.split("|")[2]
            customerName = data.split("|")[3]

            if(logUsername==customerUsername and logPw==customerPw): 
                name = customerName
                customer = True     

    if(admin):
        print("----------------------------Admin------------------------------------")
        print(f"Login successfully, {name}")
        adminView(logUsername)

    elif(customer):
        print("---------------------------Customer----------------------------------")
        print(f"Login successfully, {name}")
        customerView(logUsername)
    
    else:
        option = input("Invalid username or password, [Enter r to retry / Press m to menu]")
        if (option == "r"): 
            login()
        elif (option == "m"):
            start()
        else:
            print("Back to Login")
            login()

def exit(): #exit 
    print("-----------------------------Exit------------------------------------")
    print("Thank you for using FRESHCO Online Shopping")
    print("")

start()