import random
def message(mess):
    finalmess = ""
    probel = ""
    for i in range(0,10):
        finalmess = finalmess+"[2;"+str(random.randint(30,38))+"m"+probel+mess+"[0m\n"
        probel = probel+" "
    return "```ansi\n"+finalmess+"```"
print(message("Не достаю до пола ногами"))
