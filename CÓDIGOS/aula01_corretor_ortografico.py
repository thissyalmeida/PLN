# Dicionário básico com palavras conhecidas
dictionary = ["hello", "world", "python", "programming", "language"]

# Função simples de corretor ortográfico
def spell_checker(word):
   if word in dictionary:
       return f"{word} está correto!"
   else:
       return f"{word} está incorreto. Verifique a ortografia."

# Teste do corretor
print(spell_checker("python"))       #Correta
print(spell_checker("progrmming"))   #Incorreta
