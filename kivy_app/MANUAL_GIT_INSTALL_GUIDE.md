# 手动下载和安装Git指南

由于网络连接问题，我们无法通过命令行自动下载Git。请按照以下步骤手动下载和安装Git：

## 步骤1：下载Git安装程序

1. 打开您的浏览器
2. 访问Git官网的下载页面：[https://git-scm.com/download/win](https://git-scm.com/download/win)
3. 网站会自动检测您的系统类型（Windows 64位）
4. 下载应该会自动开始，如果没有，请点击页面上的下载链接

## 步骤2：安装Git

1. 找到下载的安装程序文件（通常在"Downloads"文件夹中，文件名类似"Git-2.xx.x-64-bit.exe"）
2. 双击安装程序文件开始安装
3. 按照安装向导的提示进行操作：

### 安装选项建议：

1. **选择安装位置**：使用默认位置即可（通常是`C:\Program Files\Git`）
2. **选择组件**：保持默认选择即可
3. **选择开始菜单文件夹**：使用默认选择
4. **选择编辑器**：建议选择您熟悉的编辑器，如Notepad++或Visual Studio Code
5. **调整PATH环境变量**：选择"Use Git from the Windows Command Prompt"（推荐）
6. **选择HTTPS传输后端**：选择"Use the OpenSSL library"（默认）
7. **配置行尾转换**：选择"Checkout Windows-style, commit Unix-style line endings"（默认）
8. **配置终端模拟器**：选择"Use Windows' default console window"或"Use MinTTY"（推荐）
9. **配置额外选项**：保持默认选择即可
10. **配置实验性功能**：根据您的需要选择，建议暂时不启用

4. 点击"Install"按钮开始安装
5. 安装完成后，点击"Finish"按钮

## 步骤3：验证Git安装

1. 打开命令提示符或PowerShell
2. 输入以下命令检查Git版本：

```bash
git --version
```

3. 如果显示Git版本信息（如`git version 2.xx.x.windows.x`），说明Git安装成功

## 步骤4：配置Git

安装成功后，需要配置Git的用户名和邮箱：

```bash
git config --global user.name "挡泥板"
git config --global user.email "932600102@qq.com"
```

## 下一步

Git安装完成后，您可以继续按照`UPLOAD_TO_GITHUB_GUIDE.md`文件中的步骤将项目上传到GitHub。

如果您在安装过程中遇到任何问题，请随时告诉我！