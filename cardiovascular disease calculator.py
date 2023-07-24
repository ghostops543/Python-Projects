# cardiovascular diseas calculator
sex = input('are you male or female')
age = int(input("what is your age"))
cho = int(input('what is your cholesterol'))
smo = input('do you smoke (yes/no)')
hdl = int(input('what is your HDL'))
bp = int(input('what is your systolic bp'))
bpstatus = input('are you taking medicine for your systolic bp(yes/no)')
points = 0
# determines whether male or female
if sex == 'male':
    # sets points for age including cholesterol and smoking
    if 20 < age < 39:
        if 160 < cho < 199:
            points += 4
        elif 200 < cho < 239:
            points += 7
        elif 240 < cho < 279:
            points += 9
        elif cho >= 280:
            points += 11
        if 20 < age < 34:
            points += -9
        elif 35 < age < 39:
            points += -4
        if smo == 'yes':
            points += 8
    if 40 < age < 49:
        if 160 < cho < 199:
            points += 3
        elif 200 < cho < 239:
            points += 5
        elif 240 < cho < 279:
            points += 6
        elif cho >= 280:
            points += 8
        if 45 < age < 49:
            points += 3
        if smo == 'yes':
            points += 5
    if 50 < age < 59:
        if cho < 160:
            points += 0
        elif 160 < cho < 199:
            points += 2
        elif 200 < cho < 239:
            points += 3
        elif 240 < cho < 279:
            points += 4
        elif cho >= 280:
            points += 5
        if 50 < age < 54:
            points += 6
        elif 55 < age < 59:
            points += 8
        if smo == 'yes':
            points += 3
    if 60 < age < 69:
        if 160 < cho < 199:
            points += 1
        elif 200 < cho < 239:
            points += 1
        elif 240 < cho < 279:
            points += 2
        elif cho >= 280:
            points += 3
        if 60 < age < 64:
            points += 10
        elif 65 < age < 69:
            points += 11
        if smo == 'yes':
            points += 1
    if 70 < age < 79:
        if 240 < cho < 279:
            points += 1
        elif cho >= 280:
            points += 1
        if 70 < age < 74:
            points += 12
        elif 75 < age < 79:
            points += 13
        if smo == 'yes':
            points += 1
    # sets points for hdl
    if hdl >= 60:
        points += -1
    elif 40 < hdl < 49:
        points += 1
    elif hdl < 40:
        points += 2
    # checks if taking medication and calculates points based on bp
    if bpstatus == 'yes':
        if 120 < bp < 129:
            points += 1
        elif 130 < bp < 139:
            points += 2
        elif 140 < bp < 159:
            points += 2
        elif bp >= 160:
            points += 3
    elif bpstatus == 'no':
        if 130 < bp < 139:
            points += 1
        elif 140 < bp < 159:
            points += 1
        elif bp >= 160:
            points += 2
    # outputs risk factor
    if points < 1:
        print('your 10 year risk is less than 1%')
    elif 0 <= points <= 4:
        print('your 10 year risk is 1%')
    elif 5 <= points <= 6:
        print('your 10 year risk is 2%')
    elif points == 7:
        print('your 10 year risk is 3%')
    elif points == 8:
        print('your 10 year risk is 4%')
    elif points == 9:
        print('your 10 year risk is 5%')
    elif points == 10:
        print('your 10 year risk is 6%')
    elif points == 11:
        print('your 10 year risk is 8%')
    elif points == 12:
        print('your 10 year risk is 10%')
    elif points == 13:
        print('your 10 year risk is 12%')
    elif points == 14:
        print('your 10 year risk is 16%')
    elif points == 15:
        print('your 10 year risk is 20%')
    elif points == 16:
        print('your 10 year risk is 25%')
    elif points >= 17:
        print('your 10 year risk is 30% or greater')
elif sex == 'female':
    # sets points for age including cholesterol and smoking
    if 20 < age < 39:
        if 160 < cho < 199:
            points += 4
        elif 200 < cho < 239:
            points += 8
        elif 240 < cho < 279:
            points += 11
        elif cho >= 280:
            points += 13
        if 20 < age < 34:
            points += -7
        elif 35 < age < 39:
            points += -3
        if smo == 'yes':
            points += 9
    if 40 < age < 49:
        if 160 < cho < 199:
            points += 3
        elif 200 < cho < 239:
            points += 6
        elif 240 < cho < 279:
            points += 8
        elif cho >= 280:
            points += 10
        if 45 < age < 49:
            points += 3
        if smo == 'yes':
            points += 7
    if 50 < age < 59:
        if 160 < cho < 199:
            points += 2
        elif 200 < cho < 239:
            points += 4
        elif 240 < cho < 279:
            points += 5
        elif cho >= 280:
            points += 7
        if 50 < age < 54:
            points += 6
        elif 55 < age < 59:
            points += 8
        if smo == 'yes':
            points += 4
    if 60 < age < 69:
        if 160 < cho < 199:
            points += 2
        elif 200 < cho < 239:
            points += 3
        elif 240 < cho < 279:
            points += 4
        elif cho >= 280:
            points += 5
        if 60 < age < 64:
            points += 10
        elif 65 < age < 69:
            points += 12
        if smo == 'yes':
            points += 2
    if 70 < age < 79:
        if 160 < cho < 199:
            points += 1
        elif 200 < cho < 239:
            points += 1
        elif 240 < cho < 279:
            points += 2
        elif cho >= 280:
            points += 2
        if 70 < age < 74:
            points += 14
        elif 75 < age < 79:
            points += 16
        if smo == 'yes':
            points += 1
    # sets points for hdl
    if hdl >= 60:
        points += -1
    elif 40 < hdl < 49:
        points += 1
    elif hdl < 40:
        points += 2
    # checks if taking medication and calculates points based on bp
    if bpstatus == 'yes':
        if 120 < bp < 129:
            points += 3
        elif 130 < bp < 139:
            points += 4
        elif 140 < bp < 159:
            points += 5
        elif bp >= 160:
            points += 6
    elif bpstatus == 'no':
        if 120 < bp < 129:
            points += 1
        elif 130 < bp < 139:
            points += 2
        elif 140 < bp < 159:
            points += 3
        elif bp >= 160:
            points += 4
    # outputs risk factor
    if points < 9:
        print('your 10 year risk is less than 1%')
    elif 9 <= points <= 12:
        print('your 10 year risk is 1%')
    elif 13 <= points <= 14:
        print('your 10 year risk is 2%')
    elif points == 15:
        print('your 10 year risk is 3%')
    elif points == 16:
        print('your 10 year risk is 4%')
    elif points == 17:
        print('your 10 year risk is 5%')
    elif points == 18:
        print('your 10 year risk is 6%')
    elif points == 19:
        print('your 10 year risk is 8%')
    elif points == 20:
        print('your 10 year risk is 11%')
    elif points == 21:
        print('your 10 year risk is 14%')
    elif points == 22:
        print('your 10 year risk is 17%')
    elif points == 23:
        print('your 10 year risk is 22%')
    elif points == 24:
        print('your 10 year risk is 27%')
    elif points >= 25:
        print('your 10 year risk is 30% or greater')
