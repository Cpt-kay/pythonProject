# This is a sample Python script.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_news():
    # Use a breakpoint in the code line below to debug your script.
    return "No news is good news"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=5000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
