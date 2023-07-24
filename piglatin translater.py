# turns word to pig latin
def piglatin(word):
    firstlet = str(word[0:1]).lower()
    pigword = word[1:len(word)]
    if firstlet not in ['a', 'e', 'i', 'o', 'u']:
        return pigword + firstlet + 'ay'
    else:
        return word + 'yay'

# lets users keep translating till stop is inputted
while 1 == 1:
    userinput = str(input())
    if userinput == 'stop':
        break
    else:
        print(piglatin(userinput))
