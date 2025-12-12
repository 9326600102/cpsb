@echo off
echo 重启后自动启动WSL并配置环境
echo =============================
wsl -d Ubuntu -e bash /mnt/c/Users/86183/Documents/trae_projects/app/kivy_app/wsl_configure.sh
pause