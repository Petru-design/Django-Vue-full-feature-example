<template>
    Details for coach [[id]]
    <router-view></router-view>
    <router-link to="/coaches/c1/contact">Contact</router-link>
</template>

<script>
export default {
    props: ['id'],
}
</script>