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

# (str) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.1.0,opencv-python,numpy,pytesseract,pillow

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
#requirements.source.kivy = ../../kivy

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

# (list) Android additional libraries to copy into libs/armeabi
#android.add_libs_armeabi = libs/android/*.so

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Use AndroidX support library
android.use_androidx = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path = 

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path = 

# (bool) If True, then skip trying to update the Android SDK
# This can be useful to avoid excess Internet downloads or save time
#android.skip_update = False

# (bool) If True, then automatically accept SDK license
sdk.accept_license = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
#android.whitelist = 

# (str) Path to a custom whitelist file
#android.whitelist_src = 

# (str) Path to a custom main.java file
#android.mainjava_src = 

# (str) Path to a custom AndroidManifest.xml file
#android.manifest_src = 

# (str) Path to a custom build.xml file
#android.build_src = 

# (str) Path to a custom styles.xml file
#android.styles_src = 

# (list) List of Java .jar files to add to the libs folder
#android.add_jars = foo.jar,bar.jar,path/to/baz.jar

# (list) List of Java files to add to the android project (can be java or a directory containing the files)
#android.add_src = 

# (list) Android AAR archives to add
#android.add_aars = 

# (list) Gradle dependencies to add
#android.gradle_dependencies = 

# (bool) Enable AndroidX support
#android.use_androidx = True

# (list) rules to exclude various files
#android.add_excludes = assets/*.mp3

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android API to use
#android.api = 33

# (str) Minimum API required
#android.minapi = 21

# (str) Android SDK version to use
#android.sdk = 33

# (str) Android NDK version to use
#android.ndk = 25.1.8937393

# (int) Android NDK API to use
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (bool) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a,armeabi-v7a

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
