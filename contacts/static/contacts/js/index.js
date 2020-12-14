new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data () {
        return {
            contacts: null
          }
    },
    mounted () {
      axios
        .get('/list_contacts')
        .then(response => (this.contacts = response.data))
    }
  })
