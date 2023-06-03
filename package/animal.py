from abc import ABCMeta, abstractmethod
from decimal import Decimal, ROUND_HALF_UP
import math


def my_round(f: float):
    return Decimal(str(f)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)


class Animal(metaclass=ABCMeta):
    """
    動物を表現する際の抽象基底クラス

    """

    @abstractmethod
    def cry(self):
        """
        鳴き声の説明

        動物がどのように鳴くかを表示する
        """
        raise NotImplementedError("鳴き声の説明は実装必須です")

    @abstractmethod
    def age_conversion(self):
        """
        年の説明

        人間の年齢に換算した際に、動物が何歳であるかを表示する
        """
        raise NotImplementedError("年齢の説明は実装必須です")


class Dog(Animal):

    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old
        self.animal_name = "犬"
        self.animal_cry = "ワンワン"

    def cry(self) -> str:
        """
        鳴き声の説明

        犬がどのように鳴くかを表示する
        """
        ret_str = f"{self.animal_name}は{self.animal_cry}と吠える"
        print(ret_str)
        return ret_str

    def age_conversion(self) -> str:
        """
        年の説明

        人間の年齢に換算した際に、犬が何歳であるかを表示する
        """
        tmp_age = my_round(16 * math.log(self.old) + 31)
        ret_str = f"{self.name}は人間の年齢に換算すると{tmp_age}歳になります"
        print(ret_str)
        return ret_str


class Cat(Animal):

    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old
        self.animal_name = "猫"
        self.animal_cry = "ニャアニャア"

    def cry(self) -> str:
        """
        鳴き声の説明

        猫がどのように鳴くかを表示する
        """
        ret_str = f"{self.animal_name}は{self.animal_cry}と吠える"
        print(ret_str)
        return ret_str

    def age_conversion(self) -> str:
        """
        年の説明

        人間の年齢に換算した際に、猫が何歳であるかを表示する
        """

        tmp_age = 20
        if self.old >= 2:
            tmp_age += 4 * (self.old - 2)

        ret_str = f"{self.name}は人間の年齢に換算すると{tmp_age}歳になります"
        print(ret_str)
        return ret_str


class Human(Animal):
    """
    人間クラス
    """

    def __init__(self, name: str, old: int):
        self.name = name
        self.old = old
        self.animal_name = "人間"
        self.animal_cry = ""

    def cry(self) -> str:
        """
        鳴き声の説明

        人間がどのように鳴くかを表示する
        """
        ret_str = f"{self.animal_name}は鳴き声を上げない"
        print(ret_str)
        return ret_str

    def age_conversion(self) -> str:
        """
        年の説明

        年齢を表示する
        """
        ret_str = f"{self.name}は{self.old}歳です"
        print(ret_str)
        return ret_str

    @staticmethod
    def print_test(param1, param2):
        """
        関数の説明タイトル

        関数についての説明文

        Args:
            param1 (引数の型): 引数の説明
            param2 (:obj:`引数の型`, optional): 引数の説明.

        Returns:
            戻り値の型: 戻り値の説明 (例 : True なら成功, False なら失敗.)

        Raises:
            例外の名前: 例外の説明 (例 : 引数が指定されていない場合に発生 )

        Yields:
            戻り値の型: 戻り値についての説明

        Examples:
            利用例：print_test("test", "message")

        Note:
            注意事項などを記載

        """

        print("%s %s" % (param1, param2))
