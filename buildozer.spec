[app]
title = Yudzz V2
package.name = yudzzv2
package.domain = org.yudzz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,gif
version = 0.1
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
