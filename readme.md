### settings_manager
Класс для управления json файлом settings.
А так же он управляет классом settings.py, который хранит в себе все поля settings.json.

Пример:
```
item = settings_manager()

result = item.open("settings.json")

iten.data
```
Вернёт все нужные поля из json.

### settings
Класс хранящие в себе поля для настроек. 