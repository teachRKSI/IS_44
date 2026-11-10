# Практическое занятие №7. Повторение ООП.

## 1. Класс и Экземпляр (Object)

### Теория

**Класс** — это чертеж, шаблон, описание того, какими будут объекты. Сам по себе класс не занимает память под данные конкретного объекта.

**Экземпляр (объект)** — это конкретная реализация класса, созданная по чертежу. У каждого экземпляра свои данные.

Аналогия: класс — это чертеж автомобиля, экземпляр — конкретная машина с VIN-номером, цветом и пробегом.

### Синтаксис

```python
class Student:          # объявление класса (имя с большой буквы — соглашение)
    pass

student1 = Student()    # создание экземпляра
student2 = Student()    # ещё один экземпляр

print(type(student1))   # <class '__main__.Student'>
print(student1 is student2)  # False — это разные объекты
```

### Что важно подчеркнуть студентам

- Имя класса по PEP 8 — `CamelCase` (`MyClass`, `StudentGroup`).
- Имя переменной-экземпляра — `snake_case` (`my_student`, `group_1`).
- Класс — это тоже объект (экземпляр метакласса `type`). Можно проверить: `type(Student)` вернет `<class 'type'>`.
- Один класс — сколько угодно экземпляров.

---

## 2. Атрибуты и Методы
### 2.1 Атрибуты экземпляра

Уникальны для каждого объекта. Создаются обычно в `__init__` через `self`.

```python
class Student:
    def __init__(self, name, age):
        self.name = name    # атрибут экземпляра
        self.age = age      # атрибут экземпляра

s1 = Student("Аня", 20)
s2 = Student("Борис", 22)

print(s1.name, s1.age)  # Аня 20
print(s2.name, s2.age)  # Борис 22

s1.age = 21             # меняем только у s1
print(s2.age)           # 22 — у s2 не изменилось
```

### 2.2 Атрибуты класса

Общие для всех экземпляров. Определяются прямо в теле класса.

```python
class Student:
    university = "МГУ"          # атрибут класса
    count = 0                   # атрибут класса

    def __init__(self, name):
        self.name = name        # атрибут экземпляра
        Student.count += 1      # обращаемся к атрибуту класса через имя класса

s1 = Student("Аня")
s2 = Student("Борис")

print(Student.university)   # МГУ
print(s1.university)        # МГУ (Python ищет в экземпляре, не находит, идет в класс)
print(Student.count)        # 2
```

### 2.3 Методы экземпляра

Это функции внутри класса. Первый аргумент — всегда `self` (ссылка на конкретный экземпляр).

```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):                          # метод экземпляра
        return sum(self.grades) / len(self.grades)

    def add_grade(self, grade):
        self.grades.append(grade)

s = Student("Аня", [4, 5, 5])
print(s.average())      # 4.666...
s.add_grade(5)
print(s.average())      # 4.75
```

### Что важно подчеркнуть

- `self` — это **не ключевое слово**, а соглашение об имени первого параметра. Технически можно назвать `this`, но так делать не принято.
- Python **автоматически** передает экземпляр первым аргументом при вызове `s.average()`. То есть `s.average()` == `Student.average(s)`.
- Метод без `self` в объявлении вызовется с ошибкой, если вызывать через экземпляр.

```python
class A:
    def method():       # забыли self
        print("hi")

a = A()
a.method()   # TypeError: method() takes 0 positional arguments but 1 was given
```
---

## 3. Магический метод `__init__` (Конструктор)

### Теория

`__init__` — это **инициализатор**, а не конструктор в строгом смысле (за создание объекта отвечает `__new__`). Но в 99% случаев достаточно знать, что `__init__` вызывается автоматически при создании объекта и служит для задания начального состояния.

### Синтаксис

```python
class Student:
    def __init__(self, name, age=18, grades=None):
        self.name = name
        self.age = age
        # ВАЖНО: не использовать изменяемые типы как значения по умолчанию!
        self.grades = grades if grades is not None else []

s1 = Student("Аня", 20, [5, 4, 5])
s2 = Student("Борис")               # age=18, grades=[]
```

### Ключевые моменты

1. **Вызывается автоматически** при `Student(...)`. Явно вызывать `s.__init__()` не нужно.
2. **Не возвращает ничего** (точнее, должен возвращать `None`). Если вернуть что-то другое — `TypeError`.
3. **`self` — это созданный объект**, который передается в `__init__` автоматически.

