
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    'nuxt-primevue'
  ],
  primevue: {
    components: {
      include: ['Button','Fieldset','Avatar','Image']
    }
  }
})