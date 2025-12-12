# 创建GitHub仓库并推送代码指南

## 1. 退出当前的"导入仓库"页面

您当前看到的是GitHub的"导入仓库"页面，这不是我们需要的。请点击左上角的GitHub标志返回首页。

## 2. 创建全新的GitHub仓库

1. 点击GitHub右上角的"+"图标
2. 选择"New repository"
3. 在创建仓库页面填写以下信息：
   - **Repository name**: 给您的仓库起个名字（例如：kivy-license-plate-app）
   - **Description**: 可选，添加仓库描述
   - **Public/Private**: 选择仓库可见性
   - **Important**: **不要**勾选以下任何选项：
     - ✅ Initialize this repository with a README
     - ✅ Add a .gitignore file
     - ✅ Choose a license
   - 保持这些选项未勾选，确保仓库是空的
4. 点击"Create repository"

## 3. 获取仓库URL

创建仓库后，您会看到一个页面，显示仓库的URL。URL格式类似于：
```
https://github.com/您的GitHub用户名/仓库名称.git
```

请复制这个URL，我们需要使用它来关联本地仓库。

## 4. 关联本地仓库与远程仓库

在您的终端中，运行以下命令（替换为您的仓库URL）：

```bash
git remote add origin https://github.com/您的GitHub用户名/仓库名称.git
```

## 5. 推送代码到GitHub

运行以下命令将代码推送到GitHub：

```bash
git push -u origin master
```

如果您的GitHub仓库默认分支是`main`而不是`master`，请使用：

```bash
git push -u origin main
```

## 6. 输入GitHub认证信息

当您运行`git push`命令时，会弹出一个窗口或在终端中提示您输入GitHub认证信息。

### 使用个人访问令牌（推荐）

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

## 7. 验证推送是否成功

推送成功后，您可以在GitHub仓库页面看到您的代码。

## 8. 下一步

代码推送成功后，您可以在GitHub仓库的"Actions"选项卡中手动触发APK构建流程，或等待自动构建完成。

详细的GitHub Actions使用说明，请参考[GITHUB_ACTIONS_GUIDE.md](GITHUB_ACTIONS_GUIDE.md)文件。