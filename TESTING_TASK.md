# Домашнее задание

Разработать автоматизированные тесты для компонентов приложения User Management System.

Для тестирования использовать:

- unittest;
- pytest;
- Allure Report;
- Coverage Report.

---

# Структура проекта

```text
user-management/

├── src/
│   ├── user.py
│   └── user_manager.py
│
├── tests/
│   │
│   ├── unittest/
│   │   ├── test_user.py
│   │   └── test_user_manager.py
│   │
│   ├── pytest/
│   │   ├── test_user.py
│   │   └── test_user_manager.py
│   │
│   └── conftest.py
│
├── reports/
│   ├── allure-results/
│   ├── allure-report/
│   └── coverage/
│
├── requirements.txt
├── pytest.ini
├── .coveragerc
└── README.md
```

---

# Тестирование User

Файл:

```text
tests/unittest/test_user.py
tests/pytest/test_user.py
```

---

## is_adult()

Проверить сценарии:

```python
возраст 17 лет

возраст 18 лет

возраст 19 лет
```

---

## to_dict()

Проверить корректность формирования словаря.

---

# Тестирование UserManager

Файл:

```text
tests/unittest/test_user_manager.py
tests/pytest/test_user_manager.py
```

---

## add_user()

Проверить успешное добавление пользователя.

---

## add_user()

Проверить возникновение исключений:

### user_id

```python
неверный тип данных

дублирующийся идентификатор
```

---

### name

```python
пустая строка

строка из одного символа

неверный тип данных
```

---

### age

```python
значение меньше 0

значение больше 120

неверный тип данных
```

---

### email

```python
отсутствует символ "@"

неверный тип данных
```

---

## get_user()

Проверить:

```python
существующий пользователь

отсутствующий пользователь
```

---

## remove_user()

Проверить:

```python
удаление существующего пользователя

удаление отсутствующего пользователя
```

---

## get_all_users()

Проверить:

```python
пустая коллекция

коллекция с пользователями
```

---

## count_users()

Проверить:

```python
пустая коллекция

коллекция с пользователями
```

---

# Требования к unittest

Необходимо использовать:

```python
unittest.TestCase

setUp()

tearDown()
```

Обязательные проверки:

```python
assertEqual()

assertTrue()

assertFalse()

assertIsNone()

assertRaises()
```

---

# Требования к pytest

Необходимо использовать:

```python
fixtures

parametrize
```

---

## Fixtures

Реализовать в conftest.py:

```python
user()

manager()
```

---

## Parametrize

Использовать минимум для следующих сценариев:

```python
проверка совершеннолетия пользователя

проверка некорректного возраста

проверка некорректного email
```

---

# Allure Report

Каждый тест должен содержать:

```python
@allure.feature()

@allure.story()

@allure.title()
```

Для pytest допускается использование:

```python
@allure.feature()

@allure.story()
```

---

# Coverage Report

Создать файл:

```text
.coveragerc
```

С настройками:

```ini
[run]
source = src

[report]
fail_under = 80
show_missing = True
```

Минимальное покрытие проекта:

```text
80%
```

---

# Результат выполнения

В репозитории должны присутствовать:

- тесты на unittest;
- тесты на pytest;
- файл conftest.py;
- настроенный Allure Report;
- настроенный Coverage Report;
- инструкция по запуску тестов.

---