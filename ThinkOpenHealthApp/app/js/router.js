import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const router = new VueRouter({
  history: true,
  saveScrollPosition: true
})

router.map({
  '/index': {
    name: 'home',
    guest: true,
    component: require('./pages/index.vue')
  }
})

router.alias({
  '': '/index'
})

// router.afterEach((transition) => {
//   let title = transition.to.name || 'page-not-found'
//   document.title = 'Student Assembly - ' + toTitleCase(title)
// })

export default router
