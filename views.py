
from django.shortcuts import render
from .models import Lista

# Função para renderizar a página inicial do blog
def blog(request):
    context = {
        'title': 'blog - ',
       
    }
    return render(request, 'blog/lista_produtos.html', context)


# Função para renderizar a página de exemplo
def exemplo(request):
    context = {
        
        'title': ' - ',
    }
    return render(request, 'blog/exemplo.html', context)

from django.shortcuts import render
from .models import Lista  # Certifique-se de que Produto é o nome correto do modelo

def lista_produtos(request):
    if request.method == 'POST':
        # Criar uma instância do modelo Produto
        novo_produto = Lista()  
        novo_produto.cod_produto = request.POST.get("campo_codigo")
        novo_produto.des_produto = request.POST.get("Descricao")
        novo_produto.qtd_produtos = request.POST.get("Quantidade")
        novo_produto.validade_produto = request.POST.get("Data_validade")
        novo_produto.setor = request.POST.get("setor_colaborador")
        
        # Salvar o novo produto no banco de dados
        novo_produto.save()  

    # Recuperar todos os produtos
    produtos = Lista.objects.all()

    # Passar os produtos para o template
    return render(request, 'blog/lista_produtos.html', {'produtos': produtos})
