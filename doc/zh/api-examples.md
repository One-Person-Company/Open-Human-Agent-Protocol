---
outline: deep
---

# 运行时 API 示例

此页演示 VitePress 运行时 API 的使用方式（内容与英文版保持一致）。

主要的 `useData()` API 可用于获取站点、主题与页面数据。在 `.md` 和 `.vue` 文件中均可使用：

```md
<script setup>
import { useData } from 'vitepress'

const { theme, page, frontmatter } = useData()
</script>

## Results

### Theme Data
<pre>{{ theme }}</pre>

### Page Data
<pre>{{ page }}</pre>

### Page Frontmatter
<pre>{{ frontmatter }}</pre>
```

<script setup>
import { useData } from 'vitepress'

const { site, theme, page, frontmatter } = useData()
</script>

## Results

### Theme Data
<pre>{{ theme }}</pre>

### Page Data
<pre>{{ page }}</pre>

### Page Frontmatter
<pre>{{ frontmatter }}</pre>

## 更多

请查看完整运行时 API 列表：https://vitepress.dev/reference/runtime-api#usedata

