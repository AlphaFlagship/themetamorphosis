store = [value for value in range(1,100)]
for number in store:
    if number==1 :
        print(f"{number}st")
    elif number==2:
        print(f"{number}nd")
    elif number==3:
        print(f"{number}rd")
    else:
        print(f"{number}th")


print(store)