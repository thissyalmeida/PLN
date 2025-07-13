import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Dados de exemplo (inglês → português)
entradas = ['cat', 'dog', 'house', 'water']
saidas = ['gato', 'cachorro', 'casa', 'água']

# Codificação simples (cada palavra vira um número)
entrada_dict = {palavra: i for i, palavra in enumerate(entradas)}
saida_dict = {palavra: i for i, palavra in enumerate(saidas)}
saida_dict_inv = {i: palavra for palavra, i in saida_dict.items()}

X = np.array([entrada_dict[p] for p in entradas])
y = to_categorical([saida_dict[p] for p in saidas])

# Modelo neural simples
modelo = Sequential()
modelo.add(Dense(10, input_shape=(1,), activation='relu'))
modelo.add(Dense(len(saidas), activation='softmax'))

modelo.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
modelo.fit(X, y, epochs=300, verbose=0)

# Função de tradução
def traduzir(palavra):
    if palavra not in entrada_dict:
        return "Palavra não conhecida"
    entrada = np.array([entrada_dict[palavra]])
    pred = modelo.predict(entrada, verbose=0)
    indice = np.argmax(pred)
    return saida_dict_inv[indice]

# Testes
print(traduzir('cat'))    # gato
print(traduzir('water'))    # agua