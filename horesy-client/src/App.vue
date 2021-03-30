<template>
  <div id="app">

    <Header class="h-container">
      <template #brand >
        <h1 class="brand-name">Ho<span class="resy">resy</span></h1>
      </template>

      <template #nav>
        <navbar :showBars="showBars">
          <nav-link @hide-dropdown="hideDropDown" url="/">Homeee</nav-link>
          <nav-link @hide-dropdown="hideDropDown" url="/about">About</nav-link>
          <nav-link @hide-dropdown="hideDropDown" url="/offers">Offers</nav-link>
          <nav-link @hide-dropdown="hideDropDown" url="/contacts">Contacts</nav-link>
        </navbar>
        <i @click="toggleBars"
          class="fas bars"
          :class="{'fa-times':showBars, 'fa-bars':!showBars}"></i>

      </template>

    </Header>

    <router-view/>
  </div>
</template>

<script>

import Header from './components/Header'
import Navbar from './components/Nav'
import NavLink from './components/Navlink'

export default {
  name: 'App',
  components: {
    Header,
    Navbar,
    NavLink
  },
  data () {
    return {
      showBars: false
    }
  },
  methods: {
    toggleBars () {
      this.showBars = !this.showBars
      console.log('He')
    },
    hideDropDown (state) {
      this.showBars = state
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Crimson+Text&display=swap');

*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root{
  --dark-clor: #2d2c2c;
  --purple-light: #8f50fb;
  --yellow-solid: #fa9e2c;
  --purple-transparent: rgba(53,10,79, .7);
  --purple-transparent-alt: rgba(74, 12, 112, 0.5);
  --gradient-color: linear-gradient(to right, var(--yellow-solid), var(--purple-light));
}

// global styles
html{
  font-size: 10px;
}

body{
  font-family: 'Crimson Text', serif;
}

a{
  text-decoration: none;
  color: inherit;
}

ul{
  list-style: none;
}

section{
  padding: 5rem 0;
}

// reusable
.h-container{
  width: 100%;
  max-width: 120rem;
  padding: 0 1.5rem;
  margin: 0 auto;
}

.h-btn{
  color: #fff;
  font-size: 1.3rem;
  font-weight: bold;
  text-transform: capitalize;
  padding: .5rem 3.5rem;
  border: none;
  border-radius: 10rem;
}

// reusable end here

.brand-name{
  font-family: 'Pacifico', cursive;
  font-size: 2.4rem;
  color: #fff;
  z-index:1;
  cursor: pointer;

}

.resy{
  color: #ef476f;
}

.bars{
  color:#ef476f;
  font-size:26px;
  position: relative;
  cursor: pointer;
}

</style>
