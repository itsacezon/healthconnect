import Vue from 'vue'
import App from './app.vue'
import router from './router'
import { initResource } from './resource'

Vue.config.debug = location.hostname === 'localhost'
initResource()
router.start(App, '#app')
