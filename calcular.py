#Nosso objetivo é fazer uma calculadora em que o usuário coloca dois números (x e y), sendo com ou sem vírgula, que gere o resultado da equação "z = (x² + y²)/(x-y)²".
#Lembrando que: Deverá funcionar mesmo que x e y sejam os mesmos números.

print("Coloque números x e y para resolver a equação z = (x² + y²)/(x-y)²:")
x = float(input("coloque o valor de x:"))
y = float(input("coloque o valor de y:"))
if x==y:
  print ("Essa equação não pode ser executada!")
valor3 = (x-y)**2
valor4 = (x**2 + y**2)
if x!=y:
 print(float(x**2 + y**2)/(x-y)**2)