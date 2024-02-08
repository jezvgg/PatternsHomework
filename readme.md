### settings
Класс хранящие в себе поля для настроек. 

### settings_manager
Класс для управления json файлом settings.
А так же он управляет классом settings.py, который хранит в себе все поля settings.json.

Пример:
```
manager = settings_manager()

manager.open("settings.json")
sets = manager.settings
```
sets - объект типа Settings со всеми настройками