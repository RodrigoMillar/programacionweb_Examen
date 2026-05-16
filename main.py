from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Ejercicio 1 Calculo de Compras

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = int(request.form.get('edad', 0))
        cantidad = int(request.form.get('cantidad', 0))

        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro

        if 18 <= edad <= 30:
            porcentaje_descuento = 15
        elif edad > 30:
            porcentaje_descuento = 25
        else:
            porcentaje_descuento = 0

        valor_descuento = total_sin_descuento * (porcentaje_descuento / 100)
        total_pagar = total_sin_descuento - valor_descuento

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': int(total_sin_descuento),
            'monto_descuento': int(valor_descuento),
            'total_pagar': int(total_pagar)
        }

    return render_template('ejercicio1.html', resultado=resultado)



# Ejercicio 2 Inicio de Sesion

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    es_valido = False

    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contrasena = request.form.get('contrasena')

        # Validacion de los usuarios segun el usuario
        if usuario == "juan" and contrasena == "admin":
            mensaje = "Bienvenido administrador juan"
            es_valido = True
        elif usuario == "pepe" and contrasena == "user":
            mensaje = "Bienvenido usuario pepe"
            es_valido = True
        else:
            mensaje = "Usuario o contraseña incorrectos"
            es_valido = False

    return render_template('ejercicio2.html', mensaje=mensaje, es_valido=es_valido)


if __name__ == '__main__':
    app.run(debug=True)