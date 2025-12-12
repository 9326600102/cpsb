# GitHub认证与代码推送指南

## 1. 在GitHub上创建仓库

1. 打开GitHub网站：https://github.com
2. 登录您的GitHub账号（如果还没有账号，请先注册）
3. 点击右上角的"+"图标，选择"New repository"
4. 填写仓库信息：
   - Repository name：给您的仓库起个名字（例如：kivy-license-plate-app）
   - Description：可选，添加仓库描述
   - **重要**：不要勾选"Initialize this repository with a README"、"Add a .gitignore file"或"Choose a license"，保持仓库为空
   - 点击"Create repository"

## 2. 获取GitHub仓库URL

创建仓库后，您会看到一个页面，其中包含仓库的URL。URL格式类似于：
```
https://github.com/您的GitHub用户名/仓库名称.git
```

请复制这个URL，我们稍后会用到它。

## 3. 添加远程仓库

在您的终端中，运行以下命令添加远程仓库（替换为您的仓库URL）：

```bash
git remote add origin https://github.com/您的GitHub用户名/仓库名称.git
```

## 4. 推送代码到GitHub

运行以下命令将代码推送到GitHub：

```bash
git push -u origin master
```

如果您的GitHub仓库默认分支是`main`而不是`master`，请使用：

```bash
git push -u origin main
```

## 5. 输入GitHub认证信息

当您运行`git push`命令时，会弹出一个窗口或在终端中提示您输入GitHub认证信息。

### GitHub认证方式

GitHub现在推荐使用**个人访问令牌（Personal Access Token）** 而不是密码进行认证。

#### 方式一：使用个人访问令牌（推荐）

1. 在GitHub上创建个人访问令牌：
   - 点击右上角头像，选择"Settings"
   - 点击左侧菜单的"Developer settings"
   - 点击"Personal access tokens"，然后选择"Tokens (classic)"
   - 点击"Generate new token"，然后选择"Generate new token (classic)"
   - 设置令牌描述（例如：Git命令行认证）
   - 选择过期时间
   - 勾选权限：至少需要勾选"repo"权限
   - 点击"Generate token"
   - 复制生成的令牌（注意：令牌只显示一次，请妥善保存）

2. 当Git提示输入密码时，粘贴您的个人访问令牌作为密码。

#### 方式二：使用GitHub用户名和密码

如果您仍然想使用密码，可以直接输入您的GitHub密码。但请注意，GitHub可能会提示您使用个人访问令牌。

## 6. 验证推送是否成功

推送成功后，您可以在GitHub仓库页面看到您的代码。

## 7. 常见问题

### 问题1：推送时提示"fatal: HttpRequestException encountered"

**解决方案**：这通常是网络问题。请检查您的网络连接，或尝试使用SSH协议而不是HTTPS协议。

### 问题2：提示"Support for password authentication was removed"

**解决方案**：GitHub已经移除了密码认证支持，请使用个人访问令牌（见第5.1节）。

### 问题3：推送时提示"The requested URL returned error: 403"

**解决方案**：这表示您没有权限推送代码到该仓库。请检查：
1. 您的GitHub用户名和密码/令牌是否正确
2. 您是否是该仓库的所有者或有推送权限
3. 仓库URL是否正确

### 问题4：提示"failed to push some refs to..."

**解决方案**：这通常是因为本地仓库与远程仓库不同步。您可以尝试：

```bash
git pull origin master --allow-unrelated-histories
git push -u origin master
```

## 8. 下一步

代码推送成功后，您可以在GitHub仓库的"Actions"选项卡中手动触发APK构建流程，或等待自动构建完成。

详细的GitHub Actions使用说明，请参考[GITHUB_ACTIONS_GUIDE.md](GITHUB_ACTIONS_GUIDE.md)文件。