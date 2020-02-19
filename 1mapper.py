input = open("purchases.txt", "r")
output = open("01.txt", "w")

for line in input:
    print(line)
    datalist = line.strip().split("    ")
    print(datalist)
    print(len(datalist))
    date, time,store, item, cost, paymentType = datalist
    output.write(paymentType + "\t" + "1" + "\n")

input.close()
output.close()