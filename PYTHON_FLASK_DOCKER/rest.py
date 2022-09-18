from app import app
from flask import jsonify, request

@app.route('/perrito')
def helloPerrito():
        resp = jsonify({'perrito':'guau guau!'})
        resp.status_code = 200
        app.logger.info('logged perrito')
        return resp

@app.route('/gatito')
def helloGatito():
        resp = jsonify({'gatito':'miau miau!'})
        resp.status_code = 200
        app.logger.info('logged gatito')
        return resp

@app.route('/error')
def helloError():
        resp = jsonify({'animal':'error'})
        resp.status_code = 400
        app.logger.error('logged error')
        return resp

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
