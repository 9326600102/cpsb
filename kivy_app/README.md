# 安卓车牌识别App

一个基于Kivy和OpenCV的安卓手机车牌识别应用，可以调用手机摄像头采集画面并实时识别车牌。

## 功能特点

- 调用手机摄像头实时预览
- 拍照识别车牌
- 在图像上标记检测到的车牌区域
- 显示识别的车牌号码
- 支持重新开始功能

## 技术栈

- **Kivy** - 跨平台移动应用开发框架
- **OpenCV** - 计算机视觉库，用于图像处理和车牌检测
- **Tesseract OCR** - 光学字符识别引擎，用于识别车牌文字
- **NumPy** - 数值计算库，用于图像处理

## 项目结构

```
.
├── main.py                    # Kivy应用主文件
├── license_plate_detector.py  # 车牌识别核心功能
├── buildozer.spec             # Android打包配置文件
├── test_detection.py          # 桌面测试脚本
└── README.md                  # 项目说明
```

## 安装和使用

### 方法一：使用Buildozer在Linux上打包（推荐）

Buildozer是Kivy官方推荐的打包工具，可以自动处理所有依赖和配置。

#### 1. 准备Linux环境

建议使用Ubuntu 18.04或更高版本。

#### 2. 安装Buildozer

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtiff5-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk libharfbuzz-dev libfribidi-dev libxcb1-dev
sudo pip3 install --upgrade pip setuptools virtualenv
sudo pip3 install buildozer
```

#### 3. 打包应用

```bash
# 进入项目目录
cd /path/to/kivy_app

# 初始化Buildozer（如果还没有buildozer.spec文件）
buildozer init

# 构建APK
buildozer -v android debug
```

构建完成后，APK文件将位于`bin/`目录下。

#### 4. 安装到手机

将生成的APK文件复制到手机上，然后点击安装。

### 方法二：使用Python for Android

如果Buildozer安装有问题，可以尝试使用Python for Android直接构建。

## 使用说明

1. 打开应用，应用将自动启动摄像头
2. 将车牌对准摄像头，确保车牌清晰可见
3. 点击"拍照识别"按钮
4. 应用将自动检测并识别车牌
5. 识别结果将显示在屏幕上
6. 点击"重新开始"可以再次拍照识别

## 配置说明

### 权限配置

应用需要以下权限：
- CAMERA - 访问摄像头
- WRITE_EXTERNAL_STORAGE - 保存图像
- READ_EXTERNAL_STORAGE - 读取图像

这些权限已经在`buildozer.spec`文件中配置好了。

### Tesseract OCR配置

在安卓设备上，Tesseract OCR需要额外的语言数据文件。Buildozer会自动处理这些依赖，但如果遇到问题，可以手动添加tessdata文件到应用中。

## 性能优化

- 降低摄像头分辨率可以提高处理速度
- 调整图像预处理参数可以提高识别准确率
- 在光线充足的环境下使用可以获得更好的识别效果

## 限制

- 目前只支持英文和数字的车牌识别
- 识别准确率受图像质量影响较大
- 在低端设备上可能会有性能问题

## 开发和测试

### 在桌面环境测试

1. 安装依赖：

```bash
pip install kivy opencv-python numpy pytesseract pillow
```

2. 运行应用：

```bash
python main.py
```

3. 使用测试脚本：

```bash
# 将测试图像命名为test_car.jpg并放在当前目录下
python test_detection.py
```

## 故障排除

### 应用无法启动

- 检查是否已经授予摄像头权限
- 确保手机运行的是Android 5.0（API 21）或更高版本

### 无法检测到车牌

- 确保车牌清晰可见，没有被遮挡
- 尝试调整光线条件
- 确保车牌在画面中央

### OCR识别错误

- 确保Tesseract OCR已正确安装
- 尝试提高图像质量
- 调整图像预处理参数

## 未来改进

- 添加实时视频流识别功能
- 支持更多语言的车牌识别
- 优化在低端设备上的性能
- 添加车牌数据库功能
- 支持车牌历史记录查询