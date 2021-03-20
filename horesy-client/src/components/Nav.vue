<template>
  <nav class="nav">
      <ul class="nav-ul" :class="{'visible': showBars, 'hide':!showBars}">
          <slot></slot>
      </ul>
  </nav>
</template>

<script>
export default {
  name: 'Navbar',
  props: {
    showBars: Boolean
  }

}
</script>

<style scoped>

.nav{
    display: flex;
    align-items: center;
}

.nav-ul{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background-color: #073b4c;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 0;
    opacity: 0;
    transform: scale(0);
    transition: all .5s ease-in-out;
}

.visible{
  opacity: 1;
  transform: scale(1);
}

.hidden{
  opacity: 0;
}

</style>
