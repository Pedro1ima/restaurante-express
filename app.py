import os

restaurantes = [{"nome":"Sushi Bar", "categoria":"Japonesa", "ativo":False}, 
                {"nome":"Pizza Suprema", "categoria":"Pizza", "ativo":True}, 
                {"nome":"Cantina Bear", "categoria":"Italiano", "ativo":False}]


def exibir_nome_do_programa():
    """ Essa função é responsável por mostrar o nome do App na tela do usuário """
    print("""
          
█▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
█▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
""") # Método para pular a linha como se fosse um \n.

def exibir_opcoes():
    """ Essa função é responsável por exibir as opções para os usuários """
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair \n")


def escolher_opcao():
    """ Solicita e executa a opção escolhida pelo usuário
    
    Inputs:
    - Opção desejada
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    
    
    """
    try: # Try para corrigir o problema caso o usuario digite uma letra. Pois daria erro,
         # já que o type da variavel "opcao_escolhida" está como "int".
        opcao_escolhida = int(input("Escolha uma opção: "))

        if(opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif(opcao_escolhida == 2):
            listar_restaurantes()
        elif(opcao_escolhida == 3):
            alternar_estado_do_restaurante()
        elif(opcao_escolhida == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except: # Caso o valor de entrada do usuario não seja um 'int', vai rodar a opcao_invalida().
        opcao_invalida()


def finalizar_app():
    """Essa função é responsável por encerrar o programa """
    exibir_subtitulo_do_menu("Encerrando o App")
    
    
def opcao_invalida():
    """ Exibe uma mensagem de opção inválida e depois retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    
    
    """
    print("Opção Inválida!\n")
    input("Digite uma tecla para voltar ao Menu Principal ")
    voltar_ao_menu_principal()
    
    
def cadastrar_novo_restaurante():
    """ Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria
    
    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    
    """
    exibir_subtitulo_do_menu("Cadastro de novos restaurantes")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria_do_restaurante = input(f"Digite o nome da categoria dos restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria":categoria_do_restaurante, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado na categoria {categoria_do_restaurante}.\n")
    
    voltar_ao_menu_principal()


def listar_restaurantes():
    """ Lista todos os restaurantes presentes na lista
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    
    """
    exibir_subtitulo_do_menu("Listando os restaurantes")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"} \n")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo_restaurante = "Ativado" if restaurante["ativo"] else "Desativado" # Se "ativo" do restaurante for True, vai aparecer "Ativado", caso não, vai aparecer "Desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}") #".ljust()" -> Serve para ter um espaçamento padrão entre todos os elementos.
    voltar_ao_menu_principal()



def voltar_ao_menu_principal():
    """ Solicita uma tecla para voltar ao menu principal
    
    Outputs:
    - Retorna ao menu principal
    
    """
    input("\nDigite uma tecla para voltar ao Menu Principal ")
    main()
    
def exibir_subtitulo_do_menu(texto):
    """ Exibe um subtítulo estilizado na tela
    
    Inputs:
    - Texto: str - O texto do subtítulo
    
    """
    os.system("cls") # Serve para limpar o Terminal, para apenas aparecer o print abaixo.
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()



def alternar_estado_do_restaurante():
    """ Essa função é responsável por alternar o estado do restaurante de ativo para desativado ou vice-versa 
    
    Inputs:
    - Nome do Restaurante
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    
    """
    exibir_subtitulo_do_menu("Alternando o estado do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if(nome_restaurante == restaurante["nome"]):
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso."
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()


def main():
    """ Função principal que inicia o programa """
    
    exibir_nome_do_programa()
    
    exibir_opcoes()
    
    escolher_opcao()


if(__name__ == "__main__"):
    main()