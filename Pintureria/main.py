from flask import Flask, render_template, request

main = Flask(__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])

        precio_tarro = 9000
        total_sin_descuento = cantidad_tarros * precio_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_aplicado = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_aplicado

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento_aplicado, total_con_descuento=total_con_descuento)

    return render_template('ejercicio1.html')

@main.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        contrasena = request.form['contrasena']

        usuarios = {'juan': 'admin', 'pepe': 'user'}

        if nombre_usuario in usuarios and usuarios[nombre_usuario] == contrasena:
            mensaje = f"Bienvenido {'Administrador' if nombre_usuario == 'juan' else 'Usuario'} {nombre_usuario}"
        else:
            mensaje = "Usuario o contraseña incorrecta"

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    main.run(debug=True)
