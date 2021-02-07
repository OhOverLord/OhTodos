<template>
    <form @submit.prevent="onSubmit">
        <input type="text" v-model="title">
        <button type="submit">Create</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            title: ''
        }
    },
    methods: {
        onSubmit(){
            if(this.title.trim()) {
                const requestOptions = {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ "text": this.title })
                };
                this.title = ''
                fetch("http://127.0.0.1:8000/todo-list/", requestOptions)
                    .then(response => response.json())
                    .then(json => this.$emit('add-todo', json));
            }
        }
    }

}
</script>

<style scoped>
form {
    display: flex;
    justify-content: center;
    align-items: center;
}

input {
    width: 400px;
}
</style>