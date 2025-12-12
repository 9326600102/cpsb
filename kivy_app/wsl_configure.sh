#!/bin/bash

echo "=== WSL配置和APK打包脚本 ==="

echo "1. 更新系统包"
sudo apt update && sudo apt upgrade -y

echo "2. 安装必要的依赖包"
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtiff5-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk libharfbuzz-dev libfribidi-dev libxcb1-dev

echo "3. 升级pip和安装buildozer"
python3 -m pip install --upgrade pip setuptools virtualenv
pip3 install buildozer cython==0.29.32

echo "4. 进入项目目录"
cd /mnt/c/Users/86183/Documents/trae_projects/app/kivy_app

echo "5. 开始构建APK"
buildozer -v android debug

echo "=== 配置完成！==="
echo "如果构建成功，APK文件将位于 bin/ 目录下"
echo "如果遇到问题，请参考 BUILDING_APK_GUIDE.md 文件"