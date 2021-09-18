from flask import Flask, render_template, request, redirect, jsonify
from json import dump
from Gameboard import Gameboard
import db


app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

game = Gameboard()

'''
Implement '/' endpoint
Method Type: GET
return: template player1_connect.html and status = "Pick a Color."
Initial Webpage where gameboard is initialized
'''


@app.route('/', methods=['GET'])
def player1_connect():
    return render_template("player1_connect.html", status="Pick a Color.")


'''
Helper function that sends to all boards don't modify
'''


@app.route('/autoUpdate', methods=['GET'])
def updateAllBoards():
    try:
        return jsonify(move=game.board, winner=game.game_result,
                       color=game.player1)
    except Exception:
        return jsonify(move="")


'''
Implement '/p1Color' endpoint
Method Type: GET
return: template player1_connect.html and status = <Color picked>
Assign player1 their color
'''


@app.route('/p1Color', methods=['GET'])
def player1_config():
    game.player1 = request.args.get('color')
    return render_template("player1_connect.html", status=game.player1)


'''
Implement '/p2Join' endpoint
Method Type: GET
return: template p2Join.html and status = <Color picked> or Error
if P1 didn't pick color first

Assign player2 their color
'''


@app.route('/p2Join', methods=['GET'])
def p2Join():
    if game.player1 == "red":
        game.player2 = "yellow"
        return render_template("p2Join.html", status=game.player2)
    elif game.player1 == "yellow":
        game.player2 = "red"
        return render_template("p2Join.html", status=game.player2)
    else:
        return render_template("p2Join.html", status="Error")
'''
Implement '/move1' endpoint
Method Type: POST
return: jsonify (move=<CurrentBoard>,
invalid=True or False, winner = <currWinner>)
If move is valid --> invalid = False else invalid = True
If invalid == True, also return reason= <Why Move is Invalid>

Process Player 1's move
'''


@app.route('/move1', methods=['POST'])
def p1_move():
    move = request.get_json(force=True)
    Invalid = True
    Reason = game.validateP1Move(move)
    if len(Reason) < 1:
        Invalid  = False
    return jsonify(move=game.board, invalid=Invalid, reason = Reason, winner=game.game_result)
'''
Same as '/move1' but instead proccess Player 2
'''


@app.route('/move2', methods=['POST'])
def p2_move():
    move = request.get_json(force=True)
    Invalid = True
    Reason = game.validateP2Move(move)
    if len(Reason) < 1:
        Invalid  = False
    return jsonify(move=game.board, invalid=Invalid, reason = Reason, winner=game.game_result)



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')