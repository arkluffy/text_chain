import requests

def check(word):
    chc = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)
    if 'title' in chc.json():
        return False
    else:
        return True

pt = 0
ctwr = 0
a = str(input('enter word: '))
if check(a) == True:
    print('word is correct')
    pt += 1
else:
    print('word is incorrect')
    ctwr += 1
while ctwr == 0:
    b = str(input('enter word: '))
    if check(b) == False:
        print('word is incorrect')
        ctwr += 1
    else:
        if a[-1] == b[0]:
            print('last letter of the previous word is the same as the first letter of the next word')
            pt += 1
            a = b
        else:
            print('last letter of the previous word is not the same as the first letter of the next word')
            ctwr += 1
print('you got ' + str(pt) + ' points')

    
