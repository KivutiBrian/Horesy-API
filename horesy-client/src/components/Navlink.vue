<template>
  <div>
      <router-link class="link" :to="url">
          <slot></slot>
      </router-link>
  </div>
</template>

<script>
export default {
  name: 'NavLink',
  props: {
    url: String
  }

}
</script>

<style scoped>

.link{
    color: #fff;
    display: block;
    font-size: 2.7rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    padding: .3rem;
    margin-bottom: 1.6rem;
}

</style>
