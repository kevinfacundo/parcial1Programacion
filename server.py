# IMPORTAMOS LIBRERIAS

from flask import Flask, render_template
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

# LEVANTAMOS SERVIDOR

app = Flask(__name__)

app= Flask (__name__, static_url_path= '/static')

# CONEXION MYSQL

app.config ['MYSQL_HOST']= os.getenv('MYSQL_HOST')
app.config ['MYSQL_USER']= os.getenv('MYSQL_USER')
app.config ['MYSQL_PASSWORD']= os.getenv('MYSQL_PASSWORD')
app.config ['MYSQL_DB']= os.getenv('MYSQL_DB')

mysql= MySQL (app)

# RUTAS

# API WEB
@app.route ('/data')
def data ():
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data= cur.fetchall()
    return render_template ('index.html', usuarios= data)


""" @app.route ('/json')
def json ():
    data= {
        'name':'Pepe'
        'surname: ''Argento'
    }
    return data """

@app.route ('/read')
def read ():
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data= cur.fetchall()
    return (data)


@app.route ('/')
def index ():
    return render_template ('index.html')

@app.route ('/login')
def login ():
    return render_template ('login.html')

@app.route ('/register')
def register ():
    return render_template ('register.html')


if __name__ == '__main__':
    app.run(port=5000, debug= True)


    
'''
@app.route ('/read')
def read ():
    cur= mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    data= cur.fetchall()
    return jsonify(data)



# API
@app.route ('/add', methods= ['POST'])# create prueba con json
def add ():
    datos= request.get_json()#para trabajar con templates request.method == 'POST'
    print(datos)
    fullname = datos.get('fullname')
    phone = datos.get('phone')
    email = datos.get('email')


    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO usuarios (fullname , phone, email) VALUES (%,%,%)', {fullname, phone, email} )
    mysql.connection.commit()
    return 'datos guardados'
'''





""" clase 10/5: crear la ruta para el delete de la db """



""" @app.route('/deleted/<string:id>')
def delete(id):
    cur =mysql.connection.cursor()
    cur.execute('DELETE FROM vino_en_mi_ciudad WHERE id = {0} .format(id)')
    mysql.connection.commit()
    print (id)
    flash('Contacto eliminado')
    return redirect (url_for('index'))
"""

""" importar flash y redirect

        from  flask import flash, redirect
"""