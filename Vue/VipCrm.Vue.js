Vue.component('nav_header', {
    template: '<p style="color:red;">我是被全局注册的组件</p>'
})


Vue.component('button-counter', {
    data: {
        count: 0
    },
    import(),
    template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
})