import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

export default defineConfig({
    plugins: [svelte()],
    base: "/wpilib-cli/",
    build: {
        outDir: "../docs",
        emptyOutDir: true,
    },
});
