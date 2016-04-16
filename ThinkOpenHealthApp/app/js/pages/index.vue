<template lang="jade">
v-header
section.page__wrapper
  .content__wrapper
    .content__section
      a.button(href="#0" @click.prevent="showProgramModal = true") Start a program

v-modal(:show.sync="showProgramModal")
  div(slot="content" style="width:300px;")
    h3 New program
    form(method="POST")
      .form__element
        .form__label Program Type
        .form__select
          select
            option Deworming
            option Fitness Program
      .form__element
        .form__label Program Name
        input(type="text")
      .form__element
        button(type="submit" @click.prevent="showProgramModal = false") Submit report
</template>

<script>
import Header from '../components/header.vue'
import Modal from '../components/modal.vue'

export default {
  data () {
    return {
      showProgramModal: false,
    }
  },
  components: {
    'v-header': Header,
    'v-modal': Modal
  }
}
</script>
