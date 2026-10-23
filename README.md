# Практическое занятие №8. Повторение ООП 2.0

## 1. `super().__init__()`

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # без этой строки self.name не появится
        self.breed = breed
```

Без `super().__init__(name)` атрибут `name` не создастся, и `d.name` упадёт с `AttributeError`. Родительский инициализатор **не вызывается автоматически** — его надо вызвать руками.

---

## 2. `has-a` vs `is-a`: окно **содержит** кнопку, а не наследуется от неё

В лекции было правило: наследуйся, только если потомок **является** родителем. В PySide6 это правило нарушают чаще всего.

**Антипаттерн (так не надо):**

```python
class MyButton(QPushButton):   # кнопка "является" кнопкой? Да, но зачем?
    def __init__(self):
        super().__init__("Нажми")
```

Наследование от `QPushButton` оправдано, только если вы **действительно расширяете поведение кнопки** (например, делаете кнопку с таймером нажатия). В 90% случаев кнопка — это просто **деталь** окна.

**Правильно (композиция):**

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Нажми")   # окно СОДЕРЖИТ кнопку
        self.label = QLabel("Кликов: 0")     # и метку
        # ... layout ...
```

Здесь `MainWindow` **имеет** (`has-a`) кнопку и метку. Это ровно тот случай, когда нужна композиция, а не наследование.

**Как быстро проверить себя:** произнесите вслух «X **является** Y» и «X **содержит** Y».
- «Окно является кнопкой» — бессмыслица → наследование не нужно.
- «Окно содержит кнопку» — осмысленно → композиция.
---

## 3. Слот — это обычный метод экземпляра

Сигналы и слоты звучат как что-то новое, но с точки зрения ООП слот — это **обычный метод экземпляра**, который вы уже умеете писать.

```python
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0                          # атрибут экземпляра
        self.button = QPushButton("Нажми")
        self.button.clicked.connect(self.on_click)   # ссылка на bound method

    def on_click(self):                         # слот = метод экземпляра
        self.count += 1
```

Важные моменты:

- `self.on_click` — это **bound method**, то есть метод, уже привязанный к конкретному экземпляру. Python сам передаст `self` при вызове. Это прямое продолжение темы «методы экземпляра».
- `self.count` — **атрибут экземпляра**, живёт внутри конкретного окна. Два окна — два независимых счётчика. Это ровно то, что вы показывали на `s1.age = 21` (изменили только у `s1`).
- Слот не обязан быть «магическим» — это обычный метод. Никаких декораторов для базового случая не нужно.

**Мини-проверка:** если создать два экземпляра `MainWindow` и нажать кнопку в первом, изменится ли счётчик во втором? (Ответ: нет, `self.count` у каждого свой.)

---

## 4. `@staticmethod` и `@classmethod`

Этого в основной лекции не было, а в PySide6 встречается (например, `QApplication.instance()`). Достаточно понимать разницу.

```python
class Student:
    university = "МГУ"                 # атрибут класса

    def __init__(self, name):
        self.name = name               # атрибут экземпляра

    def instance_method(self):         # обычный метод: получает self
        return self.name

    @classmethod
    def from_string(cls, s):           # получает класс (cls), а не экземпляр
        name, age = s.split(",")
        return cls(name)               # фабрика: создаёт экземпляр

    @staticmethod
    def is_adult(age):                 # не получает ни self, ни cls
        return age >= 18
```

| Вид метода | Первый аргумент | Когда нужен |
|---|---|---|
| Обычный | `self` | Работа с данными конкретного экземпляра |
| `@classmethod` | `cls` | Фабрики («создай объект из строки»), альтернативные конструкторы |
| `@staticmethod` | нет | Утилита, логически связанная с классом, но не с его данными |

**Что важно:** `@classmethod` — это не «метод класса вместо метода экземпляра». Это метод, который получает **класс**, а не экземпляр. Он часто используется как альтернативный конструктор. В PySide6 `QApplication.instance()` — как раз пример такого подхода: вернуть уже существующий экземпляр приложения.

