"""
3. ЗАДАНИЕ НА ЗАКРЕПЛЕНИЕ ЗНАНИЙ ПО МОДУЛЮ YAML.
 НАПИСАТЬ СКРИПТ, АВТОМАТИЗИРУЮЩИЙ СОХРАНЕНИЕ ДАННЫХ
 В ФАЙЛЕ YAML-ФОРМАТА.
ДЛЯ ЭТОГО:

ПОДГОТОВИТЬ ДАННЫЕ ДЛЯ ЗАПИСИ В ВИДЕ СЛОВАРЯ, В КОТОРОМ
ПЕРВОМУ КЛЮЧУ СООТВЕТСТВУЕТ СПИСОК, ВТОРОМУ — ЦЕЛОЕ ЧИСЛО,
ТРЕТЬЕМУ — ВЛОЖЕННЫЙ СЛОВАРЬ, ГДЕ ЗНАЧЕНИЕ КАЖДОГО КЛЮЧА —
ЭТО ЦЕЛОЕ ЧИСЛО С ЮНИКОД-СИМВОЛОМ, ОТСУТСТВУЮЩИМ В КОДИРОВКЕ
ASCII(НАПРИМЕР, €);

РЕАЛИЗОВАТЬ СОХРАНЕНИЕ ДАННЫХ В ФАЙЛ ФОРМАТА YAML — НАПРИМЕР,
В ФАЙЛ FILE.YAML. ПРИ ЭТОМ ОБЕСПЕЧИТЬ СТИЛИЗАЦИЮ ФАЙЛА С ПОМОЩЬЮ
ПАРАМЕТРА DEFAULT_FLOW_STYLE, А ТАКЖЕ УСТАНОВИТЬ ВОЗМОЖНОСТЬ РАБОТЫ
С ЮНИКОДОМ: ALLOW_UNICODE = TRUE;

РЕАЛИЗОВАТЬ СЧИТЫВАНИЕ ДАННЫХ ИЗ СОЗДАННОГО ФАЙЛА И ПРОВЕРИТЬ,
СОВПАДАЮТ ЛИ ОНИ С ИСХОДНЫМИ.
"""
import yaml

DATA = {
    'items': ['computer', 'printer', 'keyboard', 'mouse'],
    'items_quantity': 4,
    'items_price': {
        'computer': '200€-1000€',
        'keyboard': '5€-50€',
        'mouse': '4€-7€',
        'printer': '100€-300€'
    },
}

with open('my_file.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(DATA, f, default_flow_style=False, allow_unicode=True)

with open('my_file.yaml', encoding='utf-8') as f:
    yaml_content = yaml.safe_load(f)

print(yaml_content == DATA)
