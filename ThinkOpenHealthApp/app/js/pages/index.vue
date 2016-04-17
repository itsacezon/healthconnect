<template lang="jade">
v-header
section.page__wrapper
  .u-div-240.u-bg-c-dgray
    .u-bg-img.u-flex-center(style="background-image:url('static/img/header_bg.png');")
      h1 Local Health Programs
section.page__wrapper
  .content__wrapper
    .content__section
      .cards
        a.card.card--button(href="#0" @click.prevent="showProgramModal = true")
          .card__content.card--center
            span.button Start a program
        v-card(v-for="program in programs" v-bind:program="program" v-bind:images="images")

v-modal(:show.sync="showProgramModal")
  div(slot="content" style="width:400px;")
    v-add-program(@request="createProgram")

</template>

<script>
import Header from '../components/header.vue'
import Modal from '../components/modal.vue'
import Card from '../components/card.vue'

import AddProgram from './programs/add-program.vue'

export default {
  route: {
    data (transition) {
      return this.$http.get('program').then(
        (response) => ({ programs: response.data }),
        (response) => {
          console.log('Failed to retrieve programs.')
        }
      )
    }
  },
  props: ['images'],
  data () {
    return {
      programs: [],
      showProgramModal: false
    }
  },
  methods: {
    createProgram (program) {
      this.showProgramModal = false
      this.$http.post('program/', program).then(
        (response) => {
          this.programs.push(program)
        },
        (response) => {
          console.log('Failed to submit program.')
        }
      )
    }
  },
  components: {
    'v-header': Header,
    'v-modal': Modal,
    'v-card': Card,
    'v-add-program': AddProgram
  }
}
</script>
