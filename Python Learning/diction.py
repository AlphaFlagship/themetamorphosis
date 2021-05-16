class Restaurant:
    """
    To show about restaurant    
    """
    def __init__(self, name,cuisine):
        """
        name and cuisine attribute
        """
        self.name=name
        self.cuisine=cuisine
        self.number_served=0
    def des_res(self):
        """
        description
        """
        print(f"{self.name} is great restaurant. You will love its famous {self.cuisine} food")
    def open_res(self):
        """
        its open
        """
        print(f"{self.name} is open now.")
    def servings(self):
        """
        no of customers served
        """
        print(f"No. of people served:- {self.number_served}")
    def set_served_customer(self, orders):
        """
        For setting number of customer served
        """
        self.number_served = orders
       
    def increment_servings(self, new_order):
        """
        increased order number
        """
        self.number_served += new_order
class IceCream_stand(Restaurant):
    def __init__(self, name,cuisine):
        """
        Child class for icecream stand
        """
        super().__init__(name,cuisine)
        self.taste=flavs
    def flavours(self):
        """
        add flavour
        """
        for flav in flavs:
            print(f"\n{flav} is available.")
flavs = ['Choco','vanilla','mango']
my_res = Restaurant('toi','veg')
print(f"Name is {my_res.name}")
my_res.des_res()
my_res.open_res()
my_res.set_served_customer(7)
my_res.increment_servings(4)
my_res.servings()
myparlour = IceCream_stand('TopnTown','dessert')
print(myparlour.des_res())
myparlour.flavours()
