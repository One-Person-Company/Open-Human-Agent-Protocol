# Contributing to OHAP

[English](#english) | [中文](#中文)

---

## English

### How to Contribute

#### 1. Discussion & Feedback
- Open [Issues](../../issues) for questions, suggestions, or use cases
- Participate in existing discussions, share your experience
- Help answer questions from others

#### 2. Schema Improvements
- Submit new schema extensions or domain-specific types
- Optimize existing schema field definitions
- Add new example use cases

**Process:**
1. Fork this repository
2. Modify or add schemas in the `schema/` directory
3. Add corresponding examples in `schema/examples/`
4. Run `npm run schema:validate` to ensure validity
5. Submit a Pull Request explaining your changes

#### 3. Documentation
- Improve clarity of README and other docs
- Add translations (currently supporting EN and ZH)
- Write tutorials or best practice guides

#### 4. Implementations & Integrations
- Share OHAP-based implementations (SDKs, tools, platforms)
- Provide real-world integration examples
- Contribute reference implementation code

### Contribution Guidelines

#### Schema Design Principles
1. **Human-AI Fusion First**: Emphasize shared intent and mutual responsibility
2. **Verifiability**: Include evidence and provenance fields
3. **Async-Friendly**: Support partial updates and milestones
4. **Backward Compatible**: Avoid breaking changes when possible
5. **Extensible**: Use `additionalProperties` for domain extensions

#### Code Style
- JSON Schema uses draft-07 standard
- Example JSON files use 2-space indentation
- Field names use camelCase
- Enum values use kebab-case

#### Pull Request Process
1. Ensure PR description clearly explains what and why
2. Link related Issues if any
3. Breaking changes must be tagged `[BREAKING]` in PR title
4. Wait for maintainer review (typically 3-5 business days)

### Code of Conduct

We pledge to provide a friendly, safe, and inclusive environment for all:

- **Respect**: Honor different viewpoints and experiences
- **Collaborate**: Give and accept constructive feedback
- **Welcome**: Be inclusive of contributors from all backgrounds
- **Focus**: Prioritize what's best for the community

Unacceptable behaviors include but are not limited to: harassment, discrimination, offensive comments, privacy violations, etc.

Report violations to project maintainers.

---

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (see [LICENSE](LICENSE)).

Thank you for helping build the future of human-AI collaboration! 🤝

---

## 中文

### 如何贡献

#### 1. 讨论与反馈
- 在 [Issues](../../issues) 中提出问题、建议或用例
- 参与现有讨论，分享你的经验和见解
- 帮助回答其他人的问题

#### 2. Schema 改进
- 提交新的 schema 扩展或领域特定类型
- 优化现有 schema 的字段定义
- 添加新的示例用例

**流程：**
1. Fork 本仓库
2. 在 `schema/` 目录下修改或添加 schema
3. 在 `schema/examples/` 添加相应示例
4. 运行 `npm run schema:validate` 确保有效性
5. 提交 Pull Request 并说明修改理由

#### 3. 文档贡献
- 改进 README 和其他文档的清晰度
- 添加翻译（目前支持中英文）
- 编写教程或最佳实践指南

#### 4. 实现与集成
- 分享基于 OHAP 的实现（SDK、工具、平台）
- 提供真实世界的集成案例
- 贡献参考实现代码

### 贡献指南

#### Schema 设计原则
1. **人机融合优先**：强调共同意图和相互责任
2. **可验证性**：包含证据和溯源字段
3. **异步友好**：支持部分更新和里程碑
4. **向后兼容**：尽量避免破坏性变更
5. **扩展性**：使用 `additionalProperties` 支持领域扩展

#### 代码风格
- JSON Schema 使用 draft-07 标准
- 示例 JSON 文件使用 2 空格缩进
- 字段名使用 camelCase
- 枚举值使用 kebab-case

#### Pull Request 流程
1. 确保 PR 描述清晰说明改动内容和原因
2. 关联相关 Issue（如有）
3. 破坏性变更需在 PR 标题标注 `[BREAKING]`
4. 等待维护者审核（通常 3-5 个工作日）

### 行为准则

我们承诺为所有人提供友好、安全、包容的环境：

- **尊重**：尊重不同观点和经验
- **协作**：以建设性方式提供和接受反馈
- **包容**：欢迎各种背景的贡献者
- **专注**：聚焦于对社区最有益的事情

不可接受的行为包括但不限于：骚扰、歧视、攻击性言论、侵犯隐私等。

违反行为准则的行为请报告至项目维护者。