### Ловушка с изменяемыми значениями по умолчанию

Это одна из самых частых ошибок в Python. Разберем подробно, потому что она напрямую касается `__init__`.

```python
class Student:
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

s1 = Student("Аня")
s2 = Student("Борис")

s1.grades.append(5)
print(s2.grades)   # [5] — ОШИБКА! Список общий для всех экземпляров
```

**Почему так происходит:** значение по умолчанию вычисляется **один раз** при объявлении функции и хранится в `__defaults__`. Все вызовы без аргумента получают **один и тот же** объект списка.

**Правильно:**

```python
class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []
```

### Что важно подчеркнуть

- `__init__` — не единственный магический метод для инициализации, но основной.
- Если `__init__` не определен, Python использует унаследованный (в итоге — `object.__init__`, который ничего не делает).
- Аргументы `__init__` — это то, что вы передаете в скобках при создании объекта.

### Пример для закрепления

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        self.balance -= amount

acc = BankAccount("Аня", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)
```

---

## 4. Магические методы `__str__` и `__repr__`

### Теория

Оба метода возвращают строковое представление объекта, но для разных целей:

| Метод      | Для кого       | Цель                          | Кто вызывает                     |
|------------|----------------|-------------------------------|----------------------------------|
| `__str__`  | Пользователь   | Читаемое описание             | `print()`, `str()`, f-строки     |
| `__repr__` | Разработчик    | Однозначное, отладочное       | `repr()`, консоль, отладчик      |

### Правило

> `__repr__` должен быть таким, чтобы по нему можно было **воссоздать объект** (или хотя бы однозначно его идентифицировать). `__str__` — красивым для человека.

### Мини-задание для проверки

> Создайте класс `Book` с полями `title`, `author`, `year`, `is_read` (по умолчанию `False`). Добавьте метод `mark_as_read()`. Реализуйте `__str__` (красивое описание) и `__repr__` (для отладки). Создайте список из 3 книг и выведите их.

---

# Блок 2. Основные принципы ООП (Три кита)

Тут важно сразу оговорить: в Python эти принципы реализованы мягче, чем в Java или C++. Многое держится на **соглашениях**, а не на строгих запретах компилятора.

---

## 1. Инкапсуляция

### Теория

**Инкапсуляция** — это сокрытие внутренней реализации объекта и предоставление контролируемого доступа к данным.

В классическом ООП (Java, C++) есть ключевые слова `private`, `protected`, `public`. В Python **их нет**. Вместо этого — соглашения об именовании и механизм name mangling.

### Уровни доступа в Python (по соглашению)

| Синтаксис      | Название            | Смысл                                              |
|----------------|---------------------|----------------------------------------------------|
| `name`         | public              | Открыт для всех                                    |
| `_name`        | private (условно) | «Внутреннее, не трогай без необходимости»          |
| `__name`       | protected (условно)   | Name mangling — Python переименует атрибут         |
| `__name__`     | dunder              | Магические методы, не трогать                      |

### 1.1. Public

```python
class Student:
    def __init__(self, name):
        self.name = name    # публичный атрибут

s = Student("Аня")
print(s.name)      # Аня
s.name = "Борис"   # можно менять
```

### 1.2. Private `_name`

Одно подчеркивание — это **сигнал другим разработчикам**: «это внутренняя деталь, не используй снаружи». Python **не запрещает** доступ, просто предупреждает.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance    # защищенный атрибут

acc = BankAccount(1000)
print(acc._balance)   # 1000 — работает, но так делать не принято
```

### 1.3. Protected `__name` (name mangling)

Два подчеркивания включают механизм **name mangling**: Python переименовывает атрибут в `_ClassName__attr`.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance    # приватный атрибут

acc = BankAccount(1000)
# print(acc.__balance)   # AttributeError!
print(acc._BankAccount__balance)   # 1000 — но так делать не надо
```

### Что важно подчеркнуть

- **Инкапсуляция в Python — это соглашение, а не запрет.** Если очень хочется — можно залезть куда угодно.
- Смысл: показать коллегам, что атрибут внутренний, и защитить от случайного переопределения в наследниках (name mangling как раз для этого).
- **Не стоит делать все атрибуты приватными «на всякий случай».** Это не Java. Питоничный подход — открытые атрибуты + `@property`, когда нужен контроль.

### 1.4. Геттеры, сеттеры и `@property`

В Java пишут `getBalance()`, `setBalance()`. В Python так **не делают**. Вместо этого — декоратор `@property`.

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        """Геттер. Вызывается как атрибут, без скобок."""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Сеттер. Срабатывает при присваивании."""
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value

acc = BankAccount(1000)
print(acc.balance)      # 1000 — работает как атрибут, но на самом деле это геттер

acc.balance = 1500      # сработал сеттер
print(acc.balance)      # 1500

acc.balance = -100      # ValueError: Баланс не может быть отрицательным
```

