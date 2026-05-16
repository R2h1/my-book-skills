# My Book Skills

书籍知识蒸馏为 Claude Code 可执行技能（Skill）的集合仓库。

## 概览

每本书通过 [RIA-TV++ 管道](https://github.com/R2h/cangjie-skill) 蒸馏为一组结构化技能文件，可直接在 Claude Code 中使用。

| 书籍 | 技能数 | 状态 |
|------|--------|------|
| [30岁人生开挂7步法](./30岁人生开挂7步法/) | 16 | ✅ 已完成 |

## 使用方式

将书目录放入 Claude Code 的 `skills` 目录：

```bash
# 复制到用户级 skills 目录（推荐）
cp -r <书目录> ~/.claude/skills/

# 或复制到项目级 .claude/skills/
cp -r <书目录> <项目路径>/.claude/skills/
```

之后在 Claude Code 中可通过 `/技能名` 调用对应技能。

## 目录结构

```
📂 书目录/
├── 📂 v01-技能一/       # 每个技能独立目录
│   └── SKILL.md        # RIA++ 格式的技能定义
├── 📂 v02-技能二/
│   └── SKILL.md
├── ...
├── INDEX.md            # 技能关系网络索引
├── test-prompts.json   # 触发测试用例
├── BOOK_OVERVIEW.md    # 书籍概览
└── verified.md         # 三重复核记录
```

## 格式说明

每个 `SKILL.md` 遵循 RIA++ 模板：
- **R**（Reading）：核心引文
- **I**（Interpretation）：底层原理
- **A1**（Past Application）：过去应用案例
- **A2**（Future Triggers）：未来触发场景
- **E**（Execution Steps）：可执行步骤
- **B**（Boundary）：边界与局限

## 许可证

MIT
