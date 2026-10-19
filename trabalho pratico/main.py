import csv
import os

# ==========================================
# 1. GERÊNCIA DE ARQUIVOS E DADOS
# ==========================================

def carregar_dados(nome_arquivo):
    """
    Lê um arquivo CSV e retorna os dados.
    Entradas: nome_arquivo (string)
    Saídas: lista de dicionários contendo os registros.
    """
    dados = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, mode='r', encoding='utf-8') as file:
            leitor = csv.DictReader(file)
            for linha in leitor:
                dados.append(linha)
    return dados

def salvar_dados(nome_arquivo, campos, dados):
    """
    Salva a lista de dicionários no arquivo CSV sobrescrevendo o antigo.
    Entradas: nome_arquivo (string), campos (lista), dados (lista de dicts)
    Saídas: Nenhuma.
    """
    with open(nome_arquivo, mode='w', encoding='utf-8', newline='') as file:
        escritor = csv.DictWriter(file, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)

# ==========================================
# 2. CRUD DE USUÁRIOS
# ==========================================

def criar_usuario(usuarios):
    """ (Create) Adiciona um novo usuário ao sistema. """
    print("\n--- CADASTRAR NOVO USUÁRIO ---")
    login = input("Digite o login: ")
    senha = input("Digite a senha: ")
    print("Perfis disponíveis: gerente, funcionario, cliente")
    perfil = input("Digite o perfil: ").lower()
    
    usuarios.append({'login': login, 'senha': senha, 'perfil': perfil})
    print(f"Sucesso! Usuário '{login}' cadastrado.")

def listar_usuarios(usuarios):
    """ (Read) Lista todos os usuários cadastrados. """
    print("\n--- LISTA DE USUÁRIOS ---")
    for u in usuarios:
        print(f"Login: {u['login']} | Perfil: {u['perfil'].capitalize()}")

def atualizar_usuario(usuarios):
    """ (Update) Atualiza a senha ou perfil de um usuário. """
    print("\n--- ATUALIZAR USUÁRIO ---")
    login_busca = input("Digite o login do usuário que deseja alterar: ")
    
    for u in usuarios:
        if u['login'] == login_busca:
            nova_senha = input("Nova senha (deixe em branco para manter a atual): ")
            novo_perfil = input("Novo perfil (deixe em branco para manter o atual): ")
            
            if nova_senha: u['senha'] = nova_senha
            if novo_perfil: u['perfil'] = novo_perfil
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado.")

def deletar_usuario(usuarios):
    """ (Delete) Remove um usuário do sistema. """
    print("\n--- DELETAR USUÁRIO ---")
    login_busca = input("Digite o login do usuário a ser deletado: ")
    
    for i in range(len(usuarios)):
        if usuarios[i]['login'] == login_busca:
            removido = usuarios.pop(i)
            print(f"Usuário '{removido['login']}' deletado!")
            return
    print("Usuário não encontrado.")

# ==========================================
# 3. CRUD DE PRODUTOS (RELOJOARIA)
# ==========================================

def criar_produto(produtos):
    """ (Create) Adiciona um novo relógio ao estoque. """
    print("\n--- CADASTRAR NOVO RELÓGIO ---")
    codigo = input("Código de identificação: ")
    nome = input("Nome do modelo: ")
    marca = input("Marca: ")
    preco = input("Preço (ex: 1500.50): ")
    qtd = input("Quantidade em estoque: ")
    
    produtos.append({'codigo': codigo, 'nome': nome, 'marca': marca, 'preco': preco, 'quantidade': qtd})
    print(f"Relógio {nome} adicionado ao estoque!")

def listar_produtos(produtos, ordem='nome'):
    """ (Read) Lista os produtos ordenados por nome ou preço. """
    if ordem == 'preco':
        # Converte o preço para float apenas na hora de ordenar
        produtos_ordenados = sorted(produtos, key=lambda x: float(x['preco']))
        titulo = "ORDENADOS POR PREÇO"
    else:
        produtos_ordenados = sorted(produtos, key=lambda x: x['nome'].lower())
        titulo = "ORDENADOS POR NOME"
        
    print(f"\n--- CATÁLOGO DE RELÓGIOS ({titulo}) ---")
    for p in produtos_ordenados:
        print(f"[{p['codigo']}] {p['marca']} {p['nome']} | R$ {float(p['preco']):.2f} | Estoque: {p['quantidade']}")

def buscar_produto(produtos):
    """ (Read) Busca um relógio específico por nome ou código. """
    print("\n--- BUSCAR RELÓGIO ---")
    termo = input("Digite o nome ou código do relógio: ").lower()
    
    encontrados = []
    for p in produtos:
        if termo == p['codigo'].lower() or termo in p['nome'].lower():
            encontrados.append(p)
            
    if encontrados:
        print("\nResultados encontrados:")
        for p in encontrados:
             print(f"[{p['codigo']}] {p['marca']} {p['nome']} - R$ {p['preco']}")
    else:
        print("Nenhum relógio encontrado com esse termo.")

