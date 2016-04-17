<template lang="jade">
header.header__wrapper
  nav.nav__wrapper(role="navigation")
    .nav.nav--left
      a.nav__link.nav--home(v-link="{ name: 'home' }")
        .nav__logo
        h3.nav__logo-title HealthConnect

    .nav.nav--right
      a.nav__link(v-link="{ name: 'home' }") Programs
      a.nav__link(href="#0")
        span Brgy. Balara
        img(src="/static/img/icons/navigation/ic_arrow_drop_down_18px.svg" height="18")

</template>

<script>
export default {
}
</script>
