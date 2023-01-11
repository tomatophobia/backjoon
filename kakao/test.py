x = ['1', '3', '5', '7', '9']

count = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    count += 1
                    print(x[i] + x[j] + x[k] + x[l] + x[m] + ' 3 7')
print(count)
