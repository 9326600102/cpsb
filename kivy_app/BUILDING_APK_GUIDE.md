# 安卓APK打包指南

本文提供了多种将Kivy应用打包为安卓APK的方法，您可以根据自己的情况选择最适合的方式。

## 方法一：使用GitHub Actions在线打包（推荐）

这是最简单的方法，不需要在本地安装复杂的环境。

### 步骤：

1. 将项目上传到GitHub仓库

2. 启用GitHub Actions：
   - 打开仓库页面
   - 点击"Actions"标签
   - 点击"I understand my workflows, go ahead and enable them"

3. 触发构建：
   - 可以通过推送代码自动触发
   - 或在Actions页面点击"Build Android APK" -> "Run workflow"

4. 下载APK：
   - 构建完成后，在Actions页面点击对应的构建记录
   - 拉到底部的"Artifacts"部分
   - 点击"license-plate-recognition-apk"下载

## 方法二：使用Docker容器打包

如果您的系统安装了Docker，可以使用预配置的Docker镜像来打包。

### 步骤：

1. 安装Docker：[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

2. 拉取Kivy Docker镜像：
   ```bash
   docker pull kivy/buildozer
   ```

3. 进入项目目录：
   ```bash
   cd /path/to/kivy_app
   ```

4. 运行Docker容器并构建APK：
   ```bash
   docker run --rm -v "$(pwd)":/home/user/hostcwd -w /home/user/hostcwd kivy/buildozer buildozer -v android debug
   ```

5. 构建完成后，APK文件将位于`bin/`目录下。

## 方法三：在Linux系统上安装Buildozer

如果您有Linux系统（或WSL），可以直接安装Buildozer。

### 步骤：

1. 安装依赖：
   ```bash
   sudo apt update
   sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtiff5-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk libharfbuzz-dev libfribidi-dev libxcb1-dev
   ```

2. 安装Buildozer：
   ```bash
   sudo pip3 install --upgrade pip setuptools virtualenv
   sudo pip3 install buildozer
   ```

3. 进入项目目录：
   ```bash
   cd /path/to/kivy_app
   ```

4. 构建APK：
   ```bash
   buildozer -v android debug
   ```

## 方法四：在Windows上使用WSL

如果您想在Windows上使用WSL打包，需要完成以下步骤：

### 步骤：

1. 安装WSL：
   ```powershell
   wsl --install
   ```

2. 重启系统

3. 打开WSL终端

4. 在WSL中按照"方法三"的步骤安装Buildozer并构建APK

## 方法五：使用Python for Android

这是更高级的方法，适用于需要更多定制的情况。

### 步骤：

1. 安装Python for Android：
   ```bash
   pip install python-for-android
   ```

2. 构建APK：
   ```bash
   p4a apk --private /path/to/kivy_app --package=org.example.licenseplaterecognition --name="License Plate Recognition" --version=0.1 --bootstrap=sdl2 --requirements=python3,kivy==2.1.0,opencv-python-headless,numpy,pytesseract,pillow --orientation=all --permission=CAMERA --permission=WRITE_EXTERNAL_STORAGE --permission=READ_EXTERNAL_STORAGE
   ```

## 常见问题及解决方案

### 1. 构建过程中出现内存不足错误

解决方案：
- 增加系统内存或交换空间
- 在Docker中使用`--memory`参数增加内存限制

### 2. Tesseract OCR相关错误

解决方案：
- 确保在buildozer.spec中包含了tesseract相关依赖
- 可以尝试添加`tesseract==4.1.1`到requirements

### 3. OpenCV相关错误

解决方案：
- 使用`opencv-python-headless`而不是`opencv-python`
- 确保NDK和SDK版本与OpenCV兼容

### 4. 权限错误

解决方案：
- 检查buildozer.spec中的权限配置
- 确保包含了所有必要的权限（CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE）

## 调试技巧

1. 查看详细的构建日志：
   ```bash
   buildozer -v android debug > build.log 2>&1
   ```

2. 使用`adb logcat`查看应用运行时的日志：
   ```bash
   adb logcat -s python
   ```

3. 在buildozer.spec中启用调试模式：
   ```ini
   android.debug = True
   ```

## 提示

- 首次构建会下载大量依赖，可能需要较长时间，请耐心等待
- 构建过程中需要稳定的网络连接
- 如果遇到问题，可以尝试清理构建缓存：
  ```bash
  buildozer android clean
  ```

祝您打包顺利！