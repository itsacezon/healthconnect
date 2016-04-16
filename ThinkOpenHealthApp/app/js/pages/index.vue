<template lang="jade">
v-header
section.page__wrapper
  .content__wrapper
    .content__section
      a.button(href="#0" @click.prevent="showProgramModal = true") Start a program

v-modal(:show.sync="showProgramModal")
  div(slot="content" style="width:400px;")
    h3 New program
    form(method="POST")
      .form__element
        .form__label Title
        input(type="text" placeholder="What is the program called?")
      .form__element
        .form__label Barangay
        .form__select
          select
            option(disabled selected hidden value="0") Choose your location..
            option(v-for="barangay in barangays" v-bind:value="barangay.id") {{ barangay.full_name }}, {{ barangay.city }}
      .form__element
        button(type="submit" @click.prevent="showProgramModal = false") Create program
</template>

<script>
import Header from '../components/header.vue'
import Modal from '../components/modal.vue'

export default {
  route: {
    data (transition) {
      return this.$http.get('barangay').then(
        (response) => ({ barangays: response.data }),
        (response) => {
          console.log('Failed to retrieve barangays.')
        }
      )
    }
  },
  data () {
    return {
      barangays: [],
      showProgramModal: false,
    }
  },
  components: {
    'v-header': Header,
    'v-modal': Modal
  }
}
</script>
