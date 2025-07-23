linguagens = {"Python", "JavaScript", "C#"} # Cria o conjunto linguagens

print(linguagens) # Retorna {"Python", "JavaScript", "C#"}

linguagens.add("GoLang") # Adiciona GoLang ao Conjunto

print(linguagens) # Retorna {'C#', 'GoLang', 'JavaScript', 'Python'}

linguagens.remove("C#") # Remove C# do Conjunto

print(linguagens) # Retorna {'Python', 'GoLang', 'JavaScript'}

if "Python" in linguagens:
    print("Python está nos conjunto!") # Retorna Python está no conjunto!

if "C#" not in linguagens:
    print("C# não está no conjunto!") # Válido, C# não está no conjunto.
