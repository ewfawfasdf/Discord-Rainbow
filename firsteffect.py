import random
def message(asd, raz, length, rainbow):
    probel = ""
    textfull = ""
    for i in range(0,length):
        textfull = textfull+"[2;"+str(random.randint(30,37))+"m"+asd[:asd.find(raz)] + probel + asd[asd.find(raz)+len(raz):]+"[0m\n" if rainbow == True else textfull+asd[:len(asd)//2] + probel + asd[len(asd)//2:]+"\n"
        probel = probel+" " if length//2 > i else probel[1:]
    textfull = "```ansi\n"+textfull+"\n```"
    return textfull
print(message("Discord Rainbow, Probels ->-/-/-/-/-<-","-/-/-/-/-", 27, True))
#1 The text itself
#2 Separator, put where you want space 
#3 the length of the spaces
#4 Rainbow text or not (discord only
