from abc import abstractmethod


class Validator:
    def __set_name__(self, owner, name: str) -> None:
            self.protected_name = '_' + name

    def __get__(self, obj, obj_type=None):
        value = getattr(obj, self.protected_name)
        return value

    def __set__(self, instance, value):
        setattr(instance, self.protected_name, value)

    @abstractmethod
    def validate(self, value):
        pass

class Number(Validator):
    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def validate(self, value: int) -> int:
        if not isinstance(value, int):
            raise TypeError("Quantity should be integer.")

        if not self.max_value >= value >= self.min_value:
            raise ValueError(
                f"Quantity should not be less than"
                f" {self.min_value} and greater than {self.max_value}.")
        return value



class OneOf(Validator):
    def __init__(self, options):


class BurgerRecipe:
    def __init__(self,
                 buns: int=1,
                 cheese: int=1,
                 tomatoes: int=1,
                 cutlets: int=1,
                 eggs: int=0,
                 sauce: str="ketchup"):
