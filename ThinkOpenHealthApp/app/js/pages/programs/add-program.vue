<template lang="jade">
h3 New program
form(@submit.prevent="dispatchRequest")
  .form__element
    .form__label Title
    input(type="text" placeholder="What is the program called?" v-model="program.title")
  .form__element
    .form__label Description
    textarea(rows="3" placeholder="What is it about?" v-model="program.sessions[0].description")
  .form__element
    .form__label Barangay
    .form__select
      select(v-model="program.barangay_id")
        //- option(disabled selected hidden value="0") Choose your barangay..
        option(v-for="barangay in barangays" v-bind:value="barangay.id - 1") {{ barangay.full_name }}, {{ barangay.city }}
  .form__element
    .form__label Venue
    input(type="text" placeholder="Where in your barangay?" v-model="program.sessions[0].address")
  .form__element
    .form__label Fee
    input(type="text" placeholder="How much is the program? ('Free' if Php 0.00)" v-model="program.sessions[0].fee")
  .form__element
    button(type="submit") Create program
</template>

<script>
function defaultProgram () {
  return {
    title: '',
    barangay_id: 0,
    sessions: [
      {
        id: 1,
        description: '',
        address: '',
        date: new Date().toISOString(),
        fee: null
      }
    ]
  }
}
export default {
  data () {
    return {
      program: defaultProgram(),
      barangays: []
    }
  },
  created () {
    this.$http.get('barangay').then(
      (response) => {
        this.barangays = response.data
      },
      (response) => {
        console.log('Failed to retrieve barangays.')
      }
    )
  },
  methods: {
    dispatchRequest () {
      this.program.barangay_id++
      this.$dispatch('request', this.program)
      this.program = defaultProgram()
    }
  }
}
</script>
