# Dicionário básico de sentimentos
dicionario = {
    "feliz": "positivo", "triste": "negativo", "bom": "positivo", "ruim": "negativo"}

# Função para análise de sentimento
def analise_sentimento(texto):
    palavras = texto.lower().split()
    sentimentos = [dicionario.get(palavra) for palavra in palavras]
    if "negativo" in sentimentos:
        return "negativo"
    else:
        return "positivo"

# Teste com textos de exemplo
textos = ["Estou muito feliz hoje", "O dia está ruim"]
resultados = [analise_sentimento(texto) for texto in textos]

# Exibindo o resultado
import pandas as pd
df = pd.DataFrame({"Texto": textos, "Sentimento": resultados})
print(df)
