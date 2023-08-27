array = [2,6,7,4,8,9,34,56,21,45,66,76,34,78]

sum = 0

for  i in array:
    if i %2 == 0:
        sum += i


print("Dizideki çift sayıların toplamı: " , sum)