<template lang="jade">
header.header__wrapper
  nav.nav__wrapper(role="navigation")
    .nav.nav--left
      a.nav__link.nav--home(v-link="{ name: 'home' }")
        img.nav__logo(src="/static/img/icons/maps/ic_local_hospital_48px.svg" height="40")
      a.nav__link(v-link="{ name: 'home' }") Programs
      a.nav__link(href="#0") People

    .nav.nav--right
      a.nav__link(href="#0") Logout
</template>

<script>
export default {
}
</script>
