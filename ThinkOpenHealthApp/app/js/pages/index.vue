<template lang="jade">
v-header
h1 {{ msg }}
</template>

<script>
import Header from '../components/header.vue'

export default {
  data () {
    return {
      msg: 'Du bist ein Arsch mit Ohren'
    }
  },
  components: {
    'v-header': Header
  }
}
</script>
