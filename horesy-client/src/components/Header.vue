<template>
    <header class="h-header">
        <slot name="brand"></slot>
        <slot name="nav"></slot>
    </header>
</template>

<script>
export default {
  name: 'Header'

}
</script>

<style scoped>
.h-header{
    width: 100%;
    height: 6rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: fixed;
    top: 0;
    left: 0;
    background-color: #073b4c;
    z-index: 999;
}

</style>
