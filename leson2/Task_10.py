# Тема 10. Импорт модулей и __main__

# 10.1
import math

print("Корень из 144:", math.sqrt(144))
print("Число pi:", math.pi)

# 10.2
from random import randint

print("Случайное число от 1 до 100:", randint(1, 100))

# 10.3
def main() -> None:
    """Запускает основную часть программы."""
    print("Программа запущена")

if __name__ == "__main__":
    main()
