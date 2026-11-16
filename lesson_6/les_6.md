# Практическое занятие №10. Классы в PySide

До этого момента мы создавали окна последовательно, создавали окно `window = QWidget()`, потом добавляли виджеты и подключали сигналы (наши функции). В небольших примерах это работает, но когда мы пишем полноценное приложение, код превращается в кашу

Нашим решением будет наследоваться от класса `QWidget` и работать с его возможнотями уже в классе насследнике.

### `class MyWindow(QWidget)` и `super().__init__()`

```python
import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                               QLabel, QPushButton)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Моё окно")

        self.layout = QVBoxLayout(self)
        self.label = QLabel("Привет")
        self.button = QPushButton("Нажми")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.on_click)

    def on_click(self):
        self.label.setText("Нажато!")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
```

`QWidget` — базовый класс для всех виджетов Qt, и создание собственного виджета делается именно через наследование от него. `super().__init__()` вызывает конструктор родителя — без этой строки окно не инициализируется, и программа упадёт.

Вспомните что такое `super()` и подумайте, чем `super().__init__()`, так важен при наследование.

Главное изменение: теперь все виджеты — это атрибуты объекта (self.label, self.button, self.layout). Функция-обработчик тоже стала методом (self.on_click), и теперь она обращается к виджетам через self, а не через глобальные переменные — всё состояние окна собрано в одном экземпляре класса.

### `QVBoxLayout(self)` — layout сразу привязывается к окну

В предыдущих примерах мы писали:

```python
layout = QVBoxLayout()
window.setLayout(layout)
```

Внутри класса это можно сделать одной строкой:

```python
self.layout = QVBoxLayout(self)
```

Передача `self` в конструктор layout означает: «этот layout принадлежит этому окну». Отдельный `setLayout` больше не нужен.

### `QMainWindow` вместо `QWidget`

`QMainWindow` — это окно с готовыми: меню, панелью инструментов, статус-баром. Но в него нельзя положить свои кнопки и лейблы напрямую. Поэтому Qt требует назначить центральный виджет, это и будет ваш `QWidget`, который займёт середину окна, и уже внутри него вы размещаете layout со всем содержимым. Для этого мы и написали `self.setCentralWidget(central)`.

```python
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)
        layout.addWidget(QLabel("Контент внутри QMainWindow"))
```


### `QFormLayout` — layout для форм

`QVBoxLayout` ставит виджеты стопкой. Но для форм ввода («Имя:», «Возраст:») удобнее `QFormLayout`: он автоматически располагает элементы в две колонки — подпись слева, поле справа.

```python
from PySide6.QtWidgets import QFormLayout, QLineEdit, QWidget

form = QFormLayout()
form.addRow("Имя:", QLineEdit())
form.addRow("Возраст:", QLineEdit())
```

`addRow("Имя:", widget)` создаёт `QLabel` с текстом «Имя:» и ставит его слева от поля ввода . Это избавляет от ручного создания каждой метки.

### Вложенные layout

Layout можно вкладывать друг в друга. Например, горизонтальная строка с кнопками внутри вертикального основного layout:

```python
from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton

button_layout = QHBoxLayout()
button_layout.addWidget(QPushButton("OK"))
button_layout.addWidget(QPushButton("Отмена"))

main_layout = QVBoxLayout()
main_layout.addWidget(QLabel("Выберите действие"))
main_layout.addLayout(button_layout)
```
---

## Задание

### Задание 1.

Перепишите задачу «Счётчик приветствий» из предыдущего занятия в виде класса, наследующего `QWidget`.

- Все виджеты должны быть атрибутами `self` (`self.edit`, `self.button`, `self.label`).
- Счётчик тоже сделайте атрибутом (`self.count = 0`), чтобы не использовать `global`.
- Обработчики («Поздороваться» и «Сбросить») должны быть методами класса.
- В `__init__` создайте layout, добавьте виджеты и подключите сигналы.

### Задание 2.

Создайте приложение «Анкета» на основе `QMainWindow` с использованием `QFormLayout`.

**Выполните следующее:**
- Класс `MainWindow(QMainWindow)`.
- Центральный виджет — `QWidget`, внутри — `QFormLayout`.
- Поля формы: «Имя:» (`QLineEdit`), «Возраст:» (`QLineEdit`), «Город:» (`QLineEdit`).
- Под формой — `QPushButton` с текстом «Показать».
- Ниже — `QLabel` для результата.
- При нажатии на кнопку: если любое из полей пустое — в метке «Заполните все поля».
- Иначе — в метке текст в три строки: «Имя: {имя}», «Возраст: {возраст}», «Город: {город}».
- Для переноса строк в `QLabel` не забудьте `setWordWrap(True)` и символ `\n`.
