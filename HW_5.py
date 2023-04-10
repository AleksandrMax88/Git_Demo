class Shop():

    def __init__(self, dep_name, good_name, how_many, price):
        self.dep_name = dep_name
        self.good_name = good_name
        self.how_many = how_many
        self.price = price

    def all_price(self):
        return int(self.how_many) * float(self.price)


shop1 = Shop('Foodmarket', 'eggs', 400, 7)
print(shop1.dep_name)
print(shop1.good_name)
print(shop1.how_many)
print(shop1.all_price())
print(f'В магазине {shop1.dep_name} находится {shop1.how_many} {shop1.good_name} на общую сумму {shop1.all_price()} грн.')
shop2 = Shop('Annamarket', 'eggs', 800, '6.5')
print(shop2.dep_name)
print(shop2.good_name)
print(shop2.how_many)
print(shop2.all_price())
print(f'В магазине {shop2.dep_name} находится {shop2.how_many} {shop2.good_name} на общую сумму {shop2.all_price()} грн.')