def atualizar_produto(produtos):
    """ (Update) Atualiza preço e estoque de um relógio. """
    print("\n--- ATUALIZAR ESTOQUE/PREÇO ---")
    codigo = input("Digite o código do relógio: ")
    
    for p in produtos:
        if p['codigo'] == codigo:
            novo_preco = input(f"Novo preço (Atual: R$ {p['preco']}): ")
            nova_qtd = input(f"Nova quantidade (Atual: {p['quantidade']}): ")
            
            if novo_preco: p['preco'] = novo_preco
            if nova_qtd: p['quantidade'] = nova_qtd
            print("Produto atualizado!")
            return
    print("Produto não encontrado.")

def deletar_produto(produtos):
    """ (Delete) Remove um relógio do sistema. """
    print("\n--- REMOVER RELÓGIO ---")
    codigo = input("Digite o código do produto a ser removido: ")
    
    for i in range(len(produtos)):
        if produtos[i]['codigo'] == codigo:
            removido = produtos.pop(i)
            print(f"Relógio '{removido['nome']}' removido do sistema.")
            return
    print("Produto não encontrado.")

# ==========================================
# 4. MENUS E SISTEMA PRINCIPAL
# ==========================================

def menu_gerente(usuarios, produtos):
    """ Menu com acesso total (Gerente). """
    while True:
        print("\n=== PAINEL DO GERENTE ===")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Editar Usuário")
        print("4. Excluir Usuário")
        print("5. Cadastrar Relógio")
        print("6. Atualizar Relógio (Preço/Estoque)")
        print("7. Excluir Relógio")
        print("0. Sair e Salvar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': criar_usuario(usuarios)
        elif opcao == '2': listar_usuarios(usuarios)
        elif opcao == '3': atualizar_usuario(usuarios)
        elif opcao == '4': deletar_usuario(usuarios)
        elif opcao == '5': criar_produto(produtos)
        elif opcao == '6': atualizar_produto(produtos)
        elif opcao == '7': deletar_produto(produtos)
        elif opcao == '0': break
        else: print("Opção inválida.")

def menu_funcionario(produtos):
    """ Menu com permissões para gestão de produtos (Vendedor). """
    while True:
        print("\n=== PAINEL DO VENDEDOR ===")
        print("1. Listar Relógios (Por Nome)")
        print("2. Listar Relógios (Por Preço)")
        print("3. Buscar Relógio")
        print("4. Cadastrar Relógio")
        print("5. Atualizar Estoque")
        print("0. Sair e Salvar")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': listar_produtos(produtos, 'nome')
        elif opcao == '2': listar_produtos(produtos, 'preco')
        elif opcao == '3': buscar_produto(produtos)
        elif opcao == '4': criar_produto(produtos)
        elif opcao == '5': atualizar_produto(produtos)
        elif opcao == '0': break
        else: print("Opção inválida.")

def menu_cliente(produtos):
    """ Menu restrito para leitura (Cliente). """
    while True:
        print("\n=== VITRINE DA RELOJOARIA ===")
        print("1. Ver catálogo por ordem alfabética")
        print("2. Ver catálogo do mais barato ao mais caro")
        print("3. Buscar relógio específico")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': listar_produtos(produtos, 'nome')
        elif opcao == '2': listar_produtos(produtos, 'preco')
        elif opcao == '3': buscar_produto(produtos)
        elif opcao == '0': break
        else: print("Opção inválida.")

def main():
    """ Função principal que controla o fluxo de login e navegação. """
    print("Iniciando Sistema da Relojoaria ChronoMaster...")
    
    # Carregamento de dados para as Estruturas de Dados (Listas de Dicionários)
    usuarios = carregar_dados('usuarios.csv')
    produtos = carregar_dados('produtos.csv')
    
    usuario_logado = None
    
    # Estrutura de Repetição e Condicional para Login
    while not usuario_logado:
        print("\n--- LOGIN ---")
        login = input("Usuário: ")
        senha = input("Senha: ")
        
        for u in usuarios:
            if u['login'] == login and u['senha'] == senha:
                usuario_logado = u
                break
                
        if not usuario_logado:
            print("Acesso negado. Verifique suas credenciais.")
            
    print(f"\nBem-vindo(a), {usuario_logado['login']}!")
    
    # Redirecionamento baseado no nível de permissão
    if usuario_logado['perfil'] == 'gerente':
        menu_gerente(usuarios, produtos)
    elif usuario_logado['perfil'] == 'funcionario':
        menu_funcionario(produtos)
    elif usuario_logado['perfil'] == 'cliente':
        menu_cliente(produtos)
        
    # Quando o usuário escolhe '0' para sair, o fluxo chega aqui e salva os arquivos.
    print("\nSalvando alterações no banco de dados...")
    salvar_dados('usuarios.csv', ['login', 'senha', 'perfil'], usuarios)
    salvar_dados('produtos.csv', ['codigo', 'nome', 'marca', 'preco', 'quantidade'], produtos)
    print("Sistema encerrado. Até logo!")

if __name__ == "__main__":
    main()