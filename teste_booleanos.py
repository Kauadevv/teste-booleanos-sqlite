import sqlite3
import time

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

# inserir dados para teste
print("Inserindo dados...")
start = time.time()
cursor.execute('DELETE FROM teste_booleans')  # limpando a tabela antes
conn.commit()

#inserindo dados em batch
batch_size = 10000
for i in range(1, 1000001):
    status_texto = 'Sim' if i % 2 == 0 else 'Não'
    status_booleano = 1 if i % 2 == 0 else 0
    cursor.execute('INSERT INTO teste_booleans (status_texto, status_booleano) VALUES (?, ?)',
                   (status_texto, status_booleano))

    if i % batch_size == 0:
        conn.commit()
        print(f"{i} registros inseridos...")

conn.commit()
print(f"Dados inseridos em {time.time() - start:.2f} segundos.")

# Testando consulta com texto
start = time.time()
cursor.execute("SELECT COUNT(*) FROM teste_booleans WHERE status_texto = 'Sim'")
resultado_texto = cursor.fetchone()[0]
print(f"Consulta texto: {resultado_texto} registros encontrados em {time.time() - start:.4f} segundos.")

# Testando consulta com booleano
start = time.time()
cursor.execute("SELECT COUNT(*) FROM teste_booleans WHERE status_booleano = 1")
resultado_bool = cursor.fetchone()[0]
print(f"Consulta booleano: {resultado_bool} registros encontrados em {time.time() - start:.4f} segundos.")

conn.close()
