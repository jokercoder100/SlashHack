import flask
import json
from flask import url_for, render_template, request, redirect
app = flask.Flask(__name__)
app.static_folder = 'static'


class student:
    def __init__(self, name):
        self.name = name
        self.phone = 123456789


@app.route('/', methods=['POST', 'GET'])
def login(a="True"):
    global flg
    flg = "True"
    print(a)
    return render_template('Login.html', flg=a)


@app.route('/home', methods=['POST', 'GET'])
def home():
    global s
    global flg
    labels = ["Questions Asked", "Questions Answered", "Points Scored"]
    values = [5, 3, 15]
    legend = 'My Data'
    Question_dict = {"Question1": "What is Photosynthesis?",
                     "Question2": "What is exothermic reaction?"}
    Question_ans_dict = {"Question1": ["What is the capital of India?", "New Delhi"], "Question2": [
        "What is mitochondria?", "Powerhouse of the cell"]}
    if flg == "Activated":
        return render_template('home_screen.html', user_name=s, Q=Question_dict, QA=Question_ans_dict, labels=labels, values=values, legend=legend)
    user_name = request.form.get('username', 'dummy')
    password = request.form.get('password')
    print(user_name, password)
    if password == '123':
        flg = "Activated"
        s = student(user_name)
        return render_template('home_screen.html', user_name=s, Q=Question_dict, QA=Question_ans_dict, labels=labels, values=values, legend=legend)
    else:
        return(login("False"))


@app.route('/blog', methods=['POST', 'GET'])
def blog():
    d = []
    with open(r"./flask_app/static/blog_data.txt", 'r') as f:
        d = f.readlines()
        print(d)
    return render_template("blog.html", user_name=s, blogs=d)


@app.route('/forum', methods=['POST', 'GET'])
def forum():
    # d=None
    f = open("./flask_app/static/forum_content.json", 'r')
    global d
    d = json.load(f)
    f.close()
    # print(type(d))
    # print(d)
    return render_template("forum.html", user_name=s, d=d["values"])


@app.route('/forum_ans/<idx>', methods=['POST', 'GET'])
def forum_ans(idx):
    # print("testing")
    global id
    id = idx
    da = None
    for i in d["values"]:
        if id in i['id']:
            da = i
            break
    return render_template("forum_ans.html", user_name=s, da=da)


@app.route('/forum_ans_sub', methods=['POST', 'GET'])
def forum_ans_sub():
    value = request.form.get('ans')
    for i in d["values"]:
        if id in i['id']:
            print(i)
            print(value)
            i['answer'] = value
            i['answer_ind'] = "True"
            i['ans_author'] = s.name
            json.dump(
                d, open("./flask_app/static/forum_content.json", "w"), indent=2)
            break
    return redirect(url_for('forum'))


@app.route('/leaderboard', methods=['POST', 'GET'])
def leaderboard():
    m = json.load(open("./flask_app/static/leaderboard.json", "r"))
    return render_template("leaderboard.html", user_name=s, da=m)


if __name__ == '__main__':
    global flg
    flg = "True"
    # forum()
    app.run(debug=True)
