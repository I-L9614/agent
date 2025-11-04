class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price =float(price)
        self.category = category
        self.status = True

    def get_info(self):
        return f"Order: {self.name}, Price: {self.price}, Category: {self.category}"    
    
    def set_available(self, status:bool):
        self.status = status

    def is_available(self):
        return self.status

class Menu:
    def __init__(self):
        items = []    

    def add_item(self, menu_item:MenuItem):
        self.items.append(menu_item)

    def remove_item(self, item_name):
        for i in self.items:
            if i.name == item_name:
                i.remove
            else:
                continue
    def get_item_by_name(self, name):
        for i in self.items:
            if i.name == name:
                return i
            else:
                return False
    
    def get_item_by_category(self, category):
        in_category = []
        for i in self.items:
            if i.category == category:
                in_category.append(i)
            else:
                continue
    
    def display_menu(self):
        available = []
        for i in self.items:
            if i.status:
                available.append(i)
            else:
                continue
        return sorted(available)
    
    def get_total_items(self):
        return f'items on menu:{len(self.items)}'
    
class Customer:
    def __init__(self, name):
        self.name = name
        self.satisfaction = 50 

    def increase_satisfaction(self, amount):
        if (amount+self.satisfaction) > 50:
            self.satisfaction = 100
        else:
            self.satisfaction += amount   
    
    def decrease_satisfaction(self, amount):
        if (amount - self.satisfaction) < 0:
            self.satisfaction = 0
        else:
            self.satisfaction -+ amount

    def is_hapy(self):
        return self.satisfaction > 70
    
    def get_info(self):
        return f"Customer: {self.name}, satisfaction: {self.satisfaction}"

class Order:
    def __init__(self, Customer, order_number):
        self.Customer = Customer
        self.order_number = order_number
        self.items = []
        self.status = 'pending'
        self.total_price = 0

    def add_item(self, menu_item):
        self.items.append(menu_item)
        self.total_item += menu_item.price

    def remove_item(self, menu_item):
        self.item.remove(menu_item)
        self.total_price -= menu_item.price

    def get_total(self):
        return self.total_price
    
    def set_status(self, new_status):
        self.status = new_status

    def display_order(self):
        print(f"number: {self.order_number}, customer: {self.Customer}, items: {self.items}, total: {self.total_price}, status: {self.status}")
    
    def is_complete(self):
        if self.status == 'delivered':
            return True    