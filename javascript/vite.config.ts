import { defineConfig } from 'vite'
import { resolve } from 'path'
import dts from 'vite-plugin-dts'

export default defineConfig({
  build: {
    lib: {
      entry: resolve(__dirname, 'src/index.ts'),
      name: 'OHAP',
      formats: ['es', 'cjs', 'umd'],
      fileName: (format) => {
        if (format === 'es') return 'ohap.mjs'
        if (format === 'cjs') return 'ohap.cjs'
        return 'ohap.umd.js'
      },
    },
    rollupOptions: {
      external: [],
      output: {
        globals: {},
        exports: 'named',
      },
    },
    sourcemap: true,
    minify: 'terser',
  },
  plugins: [
    dts({
      insertTypesEntry: true,
      rollupTypes: true,
    }),
  ],
})
