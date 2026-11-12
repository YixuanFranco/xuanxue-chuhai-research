#!/bin/sh
# Claude Code 会话启动时启用仓库钩子，让 AI 工具的署名行进不了提交说明。
# 不设置 git 身份：署名用谁，由开会话的人自己的配置决定。
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
git config core.hooksPath tools/githooks 2>/dev/null && echo "已启用 tools/githooks（提交说明不留 AI 署名行）"
exit 0
