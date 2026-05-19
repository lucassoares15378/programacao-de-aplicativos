import json
import os

# Descobre a pasta onde o script atual está salvo
pasta_do_script = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta_do_script, "notas.json")

# Abre e lê o arquivo JSON usando o caminho correto
with open(caminho_json, "r", encoding="utf-8") as arquivo:
    notas = json.load(arquivo)

# Soma das notas
soma = notas.get("matemática", 0) + notas.get("portugues", 0)

# Exibe o resultado
print("Soma das notas:", soma)