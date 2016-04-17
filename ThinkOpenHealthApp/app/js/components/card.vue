<template lang="jade">
a.card(v-link="{ name: 'program', params: { id: program.id } }")
  .card__image(v-bind:style="{ backgroundImage: 'url(' + programImage + ')' }")
  .card__content
    h3.card__header.u-truncate {{ program.title }}
    p.u-truncate {{ program.sessions[0].description }}
    hr
    p
      strong.u-small.u-td-upper Date
      br
      span {{ program.sessions[0].date | toDateString }}
    p
      strong.u-small.u-td-upper Location
      br
      span {{ program.sessions[0].address}}, {{ program.barangay_name }}
</template>

<script>
export default {
  props: ['program', 'images'],
  computed: {
    programImage () {
      let index = this.program.id < 6 ? this.program.id - 1 : 5
      return this.images[index]
    }
  },
  filters: {
    toDateString (date) {
      return new Date(date).toDateString()
    }
  }
}
</script>
