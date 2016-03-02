from flask import Flask
app = Flask(__name__)
import random
import sys
def load_quotes():
    with open('quotes.txt', 'r') as f:
        quotes = [line.decode('utf-8').strip() for line in f.readlines()]
    return quotes

@app.route("/")
def brasky():
    quotes = load_quotes()
    index = random.randrange(0,len(quotes))
    return quotes[index]

if __name__ == "__main__":
    app.run(port=int(sys.argv[1]))
