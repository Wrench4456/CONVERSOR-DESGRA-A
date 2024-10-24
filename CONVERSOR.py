def converter():
    print("Bem-vindo ao conversor de unidades!")
    
    # Dicionário de conversões
    conversoes = {
        'km_milhas': 0.621371,
        'milhas_km': 1.60934,
        'celsius_fahrenheit': lambda c: c * 9/5 + 32,
        'fahrenheit_celsius': lambda f: (f - 32) * 5/9,
        'kg_libras': 2.20462,
        'libras_kg': 0.453592
    }

    # Solicitar entrada do usuário
    valor = float(input("Digite o valor a ser convertido: "))
    unidade_origem = input("Digite a unidade de origem (km, milhas, C, F, kg, libras): ").strip().lower()
    unidade_destino = input("Digite a unidade de destino (km, milhas, C, F, kg, libras): ").strip().lower()

    # Identificar a conversão correta
    if unidade_origem == 'km' and unidade_destino == 'milhas':
        resultado = valor * conversoes['km_milhas']
        print(f"{valor} km é igual a {resultado:.2f} milhas.")
    elif unidade_origem == 'milhas' and unidade_destino == 'km':
        resultado = valor * conversoes['milhas_km']
        print(f"{valor} milhas é igual a {resultado:.2f} km.")
    elif unidade_origem == 'c' and unidade_destino == 'f':
        resultado = conversoes['celsius_fahrenheit'](valor)
        print(f"{valor}°C é igual a {resultado:.2f}°F.")
    elif unidade_origem == 'f' and unidade_destino == 'c':
        resultado = conversoes['fahrenheit_celsius'](valor)
        print(f"{valor}°F é igual a {resultado:.2f}°C.")
    elif unidade_origem == 'kg' and unidade_destino == 'libras':
        resultado = valor * conversoes['kg_libras']
        print(f"{valor} kg é igual a {resultado:.2f} libras.")
    elif unidade_origem == 'libras' and unidade_destino == 'kg':
        resultado = valor * conversoes['libras_kg']
        print(f"{valor} libras é igual a {resultado:.2f} kg.")
    else:
        print("Conversão não suportada.")

# Executar o programa
converter()
