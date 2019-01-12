from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

request_counter = {}


@app.route('/')
def route_index():
    return render_template('index.html')


@app.route('/request-counter', methods=['GET', 'POST', 'PUT', 'DELETE'])
def route_count():
    global request_counter
    if request.method in request_counter:
        request_counter[request.method] += 1
    else:
        request_counter[request.method] = 1
    return redirect(url_for('route_index'))


@app.route('/statistics')
def route_stat():
    global request_counter
    return render_template('statistics.html', counter=request_counter)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
