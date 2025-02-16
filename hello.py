from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center" >Pentru Gabriela. </h1>'\
            '<p>This is a pharagraph.</p>'\
             '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeG4xaWVmcmNsazF4MDk2am8yMTU5czNpcjk3MWNtMnNnZjNpb2g4YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif" width=400px>'\
            '< style="text-align: center"img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmNoZ3Q3cDVhazNpcnN2bzlyZ21zMGc4eGduOXFtY3RkOXBjNzZraiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iGqP4DYXe4zVJbCY5N/giphy.gif">'


# noinspection PyUnresolvedReferences
@app.route("/bye")

def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
  return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)