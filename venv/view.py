from flask import render_template

def mostrar_formulario_cadastro():
    # Lógica para renderizar o formulário de cadastro
    return render_template('cadastro.html')

def mostrar_formulario_agendamento():
    # Lógica para renderizar o formulário de agendamento
    return render_template('agendamento.html')
