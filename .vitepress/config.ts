import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: "/ohap/",
  srcDir: "doc",
  locales: {
    root: {
      label: "English",
      lang: "en-US",
      title: "Open Human Agent Protocol",
      description: "The foundational protocol for the Solo-Corp era. Standardizing how AI Agents invoke human intelligence as a seamless API. Bridging the gap between silicon-speed logic and human-scale creativity through asynchronous, structured, and verifiable task-coupling.",
      themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
          { text: "Home", link: "/" },
          {
            text: "SDKs", items: [
              { text: "JavaScript", link: "/sdk" },
              { text: "Python", link: "/sdk-python" }
            ]
          },
          { text: "Examples", link: "/markdown-examples" }
        ],
        sidebar: [
          {
            text: "Examples",
            items: [
              { text: "Markdown Examples", link: "/markdown-examples" },
              { text: "Runtime API Examples", link: "/api-examples" }
            ]
          },
          {
            text: "SDKs",
            items: [
              { text: "JavaScript/TypeScript", link: "/sdk" },
              { text: "Python", link: "/sdk-python" }
            ]
          },

        ],
        socialLinks: [
          { icon: "github", link: "https://github.com/vuejs/vitepress" }
        ]
      }
    },
    zh: {
      label: "中文",
      lang: "zh-CN",
      title: "开放人类代理协议",
      description: "面向 Solo-Corp 时代的基础协议，标准化 AI 代理如何以异步、结构化、可验证的方式调用人类智能。",
      themeConfig: {
        nav: [
          { text: "首页", link: "/zh/" },
          {
            text: "SDK", items: [
              { text: "JavaScript", link: "/zh/sdk" },
              { text: "Python", link: "/zh/sdk-python" }
            ]
          },
          { text: "示例", link: "/zh/markdown-examples" }
        ],
        sidebar: [
           {
            text: "示例",
            items: [
              { text: "Markdown 示例", link: "/zh/markdown-examples" },
              { text: "运行时 API 示例", link: "/zh/api-examples" }
            ]
          },
          {
            text: "SDK",
            items: [
              { text: "JavaScript/TypeScript", link: "/zh/sdk" },
              { text: "Python", link: "/zh/sdk-python" }
            ]
          },
        ],
        socialLinks: [
          { icon: "github", link: "https://github.com/vuejs/vitepress" }
        ]
      }
    }
  }
})
