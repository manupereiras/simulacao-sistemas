from PIL import Image  # Biblioteca Pillow para manipular imagens

# Define o modo inicial (usuário por padrão)
modo = "usuario"

# Funções específicas para o modo Kernel
def comando_kernel(comando):
    if comando == "gerenciar_memoria":
        print("Simulando gerenciamento de memória no modo Kernel...")
    elif comando == "acessar_hardware":
        print("Simulando acesso direto ao hardware no modo Kernel...")
    elif comando == "configurar_dispositivo":
        print("Simulando configuração de dispositivos no modo Kernel...")
    else:
        print("Comando inválido para o modo Kernel.")

# Funções específicas para o modo Usuário
def comando_usuario(comando):
    if comando == "abrir_arquivo":
        try:
            # Caminho para o arquivo de imagem
            caminho_completo = "C:/Users/55619/Pictures/naruto.jpg"

            # Abre a imagem
            imagem = Image.open(caminho_completo)
            imagem.show()  # Mostra a imagem no visualizador padrão
            print("Imagem 'naruto.jpg' foi aberta com sucesso!")
        except FileNotFoundError:
            print("Erro: O arquivo 'naruto.jpg' não foi encontrado na pasta 'Pictures'.")
        except Exception as e:
            print(f"Erro ao abrir o arquivo: {e}")
    elif comando == "executar_programa":
        print("Simulando execução de programa no modo Usuário...")
    elif comando == "editar_arquivo":
        try:
            # Simula edição de um arquivo de texto
            nome_arquivo = "arquivo_simulado.txt"
            with open(nome_arquivo, "w") as arquivo:
                arquivo.write("Conteúdo editado no modo Usuário.\n")
            print(f"Arquivo '{nome_arquivo}' foi editado com sucesso!")
        except Exception as e:
            print(f"Erro ao editar o arquivo: {e}")
    else:
        print("Comando inválido para o modo Usuário.")

# Função para alternar modos
def trap():
    global modo
    if modo == "usuario":
        print("Alternando para o modo Kernel...")
        modo = "kernel"
    else:
        print("Alternando para o modo Usuário...")
        modo = "usuario"
    print(f"Modo atual: {modo}")

# Loop principal para interação
def main():
    global modo
    print("Bem-vindo à simulação de um sistema operacional!")
    print("Modo atual:", modo)

    while True:
        print("\nEscolha uma opção:")
        print("1 - Executar comando")
        print("2 - Alternar modo (TRAP)")
        print("3 - Sair")
        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            comando = input(f"Digite um comando para o modo {modo}: ")
            if modo == "usuario":
                comando_usuario(comando)
            elif modo == "kernel":
                comando_kernel(comando)
        elif escolha == "2":
            trap()
        elif escolha == "3":
            print("Encerrando a simulação...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
