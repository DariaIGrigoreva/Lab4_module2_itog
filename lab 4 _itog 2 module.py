from typing import Union

if __name__ == "__main__":

    class Hydromachine:
        """ Базовый класс гидравлических машин. """

        def __init__(self, kind: str, blade: int):
            self._kind = kind
            self._blade = blade

        """ базовый и дочерний класс ничем не отличается, значит метод str и eq можно унаследовать """
        def __str__(self):
            return f"Тип гидравлической машины {self.kind}. Количество лопастей {self._blade}"

        def __eq__(self, other):
            return self.kind == other.kind

        """ базовый и дочерний класс в части переменнных: velocity и head отличаются, значит метод repr можно перегрузить """
        def __repr__(self):
            return f"{self.__class__.__name__}(kind={self.kind!r}, blade={self.blade!r})"

        @property
        def kind(self) -> str:
            return self._kind

        @property
        def blade(self) -> int:
            return self._blade
        """атрибут kind и blade изменяться не могут"""

    class Pump(Hydromachine):
        """ Дочерний класс Насосов ( тип, количество лопастей, скорость)"""
        def __init__(self, kind: str, blade: int, velocity: Union[int, float]):
            super().__init__(kind, blade)
            self.velocity = velocity

        def __repr__(self):
            return f"{self.__class__.__name__}(kind={self.kind!r}, blade={self.blade!r}, velocity={self.velocity!r})"

        # атрибут velocity отсутствует в базовом классе

        """Статические методы используются как вспомогательные функции для проверки аргументов (velocity)"""
        @property
        def velocity(self) -> Union[int, float]:
            return self._velocity

        @velocity.setter
        def velocity(self, velocity: Union[int, float]) -> None:
            if not isinstance(velocity, (int, float)):
                raise TypeError
            if not velocity > 0:
                raise ValueError
            self._velocity = velocity

    # velocity не может быть меньше 0 и значение может быть не целым

    class Turbine(Hydromachine):
        """ Дочерний класс Турбин (тип, количество лопастей, напор) """
        def __init__(self, kind: str, blade: int, head: Union[int, float]):
            super().__init__(kind, blade)
            self.head = head

        def __repr__(self):
            return f"{self.__class__.__name__}(kind={self.kind!r}, blade={self.blade!r}, head={self.head!r})"

        # атрибут head отсутствует в базовом классе

        """Статические методы используются как вспомогательные функции для проверки аргументов (head)"""
        @property
        def head(self) -> Union[int, float]:
            return self._head

        @head.setter
        def head(self, head: Union[int, float]) -> None:
            if not isinstance(head, (int, float)):
                raise TypeError
            if not head > 0:
                raise ValueError
            self._head = head

        # head не может быть меньше 0 и значение может быть не целым

    pass

