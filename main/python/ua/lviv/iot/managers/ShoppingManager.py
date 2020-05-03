import doctest
from main.python.ua.lviv.iot.models.AbstractShoes import AbstractShoes
from main.python.ua.lviv.iot.models.Boots import Boots
from main.python.ua.lviv.iot.models.Pumps import Pumps
from main.python.ua.lviv.iot.models.Sneakers import Sneakers
from main.python.ua.lviv.iot.models.Sex import Sex
from main.python.ua.lviv.iot.models.DegreeOfOpenness import DegreeOfOpenness
from main.python.ua.lviv.iot.models.Specification import Specification


class ShoppingManager:
    def __init__(self, shoes=None):
        if shoes is None:
            shoes = [Boots(39, 1599.0, "winter", Sex.FEMALE, "ecco", "black", "leather", "wool", "oval", 27.5),
                     Pumps(38, 600.0, "classic", Sex.FEMALE, "ecco", "red", "leather", "leather", "oval", DegreeOfOpenness.MIX),
                     Sneakers(41, 789.9, "summer", Sex.MALE, "Adidas", "blue", "cotton", "", "oval", True, Specification.FOR_TRAINING)]
        self.shoes = shoes

    def find_shoes_by_assignment(self, assignment: str):
        """
        searching shoes by assignment
        >>> print(object_shopping_manager.find_shoes_by_assignment("winter"))
        Information about these shoes: size_eur_standerd = 39, price_in_uah = 1599.0, assignment = winter,
        sex = Sex.FEMALE, brand = ecco, color = black, material_of_vamp = leather, material_of_lining = wool,
        toecap_type = oval, hight_of_shaft_in_sm = 27.5

        """
        found_pairs_of_shoes_by_assignment: list[AbstractShoes] = []
        for pair_of_shoes in self.shoes:
            if pair_of_shoes.assignment == assignment:
                found_pairs_of_shoes_by_assignment.append(pair_of_shoes)
        return found_pairs_of_shoes_by_assignment

    def find_shoes_by_size_eur_standard(self, size_eur_standard):
        """
        searching shoes by assignment
        >>> print(object_shopping_manager.find_shoes_by_size_eur_standard(39))
        [Information about these shoes: size_eur_standerd = 39, price_in_uah = 1599.0, assignment = winter,
        sex = Sex.FEMALE, brand = ecco, color = black, material_of_vamp = leather, material_of_lining = wool,
        toecap_type = oval, hight_of_shaft_in_sm = 27.5]

        """
        found_pairs_of_shoes_by_size_eur_standard: list[AbstractShoes] = []
        for pair_of_shoes in self.shoes:
            if pair_of_shoes.size_eur_standart == size_eur_standard:
                found_pairs_of_shoes_by_size_eur_standard.append(pair_of_shoes)
        return found_pairs_of_shoes_by_size_eur_standard


if __name__ == "__main__":
    doctest.testmod(verbose=True, extraglobs={'object_shopping_manager': ShoppingManager()})
