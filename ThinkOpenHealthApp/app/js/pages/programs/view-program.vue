<template lang="jade">
v-header
section.page__wrapper
  .content__wrapper
    .content__section
      article.content__primary(v-if="program")
        .u-div-240.u-bg-c-dgray.u-br-t-4
          .u-bg-img.u-flex-center(v-bind:style="{ backgroundImage: 'url(' + programCoverImage + ')' }")
            h2 {{ program.title }}
        .form__wrapper
          p.large
            strong.u-small.u-td-upper Description
            br
            span {{ program.sessions[0].description }}
          p.large
            strong.u-small.u-td-upper Date
            br
            span {{ program.sessions[0].date | toDateString }}
          p.large
            strong.u-small.u-td-upper Location
            br
            span {{ program.sessions[0].address}}, {{ program.barangay_name }}
          p.large
            strong.u-small.u-td-upper Fees
            br
            span {{ program.sessions[0].fee | capitalize }}
        .form__wrapper
          .u-cf
            h4.u-ft-left Attendees
            a.button.button--small.button--inverted.u-ft-right(href="#0" @click.prevent="notifyAttendees") Notify attendees
          .users(v-if="program.sessions[0].attendees.length !== 0")
            .user(v-for="attendee in program.sessions[0].attendees")
              h4.u-mg-b-4 {{ users[attendee.user_id - 1].full_name }}
              p.small
                span {{ users[attendee.user_id - 1].address }}, {{ program.barangay_name }}
                br
                span {{ users[attendee.user_id - 1].phone_number }}
          .u-ta-c
            h3.u-mg-b-14(v-if="program.sessions[0].attendees.length === 0")
              span.header--light There are currently no attendees.
            a.button.button--small(href="#0" @click.prevent="showAttendeesModal = true") Add attendee

v-modal(:show.sync="showAttendeesModal")
  div(slot="content" style="width:300px;")
    h3.u-mg-b-14 Add an attendee
    form(@submit.prevent="addAttendee")
      .form__element
        .form__select
          select(v-model="attendee.user_id")
            option(disabled selected hidden value="0") Choose from existing users..
            option(v-for="(index, user) in users" v-bind:value="index + 1") {{ user.full_name }} - No. {{ index + 1 }}
      .form__element
        button(type="submit") Add

v-modal(:show.sync="showNotifiedAttendees")
  div(slot="content" style="width:300px;")
    h3.u-mg-b-14 All attendees notified!
    p They will receive an SMS about the upcoming event.
    a.button.button--small(href="#0" @click.prevent="showNotifiedAttendees = false") Close

</template>

<script>
import Header from '../../components/header.vue'
import Modal from '../../components/modal.vue'

function attendee () {
  return {
    health_program_id: null,
    session_id: 0,
    user_id: 0
  }
}

export default {
  props: ['images'],
  data () {
    return {
      users: [
        {
          full_name: "Denise Leviste",
          address: "Maginhawa St.",
          barangay_id: 1,
          phone_number: "09123456789"
        },
        {
          full_name: "Mara Shen",
          address: "Salvador St.",
          barangay_id: 1,
          phone_number: "09123456789"
        },
        {
          full_name: "Gerald Roy",
          address: "Lt. Francisco St.",
          barangay_id: 1,
          phone_number: "09123456789"
        },
        {
          full_name: "Gabriel Chase Patron",
          address: "Salvador St.",
          barangay_id: 1,
          phone_number: "09123456789"
        }
      ],
      attendee: attendee(),
      program: null,
      showAttendeesModal: false,
      showNotifiedAttendees: false
    }
  },
  computed: {
    programCoverImage () {
      let index = this.program.id < 6 ? this.program.id - 1 : 5
      return this.images[index]
    }
  },
  filters: {
    toDateString (date) {
      return new Date(date).toDateString()
    }
  },
  created () {
    this.$http.get('program/' + this.$route.params.id).then(
      (response) => {
        this.program = response.data
        this.attendee.health_program_id = this.$route.params.id
      },
      (response) => {
        console.log('Failed to retrieve program details.')
      }
    )
  },
  methods: {
    addAttendee () {
      this.showAttendeesModal = false
      this.$http.post('attendee/', this.attendee).then(
        (response) => {
          this.program.sessions[0].attendees.push(this.attendee)
          this.attendee = attendee()
        },
        (response) => {
          console.log('Failed to add attendee')
        }
      )
    },
    notifyAttendees () {
      this.$http.get('send-sms').then(
        (response) => {
          this.showNotifiedAttendees = true
        },
        (response) => {
          console.log('Failed to submit')
        }
      )
    }
  },
  components: {
    'v-header': Header,
    'v-modal': Modal
  }
}
</script>
