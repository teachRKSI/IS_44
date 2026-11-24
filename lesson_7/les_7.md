# Практическое занятие №11. слоты и сигналы

В начале стоит обозначить, что такое сигналы и слоты. С ними мы уже успели познакомиться ранее, но теперь погрузимся в них. На самом деле всё проще, чем кажется: **сигнал** — это механизм оповещения о том, что произошло событие, **слот** — это функция или метод, который вызывается в ответ на этот сигнал. Ранее мы создавали кнопку которая оповещала о своем нажатии. Давайте разберём её снова:

```python
import sys
from PySide6.QtWidgets import QApplication, QPushButton

def on_button_click():
    print("Кнопка нажата!")

app = QApplication(sys.argv)
button = QPushButton("Нажми меня")
button.clicked.connect(on_button_click)
button.show()
sys.exit(app.exec())
```

У нас есть кнопка `button`. У неё есть сигнал `clicked`, который испускается при нажатии на кнопку. Строкой `button.clicked.connect(on_button_click)` мы подписываем функцию `on_button_click` на этот сигнал — и она будет вызываться при каждом нажатии.

### Пользовательские сигналы

Первое, что стоит отметить: сигналы всегда объявляются на уровне класса — PySide6 регистрирует их в мета-объектной системе Qt при создании класса, и только так работают connect и emit. Разберём простой пример:


```python
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget

class Button(QWidget):

    clicked = Signal(Qt.MouseButton)

    ...

    def mousePressEvent(self, event):
        self.clicked.emit(event.button())
```

В этом примере мы создаём свой сигнал `clicked` и указываем, что при испускании он будет передавать один аргумент типа `Qt.MouseButton` — информацию о том, какая кнопка мыши была нажата. Далее мы переопределяем обработчик `mousePressEvent` (Qt вызывает его при нажатии мыши на виджете) и внутри него испускаем сигнал `clicked` через `emit`, передавая `event.button()` (он вернет значение типа `Qt.MouseButton`, соответствующее нажатой кнопке).


### `@Slot` — зачем декоратор

```python
from PySide6.QtCore import Slot

@Slot(str)
def on_done(self, text):
    self.label.setText(text)
```

Декоратор явно помечает метод как слот и помогает Qt правильно сопоставить типы при подключении. Рекомендуется помечать `@Slot` все методы, используемые в связях сигнал-слот: без этого **PySide6** добавляет метод в `QMetaObject` при создании соединения, что даёт накладные расходы во время выполнения. Особенно это важно для классов `QObject`, зарегистрированных в QML, где отсутствие декоратора может приводить к багам.
Коротко: используйте @Slot для каждого подключаемого метода :)

---

## `setStyleSheet`

`setStyleSheet` — это стилизация виджетов через CSS-подобный синтаксис (QSS). Работает для большинства стандартных виджетов: кнопок, полей ввода, меток, таблиц целиком.

Для одного виджета:

```python
button.setStyleSheet("background-color: #0078d4; color: white;")
```
Для всего приложения:

```python
app.setStyleSheet("""
    QPushButton {
        background-color: #e7ecf8;
        color: #1f2d4d;
    }
    QPushButton:hover {
        background-color: #d2ddf6;
    }
""")
```
Если ввы знакомы с css, то вам будет проще настраивать стили в своем приложение, только помните, не все что есть в css, есть в QSS.

# `QTableWidget` – виджет таблицы

Думаю

```python
import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout


class ColorTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTableWidget: цвета")
        self.resize(500, 300)

        colors = [("Red", "#FF0000"),
                  ("Green", "#00FF00"),
                  ("Blue", "#0000FF"),
                  ("Black", "#000000"),
                  ("White", "#FFFFFF"),
                  ("Electric Green", "#41CD52"),
                  ("Dark Blue", "#222840"),
                  ("Yellow", "#F9E56d")]

        table = QTableWidget()
        table.setRowCount(len(colors))
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])

        for i, (name, code) in enumerate(colors):
            item_name = QTableWidgetItem(name)
            item_code = QTableWidgetItem(code)

            item_color = QTableWidgetItem()
            item_color.setBackground(QColor(code))

            table.setItem(i, 0, item_name)
            table.setItem(i, 1, item_code)
            table.setItem(i, 2, item_color)

        layout = QVBoxLayout(self)
        layout.addWidget(table)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ColorTable()
    window.show()
    sys.exit(app.exec())
```

