# 📁 OHAP 项目文件结构

## 核心文档
- [README.md](README.md) / [README.zh.md](README.zh.md) - 项目主文档（中英双语）
- [SDK.md](SDK.md) - JavaScript/TypeScript SDK完整文档
- [PYTHON-SDK.md](PYTHON-SDK.md) - Python SDK完整文档
- [CONTRIBUTING.md](CONTRIBUTING.md) - 贡献指南（中英双语）
- [LICENSE](LICENSE) - 开源许可

## 📜 JSON Schema
**位置：** [schema/](schema/)

核心schema定义：
- [task.schema.json](schema/task.schema.json) - 任务定义
- [proposal.schema.json](schema/proposal.schema.json) - 提案定义
- [contract.schema.json](schema/contract.schema.json) - 合约定义
- [deliverable.schema.json](schema/deliverable.schema.json) - 交付物定义
- [review.schema.json](schema/review.schema.json) - 审查定义

示例文件：
- [schema/examples/](schema/examples/) - 完整工作流示例

## 💻 SDK 源代码

### JavaScript/TypeScript SDK
**位置：** [src/](src/)

- [src/index.ts](src/index.ts) - OHAPClient主类
- [src/types.ts](src/types.ts) - TypeScript类型定义
- [src/validator.ts](src/validator.ts) - Schema验证工具

### Python SDK
**位置：** [python/ohap/](python/ohap/)

- [python/ohap/client.py](python/ohap/client.py) - OHAPClient异步客户端与OHAPClientSync同步客户端
- [python/ohap/types.py](python/ohap/types.py) - Python数据类型定义
- [python/ohap/validator.py](python/ohap/validator.py) - Schema验证工具
- [python/ohap/__init__.py](python/ohap/__init__.py) - 包初始化与导出
- [python/README.md](python/README.md) - Python SDK快速开始指南
- [python/requirements.txt](python/requirements.txt) - Python依赖

Python测试：
- [python/tests/test_client.py](python/tests/test_client.py) - 单元测试
- [python/tests/__init__.py](python/tests/__init__.py) - 测试包初始化

## 📚 示例代码

### JavaScript/TypeScript示例
**位置：** [examples/](examples/)

- [examples/basic-workflow.ts](examples/basic-workflow.ts) - JavaScript完整工作流演示
- [examples/README.md](examples/README.md) - 示例文档

### Python示例
**位置：** [examples/](examples/)

- [examples/basic_workflow_python.py](examples/basic_workflow_python.py) - Python完整工作流演示（异步与同步版本）

## 🔧 构建配置
- [package.json](package.json) - NPM包配置
- [vite.config.ts](vite.config.ts) - Vite构建配置
- [tsconfig.json](tsconfig.json) - TypeScript配置

## 📖 文档站点
**位置：** [doc/](doc/)

- [doc/index.md](doc/index.md) - 文档首页（英文）
- [doc/zh/index.md](doc/zh/index.md) - 文档首页（中文）
- [.vitepress/config.ts](.vitepress/config.ts) - VitePress配置（支持多语言）

## 🎨 演示
- [demo.html](demo.html) - 浏览器端SDK演示（UMD版本）

## 🚀 快速命令

### JavaScript/TypeScript SDK

```bash
# 安装依赖
npm install

# 构建SDK
npm run build

# 验证Schema
npm run schema:validate

# 启动文档站点
npm run docs:dev

# 运行示例
npx tsx examples/basic-workflow.ts
```

### Python SDK

```bash
# 安装SDK及其依赖
pip install -e .

# 安装开发依赖
pip install -e ".[dev]"

# 运行示例（异步）
python examples/basic_workflow_python.py

# 运行示例（同步）
python examples/basic_workflow_python.py sync

# 运行测试
pytest python/tests/

# 运行SDK演示
python -m ohap
```

## � 构建产物

### JavaScript/TypeScript
运行 `npm run build` 后，产物位于 `dist/` 目录：
- `dist/ohap.mjs` - ES模块版本
- `dist/ohap.cjs` - CommonJS版本
- `dist/ohap.umd.js` - UMD版本（浏览器）
- `dist/index.d.ts` - TypeScript类型定义

### Python
Python SDK通过以下方式安装：
- PyPI: `pip install ohap-sdk`
- 本地: `pip install -e .`
- 开发: `pip install -e ".[dev]"`

## 📋 开发流程

### 1. 修改Schema
1. 编辑 `schema/*.schema.json`
2. 更新 `schema/examples/` 中的示例
3. 运行 `npm run schema:validate` 验证

### 2. 修改JavaScript SDK
1. 编辑 `src/` 下的源文件
2. 运行 `npm run build` 构建
3. 测试 `examples/basic-workflow.ts` 中的示例

### 3. 修改Python SDK
1. 编辑 `python/ohap/` 下的源文件
2. 运行 `pytest python/tests/` 测试
3. 测试 `examples/basic_workflow_python.py` 中的示例

### 4. 更新文档
1. 编辑 `doc/` 或根目录的Markdown文件
2. 运行 `npm run docs:dev` 预览
3. 运行 `npm run docs:build` 构建生产版本

## 📄 发布清单

发布前确保：
- [ ] 所有Schema通过验证
- [ ] JavaScript SDK成功构建 (`npm run build`)
- [ ] Python SDK测试通过 (`pytest python/tests/`)
- [ ] JavaScript示例代码正常运行
- [ ] Python示例代码正常运行
- [ ] 文档站点可正常访问
- [ ] 版本号已更新（package.json、setup.py、pyproject.toml）
- [ ] CHANGELOG已更新（如有）

---

更多信息请参阅各目录下的README文件。