### Зачем это нужно

1. **Валидация при присваивании** — нельзя установить некорректное значение.
2. **Вычисляемые свойства** — значение не хранится, а вычисляется.
3. **Совместимость** — можно начать с публичного атрибута, а потом незаметно заменить его на property, и код клиентов не сломается.

### Пример вычисляемого свойства

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

c = Circle(5)
print(c.area)       # 78.53975 — без скобок!
print(c.diameter)   # 10

# c.area = 100   # AttributeError: can't set attribute (сеттер не определен)
```

---

## 2. Наследование

### Теория

**Наследование** — механизм, позволяющий создать новый класс на основе существующего, унаследовав его атрибуты и методы.

- **Родитель (базовый класс, superclass)** — тот, от кого наследуют.
- **Потомок (дочерний класс, subclass)** — тот, кто наследует.

### 2.1. Базовый синтаксис

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

d = Dog("Рекс")
print(d.name)       # Рекс — унаследован от Animal
print(d.speak())    # Гав! — переопределен в Dog
```

### 2.2. Переопределение методов (Override)

Потомок может заменить реализацию метода родителя.

```python
class Animal:
    def speak(self):
        return "Какой-то звук"

class Dog(Animal):
    def speak(self):
        return "Гав!"
```

### 2.3. `super()` — вызов родительской реализации

Часто нужно не заменить, а **дополнить** поведение родителя.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # вызываем __init__ родителя
        self.breed = breed       # добавляем свое

d = Dog("Рекс", "Лабрадор")
print(d.name, d.breed)   # Рекс Лабрадор
```

### Что важно подчеркнуть

- **Без `super().__init__()` родительский `__init__` не вызовется.** Атрибут `name` не будет создан.
- `super()` без аргументов (Python 3) — правильный способ. `super(Dog, self)` — устаревший синтаксис Python 2.
- `super()` работает не только в `__init__`, но и в любых методах.

```python
class Dog(Animal):
    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound} + Гав!"
```

### 2.4. Множественное наследование

Python разрешает наследоваться от нескольких классов.

```python
class Swimmer:
    def swim(self):
        return "Плыву"

class Flyer:
    def fly(self):
        return "Лечу"

class Duck(Swimmer, Flyer):
    pass

d = Duck()
print(d.swim())   # Плыву
print(d.fly())    # Лечу
```

### Проблема ромбовидного наследования и MRO

Если у класса два родителя, у которых есть общий предок — возникает «ромб». Python решает конфликт через **MRO (Method Resolution Order)** — порядок разрешения методов, вычисляемый по алгоритму **C3-линеаризации**.

```python
class A:
    def who(self):
        return "A"

class B(A):
    def who(self):
        return "B"

class C(A):
    def who(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.who())   # B — потому что B идет раньше C в MRO

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
```

### Что важно подчеркнуть

- MRO читается слева направо: D → B → C → A → object.
- Python ищет метод в первом классе MRO, где он найден.
- Посмотреть порядок можно через `ClassName.__mro__` или `ClassName.mro()`.
- **Множественное наследование — мощный, но опасный инструмент.** В реальном коде лучше использовать миксины (mixin) — небольшие классы, добавляющие одну функциональность.

### 2.5. Проверка наследования

```python
print(isinstance(d, Dog))      # True
print(isinstance(d, Animal))   # True — потомок является экземпляром родителя
print(issubclass(Dog, Animal)) # True
print(issubclass(Animal, Dog)) # False
```

### Что важно подчеркнуть

- **`isinstance` учитывает наследование**, `type(x) == SomeClass` — нет.

```python
d = Dog("Рекс")
print(type(d) == Animal)        # False — тип Dog, а не Animal
print(isinstance(d, Animal))    # True — Dog является Animal
```

- Хорошая практика: использовать `isinstance`, а не сравнение `type()`.

### Когда наследование — плохая идея

Классический пример: класс `Stack` наследуют от `list`. Вроде удобно — все методы списка доступны. Но тогда у стека появляются методы `insert`, `sort`, `reverse`, которые нарушают семантику стека (LIFO).

> **Правило:** наследуйся, только если потомок **является** родителем (отношение «is-a»). Если потомок **имеет в себе** родителя (отношение «has-a») — используй композицию.

---

## 3. Полиморфизм

### Теория

**Полиморфизм** — способность объектов с одинаковым интерфейсом обрабатываться единообразно, при этом каждый объект ведет себя по-своему.

Проще: «один интерфейс — много реализаций».

### 3.1. Классический полиморфизм через наследование

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14159 * self.r ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4), Circle(2)]

for shape in shapes:
    print(shape.area())   # каждый объект считает по-своему
```

