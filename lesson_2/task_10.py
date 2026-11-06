import math
from random import randint


# 10.3
def main() -> None:
    """Выполняет задания по использованию модулей."""

    # 10.1
    print("Корень из 144:", math.sqrt(144))
    print("Число pi:", math.pi)

    # 10.2
    print("Случайное число от 1 до 100:", randint(1, 100))


if __name__ == "__main__":
    main()