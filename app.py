import bottle
import pypeline

db = pypeline.DB("/tmp/web_lookup")
app = application = bottle.Bottle()

@app.route('/put',method='GET')
def put():
        key = bottle.request.query["k"]
        value = bottle.request.query["v"].strip()
        db.collection('%s').append('%s') % (key,value)
        return "OK"

@app.route('/delete',method='GET')
def delete():
        key = bottle.request.query["k"]
	db.delete(key)
        return "OK"

@app.route('/get',method='GET')
def get():
        key = bottle.request.query["k"]
        values =  [record for record in db.collection(key)]
        return " ".join (values)

if __name__ == '__main__':
    bottle.run(app=app,
        host='0.0.0.0',
        port=8080)
