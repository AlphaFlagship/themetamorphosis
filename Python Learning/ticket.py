prompt = "\nto get cost of your ticket"
prompt += "\nenter your age"
while True:
    age = input(prompt)
    age = int(age)
    if age == 0:
        break
    else:
        if age <=3:
            print("your icket free")
        elif age <=12:
            print("yor ticket cost 10$")
        else:
            print("your ticket cost $20")
print("thnx")