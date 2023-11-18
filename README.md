# Инструкция

Для начала перейдем в директорию aaa_testing_tools:

```
cd aaa_testing_tools
```

## Задание 1

Запускаем при помощи команды

```
python -m doctest -v -o=ELLIPSIS -o=NORMALIZE_WHITESPACE test1.py
```

Первый тест отрабатывает успешно, а второй тест выдает ошибку, так как нет кодировки для ';'.

## Задание 2

Запускаем при помощи команды

```
python -m pytest test2.py
```
Первые два теста отрабатывают успешно, а третий падает, так как нет кодировки для ';', соответственно decode не распознает.


## Задание 3

Запускаем при помощи команды

```
python -m unittest -v test3.py
```

## Задание 4

Запускаем при помощи команды

```
python -m pytest test4.py
```

## Задание 5

Запускаем при помощи команды

```
python -m pytest -q test5.py --cov=what_is_year_now
```

Чтобы создался отчёт в виде html, нужно запустить команду

```
python -m pytest -q test5.py --cov=what_is_year_now --cov-report=html
```

Примечание: в файле what_is_year_now.py, чтобы в покрытии не учитывался код после 
```
if __name__ == '__main__'
```
 добавила директиву # pragma: no cover
