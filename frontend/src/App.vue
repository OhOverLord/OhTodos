<template>
  <div id="app">
    <h1>OhTodos</h1>  
    <AddTodo
    @add-todo="addTodo"
    />
    <select v-model="filter">
      <option value="all">All</option>
      <option value="completed">Completed</option>
      <option value="not-completed">Not completed</option>
    </select>
    <hr>
    <todo-list v-bind:todos="filteredTodos" v-on:remove-todo="removeTodo" v-if="filteredTodos.length"/>
    <p v-else>No todos!</p>
    <hr>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList'
import AddTodo from '@/components/AddTodo'

export default {
  name: 'App',
  data() {
    return {
      todos: [],
      filter: 'all'
    }
  },
  components: {
    TodoList, AddTodo
  },
  methods: {
    removeTodo(id) {
      this.todos = this.todos.filter(function(t) {
        return t.id != id
      })
      const requestOptions = {
          method: "DELETE",
          headers: { "Content-Type": "application/json" },
      };
      fetch("http://127.0.0.1:8000/delete-todo/" + id, requestOptions);
    },
    addTodo(todo) {
      this.todos.push(todo)
    }
  },
  mounted() {
    fetch('http://127.0.0.1:8000/todo-list/')
    .then(response => response.json())
    .then(json => {
      this.todos = json
    })
  },
  computed: {
    filteredTodos() {
      if(this.filter == 'all') {
        return this.todos
      }
      if(this.filter == 'completed') {
        return this.todos.filter(function(t) {
            return t.completed
        })
      }
      if(this.filter == 'not-completed') {
        return this.todos.filter(function(t) {
            return !t.completed
        })
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
