def charstuffing():
    line=str(input('enter string:'))
    esc=str(input('enter esc:'))
    flag=str(input('enter flag:'))
    text=esc+flag
    l=line.split(flag)
    stuffed=''
    for i in range(len(l)-1):
        stuffed+=l[i]+text
    stuffed+=l[len(l)-1]
    print(stuffed)
charstuffing()    
