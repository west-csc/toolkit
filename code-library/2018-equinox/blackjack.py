values = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']

counter = 0
for i in range(3):
    a = input()
    if((a == "J" or a == "Q") or (a == "K")):
        counter+=10
    elif((a=="A") and (counter + 11 > 21)):
        counter+=1
    elif(a == "A" and (counter + 11 <= 21)):
        counter+=11
    else:
        counter += int(a)
    




print(counter)