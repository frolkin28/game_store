<template>
  <div id="app">
    <Header/>
    <GamesArea/>
  </div>
</template>

<script>
import Header from "@/components/Header"
import GamesArea from "@/components/GamesArea"

export default {
  name: 'App',
  components: {
    Header,
    GamesArea
  }
}
</script>

<style>

body {
    background-color: #000000;
}

</style>
