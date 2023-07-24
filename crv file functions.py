#functions for crv files
def rows(filename):
    with open(filename, 'r') as file:  # opens file and returns the amount of rows in the file
        file = file.read()
        file = file.split('\n')
        return len(file)


def columns(filename):
    with open(filename, 'r') as file:  # opens file and returns how many columns it has
        file = file.read()
        file = file.split('\n')
        file = file.split(',')
        return len(file[0])


def key(filename):
    with open(filename, 'r') as file:  # opens file and prints the first row
        file = file.read()
        file = file.split('\n')
        return file[1]


def sumrows(filename, rownum):
    with open(filename, 'r') as file:  # opens input
        with open('output.txt', 'a') as output:  # opens output
            sum = 0  # creates empty variable
            file = file.read()  # read input file
            # splits file at new line and commas
            file = file.split('\n')
            for i in range(0, len(file)):
                file[i] = file[i].split(",")
            for j in range(0, len(file[1])):  # adds all the numbers together
                sum += float(file[rownum][j])
            output.write(f'the sum of row {rownum} is {sum}\n')


def sumcolumns(filename, columnnum):
    with open(filename, 'r') as file:  # opens input
        with open('output.txt', 'a') as output:  # opens output
            sum = 0
            file = file.read()
            # splits the file at new lines and commas
            file = file.split('\n')
            for i in range(0, len(file)):
                file[i] = file[i].split(",")
                # adds all the numbers together
            for j in range(1, len(file)):
                sum += float(file[j][columnnum])
            output.write(f'the sum of colum {columnnum} is {sum}\n')  # writes it to the file
    return sum
