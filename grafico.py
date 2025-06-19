import matplotlib.pyplot as plt

# Tempos em segundos (exemplo baseado no que você me falou)
tempos = [0.0708, 0.0688]
labels = ['Consulta Texto ("Sim")', 'Consulta Booleano (TRUE)']

# Criar gráfico de barras
plt.figure(figsize=(8,5))
bars = plt.bar(labels, tempos, color=['#1f77b4', '#ff7f0e'])

# Adicionar valores no topo das barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.002, f'{yval:.4f} s', ha='center', fontsize=12)

plt.title('Comparação de tempo entre consultas com texto e booleano')
plt.ylabel('Tempo (segundos)')
plt.ylim(0, max(tempos) + 0.02)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('comparacao_consultas.png')
plt.show()
