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
    component: require('./pages/index.vue')
  },
  '/program/:id': {
    name: 'program',
    component: require('./pages/programs/view-program.vue')
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
