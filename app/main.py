from __future__ import annotations
from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner: BurgerRecipe, name: str) -> None:
        self.protected_name = "_" + name

    def __get__(self, instance: BurgerRecipe, owner: BurgerRecipe) -> None:
        return getattr(instance, self.protected_name)

    def __set__(self, instance: BurgerRecipe, value: int | str) -> None:
        setattr(instance, self.protected_name, value)

    @abstractmethod
    def validate(self, value: int | str) -> None:
        pass


class Number(Validator):
    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner: BurgerRecipe, name: str) -> None:
        super().__set_name__(owner, name)

    def __get__(self, instance: BurgerRecipe, owner: BurgerRecipe) -> None:
        return super().__get__(instance, owner)

    def __set__(self, instance: BurgerRecipe, value: int) -> None:
        self.validate(value)
        super().__set__(instance, value)

    def validate(self, value: int) -> None:

        if not isinstance(value, int):
            raise TypeError("Quantity should be integer.")
        else:
            if not self.max_value >= value >= self.min_value:
                raise ValueError(
                    f"Quantity should not be less than {self.min_value}"
                    f" and greater than {self.max_value}.")


class OneOf(Validator):
    def __init__(self, options: tuple) -> None:
        self.options = options

    def __set_name__(self, owner: BurgerRecipe, name: str) -> None:
        super().__set_name__(owner, name)

    def __get__(self, instance: BurgerRecipe, owner: BurgerRecipe) -> None:
        return super().__get__(instance, owner)

    def __set__(self, instance: BurgerRecipe, value: str) -> None:
        self.validate(value)
        super().__set__(instance, value)

    def validate(self, value: str) -> None:
        if value not in self.options:
            raise ValueError(f"Expected {value} to be one of {self.options}.")


class BurgerRecipe:
    buns = Number(2, 3)
    cheese = Number(0, 2)
    tomatoes = Number(0, 3)
    cutlets = Number(1, 3)
    eggs = Number(0, 2)
    sauce = OneOf(("ketchup", "mayo", "burger"))

    def __init__(
            self,
            buns: int,
            cheese: int,
            tomatoes: int,
            cutlets: int,
            eggs: int,
            sauce: str
    ) -> None:
        self.buns = buns
        self.cheese = cheese
        self.tomatoes = tomatoes
        self.cutlets = cutlets
        self.eggs = eggs
        self.sauce = sauce
