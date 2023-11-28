nome = "Débora"

mensagem = f'''
    Olá meu nome é {nome},
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.
'''

print(mensagem)


menu = "MENU"

print(f"""
    {menu.center(35, "=")}
      
      1- Depositar
      2- Sacar
      0- Saar
      
    {menu.center(35, "=")}
    Obrigado por usar nosso sistema!!!
""")