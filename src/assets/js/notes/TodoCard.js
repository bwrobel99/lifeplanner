export const TodoCard = {
    delimiters: ['[[', ']]'],
    props: ['todo'],
    data() {
        return {
            id: 0,
            url: '',

            dates: {
                created: '',
                deadline: ''
            },

            isDone: false,
            bodyColor: 'black'
            
        }
    },
    watch: {
        isDone(val) {
            if (this.bodyColor == 'black') this.bodyColor = 'gray'
            else this.bodyColor = 'black'
        }
    },
    created() {
        this.id = this.todo.pk
        this.url = "todos/" + this.id
        this.dates.created = new Date(this.todo.fields.created)
        this.dates.deadline = new Date(this.todo.fields.deadline)
        this.isDone = this.todo.fields.isDone
    },
    template: '#todo-card-template',
}