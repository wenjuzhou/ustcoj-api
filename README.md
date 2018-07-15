# USTCOJ-api

**THIS IS A PRIVATE REPO**

## 开发流程

请不要直接提交代码到 master 分支，根据提交的不同将代码提交到以下分支：

- `develop`: 基于 `master` 的分支，完成检查后合并回 `master`；
- `feature/<name>`: 基于 `develop` 的分支，增加新特性，完成后以一个 `commit` 合并回 `develop`；
- `hotfix`: 基于 `master` 的分支，需要快速部署到线上的分支， 完成后需要同时合并到 `master` 和 `develop`；

一般的开发流程：

开发新的特性：

- 基于 `develop` 分支出 `feature/<name>``；
- 完成 `feature/<name>` 的开发；
- 将 `feature/<name>` 压缩为一个提交后合并回 `develop` 分支；

开发完多个特性后，上线：

- 将 `develop` 合并回 `master` 分支；

紧急修复线上：

- 基于 `master` 分支出 `hotfix`；
- 完成 `hotfix` 的开发；
- 将 `hotfix` 压缩为一个提交后合并到 `master` 和 `develop` 分支；

## Deploy

任何到 `master` 分支的提交都会触发自动部署（见：`deploy.sh`），特别的，如果修改了 `requirements.txt` 将会触发一次新的 docker 构建（见：`build.sh`）。

服务器地址位于：http://210.45.122.58:8000/


