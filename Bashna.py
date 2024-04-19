import random
def message(mess):
    final = ""
    for i in range(0,len(mess)):
        final = final+"[2;"+str(random.randint(30,38))+"m"+mess[len(mess)+-i:]+mess[:len(mess)+-i]+"[0m\n"
    return "```ansi\n"+final+"```"
print(message("Камерамен протиф шкебеде талчка"))