Давайте разберем этот код.
В учатске ниже вы можете увидеть, что сначала мы создаем объект таблицы, а потом задаем колличество строк и стобцов в ней.

```python
        table = QTableWidget()
        table.setRowCount(len(colors))
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Name", "Hex Code", "Color"])
```

Дальше важно подсветить строки, где мы создаем конкретную ячейку, обратите внимание, мы создаем ячейку с текстом, а потом уже распиывваем всю строку.
setItem(row, col, item) кладёт готовый объект в ячейку (нужно лишь передать "координаты" и сам объект). Также объект может быть и пустым (как для ячеек цвета)

```python
        item_name = QTableWidgetItem(name)   # ячейка с текстом
        table.setItem(i, 0, item_name)
```
В коде ниже мы не используем `setStyleSheet`, потому что он стилизует таблицу целиком как виджет, а не отдельную ячейку. Чтобы покрасить конкретную ячейку, у `QTableWidgetItem` есть метод `setBackground` (а для цвета текста — `setForeground`).

```python
        item_color.setBackground(QColor(code))
```

# Задания

---

## Задание 1. «Счётчик нажатий»

Создайте класс `CounterWidget(QWidget)`: метка и кнопка «Нажать». При нажатии кнопки обработчик **не обновляет метку напрямую**, а только увеличивает счётчик и испускает собственный сигнал `countChanged = Signal(int)` с новым значением. Отдельный слот, подписанный на этот сигнал, обновляет текст метки (`Нажатий: N`).

---

## Задание 2. «Кнопка мыши»

Создайте класс `MouseReporter(QWidget)`: метка с текстом «Нажмите кнопку мыши в окне». Объявите сигнал `mouseButtonPressed = Signal(Qt.MouseButton)` (как в лекции) и переопределите `mousePressEvent(self, event)`, чтобы он испускал этот сигнал с `event.button()`. Отдельный слот, подписанный на сигнал, выводит в метку «Левая кнопка», «Правая кнопка» или «Другая кнопка» в зависимости от нажатой кнопки.

---

## Задание 3. «Стилизация кнопок»

Создайте класс `StyledButtons(QWidget)` с тремя кнопками в `QVBoxLayout` («Одна», «Две», «Три»). В блоке `if __name__ == "__main__":` примените стиль ко всему приложению через `app.setStyleSheet(...)`:

```css
QPushButton { background-color: #e7ecf8; color: #1f2d4d; }
QPushButton:hover { background-color: #d2ddf6; }
```

Одной из кнопок задайте **индивидуальный** стиль через `button.setStyleSheet("background-color: #ffcccc;")` и убедитесь, что он перекрывает стиль приложения.

---

## Задание 4. «Таблица цветов»

Создайте класс `ColorTable(QWidget)` на основе примера из лекции, но с **четырьмя** столбцами: `Name`, `Hex Code`, `Color`, `Комментарий`. Заполните таблицу восемью строками (список цветов из лекции), ячейку `Color` окрашивайте через `item.setBackground(QColor(code))`, в «Комментарий» запишите произвольный текст для каждой строки. Размер окна — `self.resize(600, 320)`.

---

## Задание 5. «Форма + таблица»

Создайте класс `MainWindow(QMainWindow)`. Центральный виджет — `QWidget` (через `setCentralWidget`). Сверху — `QFormLayout` с полями «Имя:» и «Город:» (`QLineEdit`) и кнопкой «Добавить». Снизу — `QTableWidget` с колонками `Имя`, `Город`, рассчитанная на 5 строк (`setRowCount(5)`). При нажатии «Добавить» данные из формы записываются в первую свободную строку через `setItem` (счётчик заполненных строк храните в атрибуте `self.filled_rows`); если все 5 строк заполнены — ничего не происходит. Примените QSS к кнопке (`:hover`) и полям ввода.

---
