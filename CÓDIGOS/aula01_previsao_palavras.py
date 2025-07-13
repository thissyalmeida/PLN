import pandas as pd
from collections import Counter

# Pequeno corpus como exemplo
corpus = ["o gato está dormindo", "o cachorro está latindo", "o gato está correndo"]

# Tokenizar e gerar bigramas
words = []
for sentence in corpus:
    tks = sentence.split()
    words.extend([(tks[i], tks[i + 1]) for i in range(len(tks) - 1)])

# Criar um DataFrame com os pares de bigramas
df = pd.DataFrame(words, columns=["word", "next"])

# Contar frequência dos bigramas
bi_cnt = df.groupby(["word", "next"]).size().reset_index(name='count')

# Função para prever a próxima palavra
def predict_next_word(word):
    cand = bi_cnt[bi_cnt['word'] == word]
    if cand.empty:
        return "Nenhuma sugestão encontrada."
    else:
        sorted_cand = cand.sort_values(by='count', ascending=False)
        return sorted_cand.iloc[0]['next']

# Testando a previsão
print(predict_next_word("o"))       # Deve sugerir "gato"
print(predict_next_word("gato"))    # Deve sugerir "está"
