# 《金钱的属性：一个富豪的财富私房课》— 流水线状态

> 断点续跑用：每完成一个阶段就更新此文件。

## 当前阶段：全部完成 ✅

## 阶段进度

- [x] 抽取 epub → full_text.txt（119505 字符，89 parts）
- [x] 阶段 0: BOOK_OVERVIEW.md（Adler 四步，用户已确认骨架）
- [x] 阶段 1: candidates/（框架20 / 原则89 / 案例18 / 反例15 / 术语18）
- [x] 阶段 1.5: verified.md（26 个通过）+ rejected/README.md（淘汰 6 类），用户已确认名单
- [x] 阶段 2: 26 个 RIA++ SKILL.md（v01–v26，六段齐全 + V1/V2/V3 审计）
- [x] 阶段 3: INDEX.md（关系图+学习路径）+ GLOSSARY.md（18 术语），related_skills 全部校验无死链
- [x] 阶段 4: 26 × test-prompts.json（合法，各 6 用例：应触发3/诱饵2/边界1，含跨 skill 混淆）+ test-results.md（回退自测）
- [x] 阶段 5: DIGEST.md（精华长文）+ 用户选择"只保留在仓库"（不安装到 Claude）
- [x] README.md / CLAUDE.md 更新（4 本书）

## 交付物清单

| 产物 | 说明 |
|------|------|
| `full_text.txt` / `extract_epub.py` | 全书文本 + 抽取脚本 |
| `BOOK_OVERVIEW.md` | 整书理解（阶段 0） |
| `candidates/` | 原始候选池（审计） |
| `verified.md` | 26 个通过三重验证的单元 |
| `rejected/` | 淘汰单元 + 原因（审计） |
| `v01`–`v26/` | 26 个 skill（各含 SKILL.md + test-prompts.json + test-results.md） |
| `INDEX.md` / `GLOSSARY.md` / `DIGEST.md` | 关系网络 / 术语词典 / 精华长文 |
| `PIPELINE_STATE.md` | 本文件 |

## 待办（可选，用户未选择）

- 安装到 `~/.claude/skills/`（用户选择仅保留仓库）
- 推送到 GitHub（用户选择仅本地提交）
