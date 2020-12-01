f = open("input.txt","r")
seeking = set()
for n in f:
    # idk how to read n as an int straight from f
    n = int(n)
    if n in seeking: 
        print(n * (2020 - n))
        break
    seeking.add(2020 - n)