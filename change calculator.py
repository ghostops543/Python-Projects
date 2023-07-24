#change calculator
pay = round(float(input("how much did you pay")),2)
cost = round(float(input("how much did it cost")),2)
change = round((pay - cost),2)
print("you receive",change,"in change that is...")
if change>=0:
    dochange = round((change % 1),2)
    dollars = (change-dochange) / 1
    if dollars != 0:
        print(round(dollars), "dollars")
if change>=0:
    qchange = (dochange % .25)
    quarters= (dochange-qchange) / .25
    if quarters != 0:
        print(round(quarters),"quarters")
if change>=0:
    dchange = qchange % .10
    dime= (qchange-dchange) / .10
    if dime !=0:
        print(round(dime),"dimes")
if change >= 0:
    nchange= dchange % .05
    nickles = (dchange-nchange) / .05
    if nickles != 0:
        print(round(nickles),"nickles")
if change>=0:
    pennies= nchange / .01
    if pennies != 0:
        print(round(pennies),"pennies")