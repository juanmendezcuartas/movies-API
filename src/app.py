from flask import Flask, jsonify, request
from movies import movies
import mysql.connector as mariadb

mariadb_conection = mariadb.connect(
  host='127.0.0.1',
  user='root',
  password='root',
  database='pelis',
  port='33067'
)



#cursor.execute('DELETE * FROM peliculas')
#mariadb_conection.commit()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def saludo():
  return jsonify({"message": "olis ^.^"})

@app.route('/movies', methods=['GET'])
def getMovies():
  cursor = mariadb_conection.cursor()
  cursor.execute('SELECT * FROM peliculas')
  result = cursor.fetchall()
  return jsonify({"movies":result, "message": "Movies List"})

@app.route('/movies/<int:movie_id>', methods=['GET'])
def getMovie(movie_id):
  cursor = mariadb_conection.cursor()
  cursor.execute('SELECT * FROM peliculas WHERE id= {}'.format(movie_id))
  result = cursor.fetchall()
  return jsonify({"movies":result, "message": "Movies List"})

@app.route('/movies/', methods=['POST'])
def addMovie():
  new_movie = [
    {
      "id":request.json['id'],
      "nombre": request.json['nombre'],
      "Tipo": request.json['Tipo'],
      "Estrellas": request.json['Estrellas'],
      "Precio": request.json['Precio'],
    }
  ]
  movies.append(new_movie)
  return jsonify({"message":"Movie added", "movies": movies})

@app.route('/movies/<int:movie_id>', methods=['PUT'])
def updateMovie(movie_id):
  selectedMovie = [movie for movie in movies if movie['id'] == movie_id]
  if(len(selectedMovie) > 0):
    selectedMovie[0]['id'] = request.json['id']
    selectedMovie[0]['nombre'] = request.json['nombre']
    selectedMovie[0]['Tipo'] = request.json['Tipo']
    selectedMovie[0]['Estrellas'] = request.json['Estrellas']
    selectedMovie[0]['Precio'] = request.json['Precio']
    return jsonify({"message": "Update successful", "movie":selectedMovie})
  else: 
    return jsonify({"movie": "Movie not found"})

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delMovie(movie_id):
  selectedMovie = [movie for movie in movies if movie['id'] == movie_id]
  if(len(selectedMovie) > 0):
    movies.remove(selectedMovie[0])
    return jsonify({"message": "Movie deleted", "movie": selectedMovie})
  else: 
    return jsonify({"movie": "Movie not found"})

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, port=3000)