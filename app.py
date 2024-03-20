from flask import Flask , render_template
import random 

app = Flask(__name__)

number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
mixNumber = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
random.shuffle(mixNumber)

print(mixNumber)
x=0
rInt = number[x]
@app.route("/")
def index():
	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24], locate = rInt)

@app.route("/f1" , methods = ["POST"])
def box1():
	global rInt
	global x
	if mixNumber[0] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f2" , methods = ["POST"])
def box2():
	global rInt
	global x
	if mixNumber[1] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f3" , methods = ["POST"])
def box3():
	global rInt
	global x
	if mixNumber[2] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f4" , methods = ["POST"])
def box4():
	global rInt
	global x
	if mixNumber[3] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f5" , methods = ["POST"])
def box5():
	global rInt
	global x
	if mixNumber[4] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f6" , methods = ["POST"])
def box6():
	global rInt
	global x
	if mixNumber[5] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f7" , methods = ["POST"])
def box7():
	global rInt
	global x
	if mixNumber[6] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)


@app.route("/f8" , methods = ["POST"])
def box8():
	global rInt
	global x
	if mixNumber[7] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)


@app.route("/f9" , methods = ["POST"])
def box9():
	global rInt
	global x
	if mixNumber[8] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)


@app.route("/f10" , methods = ["POST"])
def box10():
	global rInt
	global x
	if mixNumber[9] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f11" , methods = ["POST"])
def box11():
	global rInt
	global x
	if mixNumber[10] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)


@app.route("/f12" , methods = ["POST"])
def box12():
	global rInt
	global x
	if mixNumber[11] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)


@app.route("/f13" , methods = ["POST"])
def box13():
	global rInt
	global x
	if mixNumber[12] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f14" , methods = ["POST"])
def box14():
	global rInt
	global x
	if mixNumber[13] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f15" , methods = ["POST"])
def box15():
	global rInt
	global x
	if mixNumber[14] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f16" , methods = ["POST"])
def box16():
	global rInt
	global x
	if mixNumber[15] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f17" , methods = ["POST"])
def box17():
	global rInt
	global x
	if mixNumber[16] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f18" , methods = ["POST"])
def box18():
	global rInt
	global x
	if mixNumber[17] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f19" , methods = ["POST"])
def box19():
	global rInt
	global x
	if mixNumber[18] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)


@app.route("/f20" , methods = ["POST"])
def box20():
	global rInt
	global x
	if mixNumber[19] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)


@app.route("/f21" , methods = ["POST"])
def box21():
	global rInt
	global x
	if mixNumber[20] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)


@app.route("/f22" , methods = ["POST"])
def box22():
	global rInt
	global x
	if mixNumber[21] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)


@app.route("/f23" , methods = ["POST"])
def box23():
	global rInt
	global x
	if mixNumber[22] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f24" , methods = ["POST"])
def box24():
	global rInt
	global x
	if mixNumber[23] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)

@app.route("/f25" , methods = ["POST"])
def box25():
	global rInt
	global x
	if mixNumber[24] == rInt:
		if x<24:
			x+=1
			rInt = number[x]
			print(number[x])
		else:
			rInt = "Completed"
		

	return render_template('main.html' , N1 = mixNumber[0],N2= mixNumber[1],N3 = mixNumber[2],N4 = mixNumber[3],N5 = mixNumber[4]
		,N6 = mixNumber[5],N7 = mixNumber[6],N8 = mixNumber[7],N9 = mixNumber[8],N10 = mixNumber[9],N11 = mixNumber[10],N12 = mixNumber[11]
		,N13 = mixNumber[12],N14 = mixNumber[13],N15 = mixNumber[14],N16 = mixNumber[15],N17 = mixNumber[16],N18 = mixNumber[17],N19 = mixNumber[18]
		,N20 = mixNumber[19],N21 = mixNumber[20],N22 = mixNumber[21],N23 = mixNumber[22],N24 = mixNumber[23],N25 = mixNumber[24],locate= rInt)


if __name__ == "__main__":
	app.run(port=5001)
