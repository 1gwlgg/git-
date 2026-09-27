# Git 协同开发实验项目

本项目用于练习基于 Issue 的任务管理、基于分支的版本管理与基于 PR 的分布式协同开发。

## 环境
- 版本管理工具：Git
- 远程仓库：GitHub
- 协作方式：Issue + Feature Branch + Pull Request

## 目录结构
- `main.py`：主程序入口
- `utils.py`：工具函数模块

## 运行方式
```bash
python main.py
```

预期输出：
```
Hello, World!
[debug] add(1, 2) = 3
1 + 2 = 3
[debug] add(0.1, 0.2) = 0.30000000000000004
0.1 + 0.2 = 0.30000000000000004
```

## 协作流程
1. 在 Issue 中描述任务并指派给开发人员；
2. 基于 `master` 创建特性分支（如 `fix-1`、`docs/xxx`）；
3. 在特性分支上开发、提交并推送；
4. 发起 Pull Request，关联 Issue（`Closes #1`）；
5. Code Review 合并后删除特性分支。
