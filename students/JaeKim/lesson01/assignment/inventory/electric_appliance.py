"""
Electric appliances class
"""

from .inventory import Inventory


class ElectricAppliance(Inventory):
    """
    Electric appliances class
    """

    # Replace using kwargs for too many arguments as an option
    def __init__(self, product_code, description, market_price, rental_price, brand, voltage):

        #super().__init__(args)
        Inventory.__init__(self, product_code, description, market_price, rental_price)

        self.brand = brand
        self.voltage = voltage

    def return_as_dictionary(self):
        """
        Return furniture as dict
        """
        output_dict = Inventory.return_as_dictionary(self)
        output_dict['brand'] = self.brand
        output_dict['voltage'] = self.voltage

        return output_dict
