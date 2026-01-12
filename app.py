from flask import Flask,request,render_template
import firebase_admin
from firebase_admin import credentials,db
import time

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://umang2026-440bc-default-rtdb.firebaseio.com/"})

ref = db.reference("/")
data = ref.get()

def overs():
        ref = db.reference("match/overs")
        anand = ref.get() or 0.0
        anand += 0.1
        if int((anand * 10) % 10) == 6:
            anand = int(anand) + 1.0
        ref.set(round(anand, 1))
# print(data)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('login.html')
@app.route("/a")
def a():
    return "site is working"

@app.route("/login",methods = ["GET","POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == "anand123" and password == "anand@123":
        return render_template('index.html')
    else:
        return render_template("login.html", error="Invalid user")
@app.route("/submit",methods = ["GET","POST"])
def submit():
    if request.method == "POST":
        return 'thank you for posting'
    else:
        return 'thank you'
@app.route("/6",methods=("GET","POST"))
def yy():
    if request.method == "POST":
        ref = db.reference("match/overs")
        anand = ref.get() or 0.0
        anand += 0.1
        if int((anand * 10) % 10) == 6:
            anand = int(anand) + 1.0
        ref.set(round(anand, 1))
        ref = db.reference("match/runs")
        current_runs = ref.get() or 0
        rf = db.reference("match/strikerRuns")
        currnt_runs = rf.get() or 0
        rf.set(currnt_runs + 6)
        ref.set(current_runs + 6)
        if int(db.reference("match/overs").get()) < 0:
            ooo = int(db.reference("match/overs").get())
        else :
            ooo = 1
        db.reference("match/strikeRate").set(
            int(db.reference("match/runs").get())/ooo
        )
        add_ball()
        for i in range(1, 7):
            ball_ref = db.reference(f"match/balls/ball{i}")
            if ball_ref.get() in (None, ""):
                ball_ref.set(6)
                break
        return "" , 204
    else:
        return '7'
@app.route("/4",methods=("GET","POST"))
def yn():
    if request.method == "POST":
        ref = db.reference("match/overs")
        anand = ref.get() or 0.0
        anand += 0.1
        if int((anand * 10) % 10) == 6:
            anand = int(anand) + 1.0
        ref.set(round(anand, 1))
        ref = db.reference("match/runs")
        current_runs = ref.get() or 0
        ref.set(current_runs + 4)
        rf = db.reference("match/strikerRuns")
        currnt_runs = rf.get() or 0
        rf.set(currnt_runs + 4)
        if int(db.reference("match/overs").get()) < 0:
            ooo = int(db.reference("match/overs").get())
        else :
            ooo = 1
        db.reference("match/strikeRate").set(
            int(db.reference("match/runs").get())/ooo
        )
        add_ball()
        for i in range(1, 7):
            ball_ref = db.reference(f"match/balls/ball{i}")
            if ball_ref.get() in (None, ""):
                ball_ref.set(4)
                break
        return "" , 204
    else:
        return '7'
@app.route("/2",methods=("GET","POST"))
def yhhkhkn():
    if request.method == "POST":
        ref = db.reference("match/overs")
        anand = ref.get() or 0.0
        anand += 0.1
        if int((anand * 10) % 10) == 6:
            anand = int(anand) + 1.0
        ref.set(round(anand, 1))
        ref = db.reference("match/runs")
        current_runs = ref.get() or 0
        ref.set(current_runs + 2)
        rf = db.reference("match/strikerRuns")
        currnt_runs = rf.get() or 0
        rf.set(currnt_runs + 2)
        if int(db.reference("match/overs").get()) < 0:
            ooo = int(db.reference("match/overs").get())
        else :
            ooo = 1
        db.reference("match/strikeRate").set(
            int(db.reference("match/runs").get())/ooo
        )
        add_ball()
        for i in range(1, 7):
            ball_ref = db.reference(f"match/balls/ball{i}")
            if ball_ref.get() in (None, ""):
                ball_ref.set(2)
                break
        return "" , 204
    else:
        return '7'
@app.route("/3",methods=("GET","POST"))
def yjkkjn():
    if request.method == "POST":
        ref = db.reference("match/overs")
        anand = ref.get() or 0.0
        anand += 0.1
        if int((anand * 10) % 10) == 6:
            anand = int(anand) + 1.0
        ref.set(round(anand, 1))
        ref = db.reference("match/runs")
        current_runs = ref.get() or 0
        ref.set(current_runs + 3)
        rf = db.reference("match/strikerRuns")
        currnt_runs = rf.get() or 0
        rf.set(currnt_runs + 3)
        add_ball()
        if int(db.reference("match/overs").get()) < 0:
            ooo = int(db.reference("match/overs").get())
        else :
            ooo = 1
        db.reference("match/strikeRate").set(
            int(db.reference("match/runs").get())/ooo
        )
        
        for i in range(1, 7):
            ball_ref = db.reference(f"match/balls/ball{i}")
            if ball_ref.get() in (None, ""):
                ball_ref.set(3)
                break
        change_strike()
        return "" , 204
    else:
        return '7'
@app.route("/1",methods=("GET","POST"))
def llhjg():
    if request.method == "POST":
        ref = db.reference("match/overs")
        anand = ref.get() or 0.0
        anand += 0.1
        if int((anand * 10) % 10) == 6:
            anand = int(anand) + 1.0
        ref.set(round(anand, 1))
        ref = db.reference("match/runs")
        current_runs = ref.get() or 0
        ref.set(current_runs + 1)
        rf = db.reference("match/strikerRuns")
        currnt_runs = rf.get() or 0
        rf.set(currnt_runs + 1)
        if int(db.reference("match/overs").get()) < 0:
            ooo = int(db.reference("match/overs").get())
        else :
            ooo = 1
        db.reference("match/strikeRate").set(
            int(db.reference("match/runs").get())/ooo
        )
        add_ball()
        for i in range(1, 7):
            ball_ref = db.reference(f"match/balls/ball{i}")
            if ball_ref.get() in (None, ""):
                ball_ref.set(1)
                break
        change_strike()
        return "", 204
@app.route("/0",methods=("GET","POST"))
def lljhgjhjg():
    if request.method == "POST":
        ref = db.reference("match/overs")
        anand = ref.get() or 0.0
        anand += 0.1
        if int((anand * 10) % 10) == 6:
            anand = int(anand) + 1.0
        ref.set(round(anand, 1))
        ref = db.reference("match/runs")
        current_runs = ref.get() or 0
        ref.set(current_runs + 0)
        if int(db.reference("match/overs").get()) < 0:
            ooo = int(db.reference("match/overs").get())
        else :
            ooo = 1
        db.reference("match/strikeRate").set(
            int(db.reference("match/runs").get())/ooo
        )
        for i in range(1, 7):
            ball_ref = db.reference(f"match/balls/ball{i}")
            if ball_ref.get() in (None, ""):
                ball_ref.set(0)
                break
        add_ball()
        return "", 204
@app.route("/W",methods=("GET","POST"))
def PPl():
    if request.method == "POST":
        ref = db.reference("match/overs")
        anand = ref.get() or 0.0
        anand += 0.1
        if int((anand * 10) % 10) == 6:
            anand = int(anand) + 1.0
        ref.set(round(anand, 1))
        ref = db.reference("match/wickets")
        current_runs = ref.get() or 0
        ref.set(current_runs + 1)
        db.reference("match").update({
            "striker":"",
            "strikerRuns":0,
            "strikerBalls":0
        })
        if int(db.reference("match/overs").get()) < 0:
            ooo = int(db.reference("match/overs").get())
        else :
            ooo = 1
        db.reference("match/strikeRate").set(
            int(db.reference("match/runs").get())/ooo
        )
        for i in range(1, 7):
            ball_ref = db.reference(f"match/balls/ball{i}")
            if ball_ref.get() in (None, ""):
                ball_ref.set("W")
                break
        return "",204
@app.route("/wide",methods=("GET","POST"))
def Piil():
    if request.method == "POST":
        ref = db.reference("match/runs")
        current_runs = ref.get() or 0
        ref.set(current_runs + 1)
        ref = db.reference("match/wide")
        current_runs = ref.get() or 0
        ref.set(current_runs + 1)
        if int(db.reference("match/overs").get()) < 0:
            ooo = int(db.reference("match/overs").get())
        else :
            ooo = 1
        db.reference("match/strikeRate").set(
            int(db.reference("match/runs").get())/ooo
        )
        return "",204
@app.route("/nb",methods=("GET","POST"))
def Pinnjil():
    if request.method == "POST":
        ref = db.reference("match/runs")
        current_runs = ref.get() or 0
        ref.set(current_runs + 1)
        ref = db.reference("match/noBall")
        current_runs = ref.get() or 0
        ref.set(current_runs + 1)
        if int(db.reference("match/overs").get()) < 0:
            ooo = int(db.reference("match/overs").get())
        else :
            ooo = 1
        db.reference("match/strikeRate").set(
            int(db.reference("match/runs").get())/ooo
        )
        return "",204
@app.route("/add",methods=("GET","POST"))
def ppu():
    ref = db.reference("match/runs")
    current_runs = ref.get() or 0
    ref.set(current_runs + 1)
    return "",204
@app.route("/sub",methods=("GET","POST"))
def poou():
    ref = db.reference("match/runs")
    current_runs = ref.get() or 0
    ref.set(current_runs - 1)
    return "",204
@app.route("/sav",methods=("POST","GET"))
def collect_data():
    d1=request.form.get("striker")
    d2=request.form.get("nonstriker")
    d3=request.form.get("bowler")
    set_data = db.reference("match").update({
        "striker":d1,
        "nonStriker":d2,
        "bowler":d3
    })


    return "",204
@app.route("/zero",methods=("GET","POST"))
def Pihl():
    
    p = ""
    if request.method == "POST":
        db.reference("match/balls").set({
            "ball1" : p,
            "ball2" : p,
            "ball3" : p,
            "ball4" : p,
            "ball5" : p,
            "ball6" : p
})
    return "",204
def add_ball():
    z = db.reference("match/strikerBalls")
    CHANGE = z.get() or 0
    z.set(CHANGE + 1)
@app.route("/rotate",methods=("GET","POST"))
def change_strike():
    if request.method== "POST" or "GET":
        pu = db.reference("match").get()
        if pu is None:
            db.reference("match").set({
                "strikerRuns": 0,
                "strikerBalls": 0,
                "nonStrikerRuns" : 0,
                # "nonStrikerBalls" : 0,
                "striker":"RAJU RANJAN",
                "nonStriker":"MANISH KUMAR"
            })
        else:
            db.reference("match").update({
                "strikerRuns": pu["nonStrikerRuns"],
                "strikerBalls": pu["nonStrikerBalls"],
                "nonStrikerRuns" :pu["strikerRuns"] ,
                "nonStrikerBalls" :pu["strikerBalls"] ,
                "striker" : pu["nonStriker"],
                "nonStriker":pu["striker"]
        })
    return "",204
def t1():
    return 4
def t2():
    return 6
def t3():
    return 1
def t4():
    return 2
if __name__ == "__main__":
    app.run(debug=True)
    
def plus1():
    return int(r)+1
r = db.reference("match/runs").get()
s = db.reference("match/overs").get()
t = db.reference("match/wickets").get()

print(r)
# print(s)
# print(t)
p = 6
kt=plus1()
print(kt)






# @app.route("/1", methods=["POST"])
# def ll():

#     return "", 204
