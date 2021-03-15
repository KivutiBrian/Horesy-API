<template>
  <div id="app">

    <Header class="h-container">
      <template #brand>
        <h1 class="brand-name">Ho<span class="resy">resy</span></h1>
      </template>

      <template #nav>
        <navbar>
          <nav-link url="/">Home</nav-link>
          <nav-link url="/about">About</nav-link>
          <nav-link url="/offers">Offers</nav-link>
          <nav-link url="/contacts">Contacts</nav-link>
        </navbar>
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
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Crimson+Text&display=swap');

*,
*::before,
*::after{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root{
  --dark-clor: #2d2c2c;
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

.brand-name{
  font-family: 'Pacifico', cursive;
  font-size: 2.4rem;
  color: #fff;
  cursor: pointer;
}

.resy{
  color: #ef476f;
}

</style>
