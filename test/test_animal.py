from package import __version__
import unittest as ut
import pytest
from package.animal import Animal, Dog, Human


class NgTest01(Animal):
    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old
        self.animal_name = ""
        self.animal_cry = ""

    def cry(self) -> str:
        return ""


class NgTest02(Animal):
    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old
        self.animal_name = ""
        self.animal_cry = ""

    def age_conversion(self) -> str:
        return ""


class SpTest(ut.TestCase):

    def test_version(self):
        assert __version__ == '0.1.0'

    def test_dog(self):
        kaede_dog = Dog(name="楓", old=2)
        kaede_dog.age_conversion()
        kaede_dog.cry()

    def test_human(self):
        aoi_human = Human(name="時巻あおい", old=18)
        aoi_human.age_conversion()
        aoi_human.cry()
        aoi_human.print_test("test", "message")

    def test_ng_age(self):
        # TypeErrorを検知
        with pytest.raises(TypeError) as e:
            _ = NgTest01(name="aaa", old=50)

        # エラーメッセージを検証
        assert str(e.value) == "Can't instantiate abstract class NgTest01 with abstract method age_conversion"

    def test_ng_cry(self):
        # TypeErrorを検知
        with pytest.raises(TypeError) as e:
            _ = NgTest02(name="bbb", old=30)

        # エラーメッセージを検証
        assert str(e.value) == "Can't instantiate abstract class NgTest02 with abstract method cry"
