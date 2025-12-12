def coins_convert(sentence):

    penny = 0.01  #Set value of coins
    nickel = 0.05
    dime = 0.10
    quarter = 0.25

    total = 0.0

    #Deciphers each side of the sentence after / before and
    parts = sentence.split(' and ')


    for part in parts:

        pieces = part.split()
        number = int(pieces[0]) #Convert amount of said coins to an integer
        coin = pieces[1]  #Coin name

        #Checks coin name and adds amount to that specific one
        if coin == "penny" or coin == "pennies":
            total += number * penny
        elif coin == "nickel" or coin == "nickels":
            total += number * nickel
        elif coin == "dime" or coin == "dimes":
            total += number * dime
        elif coin == "quarter" or coin == "quarters":
            total += number * quarter


    return round(total, 2) #rounding to two decimal places to match normal money format

#uses function to break down the sentence and show correct output
print (coins_convert("1 penny and 2 nickels"))
print (coins_convert("4 dimes and 7 quarters"))
print (coins_convert("1 quarter and 3 pennies"))
print (coins_convert("21 pennies and 17 dimes and 52 quarters"))
print (coins_convert("95 dimes and 73 quarters and 22 nickels and 36 pennies"))
print (coins_convert("1 nickel and 17 quarters"))
print (coins_convert("21 nickels and 15 pennies"))
print (coins_convert("1 dime and 1 nickel and 1 penny and 1 quarter"))





