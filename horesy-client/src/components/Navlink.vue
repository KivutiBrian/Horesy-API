<template>
  <div>
      <router-link  @click.native="$emit('hide-dropdown', false)" class="link" :to="url">
          <slot></slot>
      </router-link>

      <!-- click.native="$emit('hide-dropdown', false)" -->
  </div>
</template>

<script>
export default {
  name: 'NavLink',
  props: {
    url: String
  },
  methods: {
    hello () {
      console.log('Gaideh')
    }
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
