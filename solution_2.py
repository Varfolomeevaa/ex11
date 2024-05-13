import code


class Good:
    """
    The Good class represents an item with a unique barcode and price.

    Attributes:
        info (str): A string containing information about the item, separated by spaces.
        __cod (str): The barcode of the item. Private attribute.
        country (str): The country of origin of the item, determined from the barcode.
        check_digit (str): The check digit of the barcode.
        price (int): The price of the item.

    Methods:
        cod (property): Returns the barcode of the item.
        cod (cod.setter): Sets a new value for the barcode.
        country_fr_code (staticmethod): Determines the country of origin from the code.
        __eq__ (magic method): Compares items based on their information.
        __str__ (magic method): Returns a string representation of the item's information.
        __repr__ (magic method): Returns a string representation of the Good class object.
    """
    def __init__(self, info):
        """
        Initialize a new Good object with information about the item.
        Parameters:
            info (str): A string of information about the item, separated by spaces.
        """
        self.info = info.split()
        self.__cod = self.info[0]
        self.country = Good.country_fr_code(self.__cod[:3])
        self.check_digit = self.__cod[-1]
        self.price = int(self.info[1])

    @property
    def cod(self):
        """
        Return the barcode of the item.
        Returns:
            str: The barcode of the item.
        """
        return self.__cod

    @cod.setter
    def cod(self, new_value):
        """
        Set a new value for the item's barcode.
        Parameters:
            new_value (str): The new barcode value.
        """
        self.__cod = self.__cod

    @staticmethod
    def country_fr_code(cntr):
        """
        Determine the country of origin of the item from the code.
        Parameters:
            cntr (str): The country code.
        Returns:
            str: The country of origin of the item.
        """
        for x in code.country:
            if cntr[:2] in code.country[x] or cntr in code.country[x]:
                return x

    def __eq__(self, other):
        """
        Compare this item with another item.
        Parameters:
            other (Good): Another Good object to compare with.
        Returns:
            bool: True if the items are equal, False otherwise.
        """
        return self.info == other.info

    def __str__(self):
        """
        Return a string representation of the item's information.
        Returns:
            str: The item information as a string.
        """
        return f'Штрих-код: {self.__cod}; Страна: {self.country}; Цена: {self.price}'

    def __repr__(self):
        """
        Return an official string representation of the Good object.
        Returns:
            str: The official representation of the object.
        """
        return self.__str__()


class Basket:
    """
    The Basket class represents a shopping basket.

    Attributes:
        all_goods (list): A list of all the items in the basket.
        __cost_goods (int): The total cost of the items in the basket. Private attribute.

    Methods:
        cost_goods (property): Returns the total cost of the goods in the basket.
        cost_goods (cost_goods.setter): Sets a new cost for the goods in the basket.
        add_good (method): Adds a new item to the basket and updates the total cost.
        delete_good (method): Removes an item from the basket and updates the total cost.
        __str__ (magic method): Returns a string representation of the items in the basket and the total cost.
        __repr__ (magic method): Returns a string representation of the Basket class object.
    """
    def __init__(self):
        """
        Initialize a new Basket object with information about the item.
        """
        self.all_goods = []
        self.__cost_goods = 0

    @property
    def cost_goods(self):
        """
        Get the total cost of the goods in the basket.
        Returns:
            int: The total cost of the goods in the basket.
        """
        return self.__cost_goods

    @cost_goods.setter
    def cost_goods(self, new_cost):
        """
        Set a new total cost for the goods in the basket.
        Parameters:
            new_cost (int): The new total cost of the goods.
        """
        self.__cost_goods = self.__cost_goods

    def add_good(self, new_good):
        """
        Add a new item to the basket and update the total cost.
        Parameters:
            new_good (Good): The Good object to add to the basket.
        Returns:
            None
        """
        self.all_goods.append(new_good)
        self.__cost_goods += new_good.price

    def delete_good(self, del_good):
        """
        Remove an item from the basket and update the total cost.
        Parameters:
            del_good (Good): The Good object to remove from the basket.
        Returns:
            None
        """
        self.all_goods.remove(del_good)
        self.__cost_goods -= del_good.price

    def __str__(self):
        """
        Return a string representation of the good's information.
        Returns:
            str: The good information as a string.
        """
        return (f'Товары в корзине: \n'
                f'{"\n".join([str(i) for i in self.all_goods])} \n'
                f'Общая стоимость корзины: {self.__cost_goods}')

    def __repr__(self):
        """
        Return an official string representation of the Basket object.
        Returns:
            str: The official representation of the object.
        """
        return self.__str__()
