<template>
    <div>
        <img src="" alt="">
        <h1></h1>
    </div>
</template>

<script>
export default {
    name: UserItem,
    data(){
        return {
            user: {
                full_name: '',
                city: null,

                
            }
        }
    },
    props: [user],
    
    mounted() {
        fetch()
    }
}
</script>

