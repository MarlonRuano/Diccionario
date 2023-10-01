def mostrar(ingles):
    for español in ingles:
        traductor=0
        print(español,ingles[ingles]) 
traducciones = {
        "ES-EN": { "perro": "dog", "silla": "chair", "mesa": "table"},
        "EN-ES": { "dog": "perro", "chair": "silla", "table": "mesa",}
}
traductor=input("Escriba una palabra en español para traducirla al ingles:")
if traductor=="perro":
    print("si existe")
    print("dog")
if traductor=="silla":
    print("si Existe")
    print("chair")
elif traductor=="mesa":
    print("Si Existe")
    print("table")
else:
    print("No se puede traducir esta palabra.")