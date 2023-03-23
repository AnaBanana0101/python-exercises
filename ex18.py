# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


tamanho_arquivo = float(input("Digite o tamanho do arquivo para download: "))
velocidade = float(input("Digite a velocidade de um link de internet: "))

segs = tamanho_arquivo/velocidade
mins = int(segs/60)
segs = segs%60


print(f"Tempo aproximado para o download é de {mins} minutos e {segs} segundos.")