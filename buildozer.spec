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
source.dir = .
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
android.min_api = 21
android.api = 33
android.build_tools_version=33.0.0
[buildozer]

# Сатҳи гузоришдиҳӣ
log_level = 2

# Истифодаи ҳолати вижаи зеркашӣ
android.accept_sdk_license = True
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r28c
