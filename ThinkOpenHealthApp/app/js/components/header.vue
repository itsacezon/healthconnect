<template lang="jade">
header.header__wrapper
  nav.nav__wrapper(role="navigation")
    .nav.nav--left
      a.nav__link.nav--home(v-link="{ name: 'home' }")
        img.nav__logo(src="/static/img/icons/maps/ic_local_hospital_48px.svg" height="40")
        h4.nav__logo-title Health App

    .nav.nav--right
      a.nav__link(v-link="{ name: 'home' }") Programs
      a.nav__link(href="#0") People

</template>

<script>
export default {
}
</script>
