import random
upper = True
a = list(str(input()))
for i in range(len(a)):
    if upper == True:
        a[i] = "["+str(random.randint(1,4))+";"+str(random.randint(30,47))+"m"+a[i].upper()+"[0m"
    else:
        a[i] = "["+str(random.randint(1,4))+";"+str(random.randint(30,47))+"m"+a[i].lower()+"[0m"
    upper = not upper
print("```ansi\n"+''.join(a)+"\n```")
