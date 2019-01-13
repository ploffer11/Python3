class Inventory:
    def lock(self, item_type):
        """
        Select the type of item that is going to be manipulated.
        This method will lock the item so nobody else can manipulate
        the inventory until it's returned.
        This prevents selling the same item to two different customers.
        """

    def unlock(self, item_type):
        """
        Release the given type so that other customers can access it.
        """

    def purchase(self, item_type):
        """
        If the item is not locked, raise an exception.
        If the item is currently out of stock, raise an exception.
        If the item is available, subtract one item and return the
        number of items left.  
        """

item_type = "widget"
inv = Inventory()
inv.lock(item_type)

try:
    num_left = inv.purchase(item_type)
except InvalidItemType:
    print(f"Sorry, we don't sell {item_type}")
except OutOfStock:
    print("Sorry, that item is out of stock.")
else:
    print(f"Purchase complete. There are {num_left} {item_type}s left")
finally:
    inv.unlock(item_type) 