**Смысл полиморфизма:** цикл `for` не знает, какой конкретно объект перед ним. Он просто вызывает `area()`. Это делает код расширяемым — добавляем новый класс `Triangle`, и цикл **не меняется**.

### 3.2. Утиная типизация (Duck Typing)

Это **питоничный** подход к полиморфизму. Идея: «Если это выглядит как утка, плавает как утка и крякает как утка — это утка».

Python не проверяет тип объекта. Ему важно только, есть ли у объекта нужный метод.

```python
class Duck:
    def speak(self):
        return "Кря!"

class Dog:
    def speak(self):
        return "Гав!"

class Robot:
    def speak(self):
        return "Beep-boop"

# Никакого общего родителя!
def make_it_speak(obj):
    print(obj.speak())   # Python просто вызывает метод — есть он или нет

make_it_speak(Duck())    # Кря!
make_it_speak(Dog())     # Гав!
make_it_speak(Robot())   # Beep-boop
```

### Что важно подчеркнуть

- В Python **тип объекта проверяется в момент вызова**, а не при передаче.
- Нет `implements`-интерфейсов, как в Java. Если у объекта есть нужный метод — он подходит.
- Если метода нет — `AttributeError` в момент вызова.
- Утиная типизация — это **не отсутствие типов**, а гибкий контракт: «мне не важно, кто ты, мне важно, что ты умеешь».

### 3.3. Полиморфизм операторов (магические методы)

Полиморфизм проявляется и в перегрузке операторов.

```python
print(1 + 2)                 # 3 — сложение чисел
print("a" + "b")             # ab — конкатенация строк
print([1] + [2])             # [1, 2] — объединение списков
```

Все три используют **один и тот же** оператор `+`, но ведут себя по-разному. За это отвечают магические методы `__add__` у каждого класса.

Можно определить свой:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)   # Vector(4, 6)
```

### Задание для проверки

#### Задание 1

### Условие

Создайте класс `Temperature`, который хранит температуру в градусах Цельсия.

Требования:
1. Внутренний атрибут называется `_celsius`.
2. Через `@property` реализовать доступ к `celsius`.
3. В сеттере запретить установку температуры ниже **абсолютного нуля** (−273.15 °C) — бросать `ValueError`.
4. Добавить вычисляемое свойство `fahrenheit` (только геттер) — перевод по формуле `F = C × 9/5 + 32`.

## Задание 2. Наследование и `super()`

### Условие

Есть базовый класс `Vehicle`:

```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        return f"{self.brand}, {self.year} г."
```

Нужно создать два наследника:

1. **`Car`** — добавляет поле `fuel` (тип топлива: `"бензин"`, `"дизель"`, `"электро"`). Метод `info()` возвращает строку родителя плюс тип топлива.
2. **`Motorcycle`** — добавляет поле `engine_volume` (объем двигателя в см³). Метод `info()` возвращает строку родителя плюс объем.

## Задание 3. Полиморфизм и утиная типизация

### Условие

Даны три независимых класса (без общего родителя):

```python
class Dog:
    def sound(self):
        return "Гав"

class Cat:
    def sound(self):
        return "Мяу"

class Cow:
    def sound(self):
        return "Му"
```

Требуется:

1. Написать функцию `chorus(animals)`, которая принимает **список любых объектов** и печатает их звуки в формате: `"<звук>!"`.
2. Создать список из нескольких объектов разных классов и вызвать `chorus`.
3. Добавить четвертый класс `Robot` с методом `sound()`, возвращающим `"Beep"`, и убедиться, что `chorus` работает и с ним **без изменений**.

### Пример использования

```python
animals = [Dog(), Cat(), Cow(), Dog(), Robot()]
chorus(animals)

# Гав!
# Мяу!
# Му!
# Гав!
# Beep!
```
