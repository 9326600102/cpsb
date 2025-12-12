# 将项目上传到GitHub仓库的详细指南

本指南将教您如何将本地的Kivy项目上传到GitHub仓库，以便使用GitHub Actions进行APK打包。

## 步骤1：安装Git

如果您的计算机上还没有安装Git，请先安装它：

1. 访问[Git官网](https://git-scm.com/downloads)
2. 下载适合Windows的Git安装程序
3. 运行安装程序，按照默认选项进行安装

安装完成后，打开命令提示符或PowerShell，输入以下命令验证安装：

```bash
git --version
```

## 步骤2：创建GitHub仓库

1. 登录到您的[GitHub账号](https://github.com/)
2. 点击右上角的"+"图标，选择"New repository"
3. 填写仓库信息：
   - **Repository name**：输入仓库名称（例如：license-plate-recognition）
   - **Description**：输入仓库描述（可选）
   - **Visibility**：选择"Public"（公开）或"Private"（私有）
   - **Initialize this repository with**：不要勾选任何选项（保持为空仓库）
4. 点击"Create repository"按钮

创建成功后，您将看到仓库的URL（例如：https://github.com/yourusername/license-plate-recognition.git）

## 步骤3：配置Git

在推送代码之前，需要配置Git的用户名和邮箱：

```bash
git config --global user.name "您的GitHub用户名"
git config --global user.email "您的GitHub邮箱"
```

## 步骤4：初始化本地仓库并推送代码

### 方法A：使用命令行（推荐）

1. 打开PowerShell，导航到项目目录：

```bash
cd c:\Users\86183\Documents\trae_projects\app\kivy_app
```

2. 初始化Git仓库：

```bash
git init
```

3. 添加所有文件到暂存区：

```bash
git add .
```

4. 提交文件：

```bash
git commit -m "Initial commit"
```

5. 添加远程仓库地址：

```bash
git remote add origin https://github.com/yourusername/your-repository-name.git
```

请将`https://github.com/yourusername/your-repository-name.git`替换为您在步骤2中创建的仓库URL。

6. 推送代码到GitHub：

```bash
git push -u origin master
```

如果您的GitHub仓库默认分支是`main`而不是`master`，请使用：

```bash
git push -u origin main
```

### 方法B：使用GitHub Desktop（图形界面）

1. 下载并安装[GitHub Desktop](https://desktop.github.com/)
2. 打开GitHub Desktop，登录您的GitHub账号
3. 点击"File" > "Add Local Repository"
4. 浏览到项目目录`c:\Users\86183\Documents\trae_projects\app\kivy_app`，点击"Add Repository"
5. 在左侧面板中，输入提交信息，点击"Commit to master"
6. 点击顶部菜单栏的"Repository" > "Push origin"

## 步骤5：验证上传

1. 回到GitHub仓库页面
2. 刷新页面，您应该能看到已上传的项目文件

## 常见问题与解决方案

### 问题1：推送时提示输入用户名和密码

**解决方案**：
- 输入您的GitHub用户名
- 输入您的GitHub个人访问令牌（而不是密码）

**如何创建个人访问令牌**：
1. 登录GitHub，点击右上角头像 > "Settings"
2. 点击左侧菜单栏的"Developer settings" > "Personal access tokens" > "Tokens (classic)"
3. 点击"Generate new token" > "Generate new token (classic)"
4. 填写描述，勾选"repo"权限
5. 点击"Generate token"并保存好生成的令牌

### 问题2：推送失败，提示"fatal: refusing to merge unrelated histories"

**解决方案**：

```bash
git pull origin master --allow-unrelated-histories
git push origin master
```

### 问题3：文件太大无法上传

**解决方案**：
- 使用Git LFS（Large File Storage）来管理大型文件
- 或者将大型文件添加到`.gitignore`文件中，不进行版本控制

## 后续步骤

上传成功后，您可以：
1. 在GitHub仓库的"Actions"选项卡中手动触发APK构建流程
2. 或者推送新的代码更改，自动触发构建流程
3. 构建完成后，在"Artifacts"部分下载APK文件

详细的GitHub Actions使用说明请参考`GITHUB_ACTIONS_GUIDE.md`文件。