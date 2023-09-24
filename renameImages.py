import os

# Defina o diretório on\de estão os arquivos que você deseja renomear
diretorio = 'C:\\Users\\f4bri\\Desktop\\birds\\dataset\\Zonotrichia_capensis'

# Solicite ao usuário os números inicial e final
numero_inicial = int(input("Digite o número inicial: "))
numero_final = int(input("Digite o número final: "))

# Garanta que o número final seja maior ou igual ao número inicial
if numero_final < numero_inicial:
    print("O número final deve ser maior ou igual ao número inicial.")
else:
    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio)
    
    # Loop pelos arquivos e renomeia com os números escolhidos
    for i, arquivo in enumerate(arquivos):
        novo_nome = f"{numero_inicial + i}{os.path.splitext(arquivo)[1]}"
        caminho_atual = os.path.join(diretorio, arquivo)
        novo_caminho = os.path.join(diretorio, novo_nome)
        os.rename(caminho_atual, novo_caminho)
    
    print("Renomeação concluída com sucesso!")
