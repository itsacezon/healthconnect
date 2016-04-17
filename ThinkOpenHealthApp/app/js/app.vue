<template>
<div>
  <router-view v-bind:images="images"></router-view>
</div>
</template>

<script>
export default {
  data () {
    return {
      images: [
        'http://img12.deviantart.net/a460/i/2012/297/3/8/quezon_memorial_circle_by_nikocruz-d5it4sl.jpg',
        'https://ayalalveoland.files.wordpress.com/2011/06/up-diliman-1.jpg',
        'http://photos.wikimapia.org/p/00/02/47/92/71_big.jpg',
        'http://photos.wikimapia.org/p/00/02/47/92/58_big.jpg',
        'http://www.mb.com.ph/wp-content/uploads/2016/01/Quezon-City-cityhall.jpg',
        'https://www.google.com/maps/d/u/0/thumbnail?mid=z9-guoirihpU.k8DJuT8RqnTc&hl=en_US'
      ]
    }
  }
}
</script>
