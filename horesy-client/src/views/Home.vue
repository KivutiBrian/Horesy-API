<template>
  <main>
    <div class="hero">
      <div class="h-container">
        <div class="main-heading">
          <h1 class="title">Explore</h1>
          <h2 class="subtitle">Luxury hotels</h2>
          <!-- <br><br><br><br><br><br><h1>hell</h1> -->
        </div>
        <router-link class="h-btn h-btn-gradient" to="#">
            Explore now
            <span class="dots"><i class="fa fa-ellipsis-h"></i></span>
          </router-link>
      </div>
    </div>
  </main>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {

  }
}
</script>

<style scoped>
.hero{
  width: 100%;
  height: 100vh;
  background: url("../assets/landing-page.jpg") center no-repeat;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  position: relative;
  z-index: 0;
}

.hero::before{
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: inherit;
  height: inherit;
  background-color: var(--purple-transparent-alt);
  z-index: -1;
}

.main-heading{
  color: #fff;
  line-height: 1;
  text-shadow: 1px 1px 1rem rgba(0,0,0, .5);
  margin-bottom: 2.5rem;
}

.title{
  font-size: 4.8rem;
  text-transform: uppercase;
  letter-spacing: 3px;
}

.subtitle{
  font-size: 3.4rem;
  font-weight: 300;
  font-family: 'Pacifico', cursive;
}

.h-btn-gradient{
  background-image: var(--gradient-color);
}

</style>
