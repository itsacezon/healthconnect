<template lang="jade">
header.header__wrapper
  nav.nav__wrapper(role="navigation")
    .nav.nav--left
      //- a.nav__link.nav--home(v-link="{ name: 'home' }")
      //-   img.nav__logo(src="/static/img/logo-glyph.png" height="32")
      form.nav__search
        input(type="text" tabindex="-1" placeholder="Search Health App")

    .nav.nav--right
      a.nav__link(href="#0") Report
      a.nav__link(href="#0") Rate
</template>

<script>
export default {
}
</script>
