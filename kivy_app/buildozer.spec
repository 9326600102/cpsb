[app]

# (str) Title of your application
title = License Plate Recognition

# (str) Package name
package.name = licenseplaterecognition

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = venv,test,__pycache__

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,data/audio/*.wav

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.1.0,opencv-python-headless,numpy,pytesseract,pillow

# (str) Supported orientation (one of landscape, portrait or all)
orientation = all

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
android.apptheme = android:style/Theme.NoTitleBar

#
# Buildozer storage directory
#
# (str) Directory path to buildozer artifacts
# This directory is used to store all the buildozer generated files
# (like the build environment, the generated packages, etc.)
build_dir = ./.buildozer

# (bool) If true, then verbose output from buildozer will be shown
verbose = 2

# (bool) If true, then buildozer will use color into the output
color = 1