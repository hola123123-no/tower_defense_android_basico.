[app]

title = Tower Defense Avanzado
package.name = towerdefense
package.domain = org.example

source.dir = .
source.include_exts = py,json

version = 1.0

requirements = python3,pygame

orientation = portrait
fullscreen = 0

p4a.bootstrap = sdl2

android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

log_level = 2
warn_on_root = 1
