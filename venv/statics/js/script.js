const formulario = document.querySelector('.formulario');

formulario.addEventListener('submit', function(event) {
    event.preventDefault()
    
    const nome = document.getElementById("nome").value
    const telefone = document.getElementById("telefone").value
    const email = document.getElementById("email").value
    const senha = document.getElementById("senha").value
    
    if (email !== "" && senha !== "") {
        axios.post('127.0.0.1:5500/cadastro', { nome, telefone, email, senha })
        .then(response => {
            alert(response.data)
        })
        .catch(error => {
            console.error('Erro na requisição POST', error);
        })
    } else {
        console.log("Por favor, preencha todos os campos.");
    }
});
