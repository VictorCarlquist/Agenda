var v = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  propsData: ['pk'],
  data () {
      return {
          addresses: null
        }
  },
  methods: {
      delete_address: function ($event, pk) {
        delete_item('/info_address/' + pk);
      }
    },
  mounted () {
    id_contact = window.location.href.split('/');
    id_contact = id_contact[id_contact.length-1]
    axios
      .get('/list_address/' + id_contact)
      .then(response => (this.addresses = response.data));
  }
});

$(document).ready(function() {

  function limpa_formulário_cep() {
      // Limpa valores do formulário de cep.
      $("#street").val("");
      $("#extra_info").val("");
      $("#city").val("");
      $("#state").val("");
  }
  
  $("#zip_code").blur(function() {
      var cep = $(this).val().replace(/\D/g, '');
      if (cep != "") {
         var validacep = /^[0-9]{8}$/;
          if(validacep.test(cep)) {
              $("#street").val("...");
              $("#extra_info").val("...");
              $("#city").val("...");
              $("#state").val("...");

              $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {
                  if (!("erro" in dados)) {
                      $("#street").val(dados.logradouro);
                      $("#extra_info").val(dados.bairro);
                      $("#city").val(dados.localidade);
                      $("#state").val(dados.uf);
                  } 
                  else {
                      limpa_formulário_cep();
                      alert("CEP não encontrado.");
                  }
              });
          }
          else {
              limpa_formulário_cep();
              alert("Formato de CEP inválido.");
          }
      }
      else {
          limpa_formulário_cep();
      }
  });
});
