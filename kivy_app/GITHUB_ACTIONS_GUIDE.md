# 使用 GitHub Actions 打包 APK 指南

由于在本地配置 WSL 环境可能遇到各种问题，GitHub Actions 提供了一个更简单、更可靠的方式来打包您的 Android APK。

## 步骤 1：准备工作

1. 确保您的项目已经上传到 GitHub 仓库
2. 检查项目根目录是否存在 `buildozer.spec` 文件（我们已经为您创建）
3. 确保 `.github/workflows/build-apk.yml` 文件存在（我们已经为您创建）

## 步骤 2：触发构建流程

有两种方式可以触发构建流程：

### 方法 A：推送代码到 GitHub

1. 将项目代码推送到 GitHub 仓库的 `main` 分支
2. GitHub Actions 会自动开始构建流程

### 方法 B：手动触发构建

1. 登录到您的 GitHub 账号
2. 打开您的项目仓库
3. 点击顶部导航栏的 "Actions" 选项卡
4. 在左侧列表中选择 "Build Android APK"
5. 点击 "Run workflow" 按钮
6. 选择分支（通常是 `main`）
7. 点击 "Run workflow" 开始构建

## 步骤 3：下载构建好的 APK

1. 构建完成后，在 "Actions" 页面点击对应的构建记录
2. 向下滚动到 "Artifacts" 部分
3. 点击 "license-plate-recognition-apk" 下载 APK 文件

## 注意事项

- 首次构建可能需要较长时间（15-30分钟），因为需要下载和配置所有依赖
- 确保 `buildozer.spec` 文件中的配置正确
- 如果构建失败，可以查看构建日志以了解具体错误

## 常见问题

### 构建失败怎么办？

1. 查看构建日志，找到错误信息
2. 根据错误信息修复问题
3. 重新触发构建流程

### APK 文件在哪里？

构建完成后，APK 文件会作为 Artifact 上传到 GitHub，可以在构建记录的 "Artifacts" 部分下载。

### 构建需要多长时间？

首次构建通常需要 15-30 分钟，后续构建会快一些，因为部分依赖会被缓存。

## 替代方案

如果 GitHub Actions 也不适合您，您还可以：

1. 使用 Docker 容器进行打包（详见 BUILDING_APK_GUIDE.md）
2. 使用在线服务如 Buildozer Online
3. 在 Linux 系统上直接安装 Buildozer（推荐使用 Ubuntu 20.04 或 22.04）
