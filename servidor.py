from flask import Flask, render_template, request, redirect
import json, requests
from modulos import verificaRef as vr

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locacao')
def locacao():
    return render_template('locacao.html')

@app.route('/venda')
def venda():
    return render_template('venda.html')

@app.route('/status', methods=['POST',])
def status():
    ref = request.form['ref']
    resposta=vr.verificaRef(ref)
    return render_template('status.html', ref=ref, status=resposta)

@app.route('/listar')
def listar():
    resposta=vr.pegarRef()
    return render_template('listar.html', statuss=resposta)


app.run(host="0.0.0.0", port=5000, debug=True) 
