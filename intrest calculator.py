#intrest rate calculator and creates file with info
p = int(input('what is the loan amount'))  # loan amount
r = float(input('what is the interest rate as a decimal'))  # interest
n = int(input('how many times is it compounded yearly'))  # amount of compounds per year
# calculates the total repay, interest, and principal repay
total_repay = round(p * (((r / n) * ((1 + r / n) ** n)) / (((1 + r / n) ** n) - 1)),2)
interest_pay = round(p * (r / n),2)
principle_repay = round(total_repay - interest_pay,2)
remainder = p
cnt = 0
if n > 30:
    num = 30
else:
    num = n
with open('loan.crv','w') as loan:  # opens the file
    loan.write('payments made, monthly payment, interest, total payment, remainder \n')
    while int(cnt) <= num:  # creates a table of all the payments
        if cnt == 0:  # prints the zero month info
            loan.write(f'{cnt}, 0, {interest_pay}, 0, {p}\n')
        elif cnt != 0:  # prints the rest of the month info
            remainder = round(remainder - principle_repay,2)
            loan.write(f'{cnt}, {principle_repay}, {interest_pay}, {total_repay}, {remainder}\n')
            p = remainder
            interest_pay = round(p * (r / n), 2)
            principle_repay = round(total_repay - interest_pay, 2)
        cnt +=1






