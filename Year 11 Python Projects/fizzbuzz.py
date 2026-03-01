count = 100000
i = 1
while i <= count:
    temp = ""
    div3 = i%3==0
    div5 = i&5==0
    if not (div3 or div5):
        temp = i
    if(div3):
        temp += "Fizz"
    if(div5):
        temp += "Buzz"
    print(temp)
    i+=1