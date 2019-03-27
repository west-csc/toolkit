def make_pig_latin(string):
    vowels = ["a","e","i","o","u"]
    words = string.split(' ')
    newword = []
    for word in words:
        if(word[0] in vowels):
            word = word + "yay"
            newword += [word]
        elif(word[0] not in vowels):
            word = word[1:] + word[0]
            word += "ay"
        newword += [word]
    return ' '.join([str(i) for i in newword])