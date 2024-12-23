def format(x,length):
    c = str(x)
    while(True):
        if(len(c)==length):
            break
        c = "0"+c
    return c

tp = "9999"
x = 0
while True:
    num = format(x,4)
    x += 1
    if num == tp:break
    df = open('wordlist-password1.txt', 'a', encoding='utf-8')
    df.writelines(num+'\n')
    df.close