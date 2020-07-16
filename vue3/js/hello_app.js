const { ref, reactive } = VueCompositionAPI;

Vue.component('todo-item', {
    props: ['todo'],
    template: '<li>Item: {{ todo.text }}</li>',
});

var app = new Vue({
    el: "#app",
    data: {
        groceryList: [
            { id: 0, text: 'Vegetables' },
            { id: 1, text: 'Cheese' },
        ],
        message: "Hello Todo list",
    },
});


