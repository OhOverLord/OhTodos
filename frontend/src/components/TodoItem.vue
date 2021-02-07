<template>
    <li>
        <span :class="{done: todo.completed}">
            <input type="checkbox" v-on:change="todoCompleted(todo)" :checked="todo.completed">
            {{todo.text}}
        </span>
        <a class="rm" v-on:click="$emit('remove-todo', todo.id)">&times;</a>
    </li>
</template>

<script>
export default {
    props: {
        todo: {
            type: Object,
            required: true,
        },
        index: Number,
    },
    methods: {
        todoCompleted(todo) {
            todo.completed = !todo.completed
            fetch("http://127.0.0.1:8000/todo-status/" + todo.id);
        }
    }
}
</script>

<style scoped>
li {
    display: flex;
    justify-content: space-between;
    padding: .5rem 2rem;
    border: 1px solid gray;
    width: 50%;
    margin: auto;
    margin-bottom: 1rem;
    align-items: center;
}

.rm {
  font-weight: 700;
  color: white;
  text-decoration: none;
  padding: .8em 1em calc(.8em + 3px);
  border-radius: 3px;
  background: rgb(64,199,129);
  box-shadow: 0 -3px rgb(53,167,110) inset;
  transition: 0.2s;
} 
.rm:hover { background: rgb(53, 167, 110); }
.rm:active {
  background: rgb(33,147,90);
  box-shadow: 0 3px rgb(33,147,90) inset;
}

input {
    margin-right: 1rem;
}

.done {
    text-decoration: line-through;
}
</style>