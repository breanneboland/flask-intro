

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    Hi! This is the home page.
    <p>Will it run an additional line?</p>
    <a href="/hello">Let's chat!</a>
    """

    # return "Does this appear?"

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet" method="post">
                <label>What's your name? <input type="text" name="person"></label>
                <label>Pick your greeting: <select name ="compliment">
                    <option value="awesome">Awesome</option>
                    <option value="terrific">Terrific</option>
                    <option value="fantastic">Fantastic</option>
                    <option value="neato">Neato</option>
                    <option value="wowza">Wowza</option>
                </select>
            <input type="submit">
            
            <form action="/diss" method="post">
                <label>Pick your greeting: <select name ="terrible_word">
                    <option value="terrible">terrible</option>
                    <option value="a-player">a player</option>
                    <option value="dumb">dumb</option>
                    <option value="elderberries">Smell of elderberries</option>
                    <option value="glittery">Curiously covered in glitter</option> 
                </select>
                <input type="submit">
            </form>
        </body>
    </html>

    """

@app.route('/greet', methods=["POST"])
def greet_person():
    player = request.form.get("person")
    compliment = request.form.get("compliment")

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = request.args("compliment")

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, compliment)

@app.route('/diss', methods=["POST"])
def greet_person2():
    player = request.form.get("person")
    diss = request.form.get("terrible_word")

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s I think you're %s!
        </body>
    </html>""" % (player, diss)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
