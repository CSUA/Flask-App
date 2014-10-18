import os

from flask import Flask, render_template, send_file
from HogOnline import HogOnline

hog = HogOnline()
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("play.html")
  
@app.route('/js/<path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return send_file(os.path.join('js', path))

@app.route('/join/<name>')
def join(name):
    return hog.GetEmptyGame(name)

@app.route('/play/<game>/<player_id>/<dice>')
def make_move(game,player_id,dice):
    return hog.RollDice(game, player_id, dice)

@app.route('/status/<game>')
def game_status(game):
    return hog.GameStatus(game)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
