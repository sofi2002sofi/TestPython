import doctest
from main.python.ua.lviv.iot.models.AbstractShoes import AbstractShoes
from main.python.ua.lviv.iot.models.Boots import Boots
from main.python.ua.lviv.iot.models.Pumps import Pumps
from main.python.ua.lviv.iot.models.Sneakers import Sneakers
from main.python.ua.lviv.iot.models.Sex import Sex
from main.python.ua.lviv.iot.models.Specification import Specification
from main.python.ua.lviv.iot.models.DegreeOfOpenness import DegreeOfOpenness
from main.python.ua.lviv.iot.models.SortType import SortType


class ShoppingManagerUtil:
    """
    def __init__(self, shoes=None):
        if shoes is None:
            shoes = [Boots(39, 1599.0, "winter", Sex.FEMALE, "Ecco", "black", "leather", "wool", "oval", 27.5),
                     Pumps(38, 600.0, "classic", Sex.FEMALE, "Ecco", "red", "leather", "leather", "oval", DegreeOfOpenness.MIX),
                     Sneakers(41, 789.9, "summer", Sex.MALE, "Adidas", "blue", "cotton", "cotton", "oval", True, Specification.FOR_TRAINING)]
        self.shoes = shoes
    """

    def __init__(self):
        pass

    """
    def sort_shoes_by_price_in_uah(self, sort_type: SortType):
        
        sorting shoes by price in UAH
        >>> print(object_shopping_manager_util.sort_shoes_by_price_in_uah(SortType.ASC))
        [Information about these shoes: size_eur_standerd = 38, price_in_uah = 600.0, assignment = classic,
        sex = Sex.FEMALE, brand = Ecco, color = red, material_of_vamp = leather, material_of_lining = leather,
        toecap_type = oval, degree_of_openness = DegreeOfOpenness.MIX,
        Information about these shoes: size_eur_standerd = 41, price_in_uah = 789.9, assignment = summer,
        sex = Sex.MALE, brand = Adidas, color = blue, material_of_vamp = cotton, material_of_lining = cotton,
        toecap_type = oval, eyelets_presence = True, specification = Specification.FOR_TRAINING,
        Information about these shoes: size_eur_standerd = 39, price_in_uah = 1599.0, assignment = winter,
        sex = Sex.FEMALE, brand = Ecco, color = black, material_of_vamp = leather, material_of_lining = wool,
        toecap_type = oval, hight_of_shaft_in_sm = 27.5]
        
        if sort_type == SortType.ASC:
            self.shoes = sorted(self.shoes, key=lambda shoe: shoe.price_in_uah, reverse=False)
        else:
            self.shoes = sorted(self.shoes, key=lambda shoe: shoe.price_in_uah, reverse=True)
        return self.shoes
    """

    @staticmethod
    def sort_shoes_by_price_in_uah(shoes, sort_type: SortType):
        """
        sorting shoes by price in UAH
        >>> ShoppingManagerUtil.sort_shoes_by_price_in_uah(shoes, SortType.ASC)
        [Information about these shoes: size_eur_standerd = 38, price_in_uah = 600.0, assignment = classic,
        sex = Sex.FEMALE, brand = Ecco, color = red, material_of_vamp = leather, material_of_lining = leather,
        toecap_type = oval, degree_of_openness = DegreeOfOpenness.MIX,
        Information about these shoes: size_eur_standerd = 41, price_in_uah = 789.9, assignment = summer,
        sex = Sex.MALE, brand = Adidas, color = blue, material_of_vamp = cotton, material_of_lining = cotton,
        toecap_type = oval, eyelets_presence = True, specification = Specification.FOR_TRAINING,
        Information about these shoes: size_eur_standerd = 39, price_in_uah = 1599.0, assignment = winter,
        sex = Sex.FEMALE, brand = Ecco, color = black, material_of_vamp = leather, material_of_lining = wool,
        toecap_type = oval, hight_of_shaft_in_sm = 27.5]
        """
        if sort_type == SortType.ASC:
            sorted_shoes = sorted(shoes, key=lambda shoe: str(shoe.price_in_uah), reverse=False)
        else:
            sorted_shoes = sorted(shoes, key=lambda shoe: str(shoe.price_in_uah), reverse=True)
        return sorted_shoes

    """
    def sort_shoes_by_brand(self, sort_type: SortType):
        
        sorting shoes by brand
        >>> print(object_shopping_manager_util.sort_shoes_by_brand(SortType.DESC))
        [Information about these shoes: size_eur_standerd = 38, price_in_uah = 600.0, assignment = classic,
        sex = Sex.FEMALE, brand = Ecco, color = red, material_of_vamp = leather, material_of_lining = leather,
        toecap_type = oval, degree_of_openness = DegreeOfOpenness.MIX,
        Information about these shoes: size_eur_standerd = 39, price_in_uah = 1599.0, assignment = winter,
        sex = Sex.FEMALE, brand = Ecco, color = black, material_of_vamp = leather, material_of_lining = wool,
        toecap_type = oval, hight_of_shaft_in_sm = 27.5,
        Information about these shoes: size_eur_standerd = 41, price_in_uah = 789.9, assignment = summer,
        sex = Sex.MALE, brand = Adidas, color = blue, material_of_vamp = cotton, material_of_lining = cotton,
        toecap_type = oval, eyelets_presence = True, specification = Specification.FOR_TRAINING]
        
        if sort_type == SortType.ASC:
            self.shoes = sorted(self.shoes, key=lambda shoe: shoe.brand, reverse=False)
        else:
            self.shoes = sorted(self.shoes, key=lambda shoe: shoe.brand, reverse=True)
        return self.shoes
    """

if __name__ == '__main__':
    #doctest.testmod(verbose=True, extraglobs={'object_shopping_manager_util': ShoppingManagerUtil()})
    doctest.testmod(verbose=True, extraglobs={"shoes": [Boots(39, 1599.0, "winter", Sex.FEMALE, "Ecco", "black", "leather", "wool", "oval", 27.5), \
Pumps(38, 600.0, "classic", Sex.FEMALE, "Ecco", "red", "leather", "leather", "oval", DegreeOfOpenness.MIX), \
Sneakers(41, 789.9, "summer", Sex.MALE, "Adidas", "blue", "cotton", "cotton", "oval", True, Specification.FOR_TRAINING)]})