---

# 5. Магические методы (dunder)

**Куда вставить:** после `@staticmethod`/`@classmethod`, перед сборным примером. **10–12 минут.**

## Идея

Магический метод — это обычный метод с `self`, просто Python вызывает его сам в ответ на синтаксис. `print(s)` — это, по сути, `print(s.__str__())`. Ничего нового, просто соглашение между Python и твоим классом. Ты уже видел `__init__`, `__str__`, `__repr__` — это они.

## `__str__` и `__repr__`

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"«{self.title}» — {self.author}"

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"

b = Book("Война и мир", "Толстой")
print(b)          # «Война и мир» — Толстой
print(repr(b))    # Book(title='Война и мир', author='Толстой')
```

`__repr__` — для разработчика, однозначно. `__str__` — для человека, красиво. Если `__str__` нет, Python возьмёт `__repr__`. Без них в консоли будет `<__main__.Book object at 0x...>` — бесполезно.

## `__eq__` — сравнение

Без `__eq__` два объекта с одинаковыми данными не равны — сравниваются адреса:

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title

print(Book("Война и мир") == Book("Война и мир"))   # True
```

Два момента: `isinstance` защищает от сравнения с посторонним; `return NotImplemented` (не `False`!) говорит «я не умею сравнивать с таким типом», а `False` соврал бы «они точно не равны».

## `__len__` и `__iter__` — объект как коллекция

```python
class Library:
    def __init__(self):
        self._books = []

    def add(self, book):
        self._books.append(book)

    def __len__(self):
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

lib = Library()
lib.add(Book("Война и мир"))
lib.add(Book("Анна Каренина"))

print(len(lib))              # 2
for book in lib:             # __iter__
    print(book)
```

`len(lib)` — это `lib.__len__()`. `for book in lib` — это `lib.__iter__()`. Синтаксис прежний, поведение задаёт твой класс.

## `__add__` — перегрузка операторов

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))   # Vector(4, 6)
```

Один оператор `+` — разное поведение у разных классов. Это полиморфизм операторов из лекции.


| Синтаксис | Метод |
|---|---|
| `Class(...)` | `__init__` |
| `print(obj)`, `str(obj)` | `__str__` |
| `repr(obj)`, консоль | `__repr__` |
| `obj1 == obj2` | `__eq__` |
| `len(obj)` | `__len__` |
| `for x in obj` | `__iter__` |
| `obj[i]` | `__getitem__` |
| `obj1 + obj2` | `__add__` |


## Задания

**Задание 1.** Дан код с ошибкой:

```Python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} издаёт звук"

class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed       # забыли super()

    def info(self):
        return f"{self.name}, порода: {self.breed}"
```

1. Исправьте класс Dog.

2. Создайте d = Dog("Рекс", "Лабрадор") и вызовите d.info() и d.speak(). Убедитесь, что оба работают.

3. Добавьте в Dog метод speak(), который вызывает super().speak() и дописывает " (гав!)". Проверьте результат.

**Задание 2.** Дан класс:

```Python
class Student:
    university = "МГУ"

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

1. Добавьте @staticmethod is_adult(age), возвращающий True, если age >= 18. Вызовите его и через класс (Student.is_adult(20)), и через экземпляр (s.is_adult(20)).

2. Добавьте @classmethod from_string(cls, s), который принимает строку вида "Аня,20", разбивает её по запятой и возвращает cls(name, int(age)). Проверьте:

**Задание 3** Напишите свой класс Library

Book — поля title, author, year, is_read (по умолчанию False). Методы: mark_as_read(), __str__ (красивое описание), __repr__ (для отладки).

Library — содержит список книг (has-a). Методы:

add(book) — добавить книгу;

find_by_author(author) — вернуть список книг автора;

unread() — вернуть список непрочитанных;

__len__ — количество книг.

DigitalLibrary(Library) — наследуется от Library (is-a), добавляет поле format ("pdf", "epub") и переопределяет __str__, вызывая super().__str__() и дописывая формат.


---
