const tabela = document.querySelector('.tabela-js')

axios.get('http://10.109.142.96:5000/list').then(function(resposta){
    //Pegando dados da requisição (Pegar os dados precisa fazer uma requisição antes)
    getData(resposta.data)
}).catch(function(error){
    console.log(error)
})

//Percorrer array
function getData(dados){
    //Funciona da mesma forma que o forEach, criando uma array function
    dados.map((item)=> {
        tabela.innerHTML += `
            <tr>
                <th scope="row">${item.Id}</th>
                <td>${item.Tarefa}</td>
                <td><button type="button" class="btn btn-outline-primary"><i class="bi bi-pencil"></i>Editar</button>
                    <button type="button" class="btn btn-outline-danger"><i class="bi bi-trash"></i>Deletar</button>
                </td>
            </tr>
            `
    })
}
