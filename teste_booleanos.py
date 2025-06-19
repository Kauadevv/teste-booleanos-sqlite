import sqlite3
import time
import matplotlib.pyplot as plt

# Conectar (ou criar) banco local SQLite
conn = sqlite3.connect('teste_booleans.db')
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS teste_booleans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status_texto TEXT,
    status_booleano BOOLEAN
)
''')

# Inserir dados para teste
print("Inserindo dados...")
start_insercao = time.time()

cursor.execute('DELETE FROM teste_booleans')  # limpando a tabela antes
conn.commit()

batch_size = 10000
for i in range(1, 1000001):
    status_texto = 'Sim' if i % 2 == 0 else 'Não'
    status_booleano = 1 if i % 2 == 0 else 0
    cursor.execute('INSERT INTO teste_booleans (status_texto, status_booleano) VALUES (?, ?)',
                   (status_texto, status_booleano))

    if i % batch_size == 0:
        conn.commit()
        #print(f"{i} registros inseridos...")

conn.commit()
print(f"Dados inseridos em {time.time() - start_insercao:.2f} segundos.")

# Testando consulta com texto
start_texto = time.time()
cursor.execute("SELECT COUNT(*) FROM teste_booleans WHERE status_texto = 'Sim'")
resultado_texto = cursor.fetchone()[0]
tempo_texto = time.time() - start_texto
#print(f"Consulta texto: {resultado_texto} registros encontrados em {tempo_texto:.4f} segundos.")

# Testando consulta com booleano
start_bool = time.time()
cursor.execute("SELECT COUNT(*) FROM teste_booleans WHERE status_booleano = 1")
resultado_bool = cursor.fetchone()[0]
tempo_bool = time.time() - start_bool
#print(f"Consulta booleano: {resultado_bool} registros encontrados em {tempo_bool:.4f} segundos.")

conn.close()

print("Criando visualização")

# Criar gráfico de barras com os tempos reais medidos
tempos = [tempo_texto, tempo_bool]
labels = ['Consulta Texto (Sim ou Não)', 'Consulta Booleano (TRUE or FALSE)']

plt.figure(figsize=(8,5))
bars = plt.bar(labels, tempos, color=['#1f77b4', '#ff7f0e'])

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
