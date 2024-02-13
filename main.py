from Src.settings_manager import settings_manager

manager = settings_manager()
manager.open('settings.json')
print(manager)
print(manager.settings)