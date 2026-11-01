import math
from random import randint

# 10.1
print("sqrt(144) =", math.sqrt(144))
print("pi =", math.pi)

# 10.2
print("Случайное 1..100:", randint(1, 100))

# 10.3
def main() -> None:
    """Точка входа программы."""
    print("Программа запущена напрямую")

if __name__ == "__main__":
    main()