sand_orders = ['plain', 'cheese','pastarami','veg' ,'italian','roasted','plain','pastarami','cheese','pastarami','pastarami']
finished = []
while sand_orders:
    current = sand_orders.pop()
    if current == 'pastarami':
        print("no pasta")
        while 'pastarami' in sand_orders:
            sand_orders.remove('pastarami')

            
        continue
    else:
        

        print(f"\norder complete {current}")
        finished.append(current)
print("today we made:")
for made in finished:
    print(made)
print(finished)
print(sand_orders)