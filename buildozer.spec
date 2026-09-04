[app]

# Номи барномаи шумо
title = RunamoApp

# Номи баста (package name)
package.name = runamoapp

# Домени баста
package.domain = org.runamo

# Файлҳои шомили барнома
source.include_exts = py,png,jpg,kv,atlas

# Нуқтаи оғози барнома
source.include_dir = .
source.main_file = main.py

# Версияи барнома
version = 0.1

# Китобхонаҳои лозимӣ (Kivy, KivyMD ва дигар вобастагиҳо)
requirements = python3,kivy,kivymd

# Ориентацияи экрани телефон (portrait - амудӣ)
orientation = portrait

# Иҷозатҳо (Permissions) барои телефони андроид
android.permissions = INTERNET

# Версияи ҳадди аққали API
android.min_api = 24

[buildozer]

# Сатҳи гузоришдиҳӣ
log_level = 2

# Истифодаи ҳолати вижаи зеркашӣ
android.accept_sdk_license = True
