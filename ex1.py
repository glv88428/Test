with open("data.txt", "r") as file:
    sum=0
    for line in file:
        try:
            a=int(line.strip())
            sum+=a
        except ValueError:
            pass
print(sum)