from flask import Flask, request, url_for
from flask import render_template
from jinja2 import Template
from matplotlib import pyplot as plt


import csv
from csv import DictReader

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def my_form_post():

	file = open('data.csv')
	read = csv.reader(file)
	header = next(read)
	rows = []
	for row in read:
		rows.append(row)

	if request.method == "GET":
		return render_template("main.html")

	elif request.method == "POST":
		ID = request.form["ID"]
		value = request.form["id_value"]

		if ID == "student_id":
			name = []
			total1 = 0
			for i in rows:
				if int(i[0]) == int(value):
					name.append(i)
					total1 = total1 = i[2]

			if total1==0:
				return render_template("error.html")

			template = '''
			<!DOCTYPE html>
			<html>
			 <head>
			     <style>
				 	table, th, td { border: 1px solid black; }
				 </style>
				 <meta charset="UTF-8"/>
				 <title> Student Details </title>
			 </head>
			 <body>
			   <h1>Enter the Details</h1>
			   <div id="main">
			    <table>            
               	 <thead>                  
                	  <tr>
                    	  <th>Student id</th>
                      	  <th>Course id</th>
                          <th>Marks</th>
                      </tr>
                 </thead>
                 <tbody>              
                    {% for id in data %}
                    <tr>
                        <td>{{id[0]}}</td>
                        <td>{{id[1]}}</td>
                        <td>{{id[2]}}</td>
                    </tr>
                    {% endfor %}

                    <thead>
                    	<tr>
                        	<th id="total" colspan="2">Total Marks</th>
							<td>{{total}}</td>
						</tr>
                    </thead>
                   </tbody>
				   </table>

				   <form>
 <input type="button" value="Go back!" onclick="history.back()">
</form>
	            </body>
				</html> '''
			result = Template(template)
			File = open("./templates/student.html","w")
			output = File.write(result.render(data=name,total=total1))
			File.close()

    	
			return render_template('student.html')
			
		else:
			L = []
			countc = 0
			name = []
			total1 = 0
			for i in rows:
				if int(i[1]) == int(value):
					name.append(i)
					total1 = total1 = i[2]

			if total1==0:
				return render_template("error.html")

			avg = 0
			n= []
			for j in name:
				avg = avg + int(j[2])
				n.append(int(i[2]))

			s = int(max(n))

			plt.hist(n)
			plt.xlabel("Marks")
			plt.ylabel("Frequency")
			
			url_for('static',filename='myplot.png')
			plt.savefig('static/myplot.png')
			Avg = avg/len(name)

			template="""
			<!DOCTYPE html>
			<html>
			 <head>
			     <style>
				 	table, th, td { border: 1px solid black; }
				 </style>
				 <meta charset="UTF-8"/>
				 <title> Course Details </title>
			 </head>
			 <body>
			   <h1>Course Details</h1>
			    <div id="main">
            	<table>
                <thead>
                  
                    <tr>
                      <th>Average Marks</th>
                      <th>Maximum Marks</th>
					</tr>
                </thead>
                <tbody>
              
                      <tr>
                        <td>{{avg}}</td>
                        <td>{{max}}</td>

                    </tr>
                    
                </tbody>


            </table>
            
        </div>
        <img src="/static/myplot.png"/>
    
				   <form>
 <input type="button" value="Go back!" onclick="history.back()">
</form>
	            </body>
				</html> 		
			
			"""

			result = Template(template)
			File = open("./templates/course.html","w")
			output = File.write(result.render(avg=Avg,max=s))
			File.close()

    	
			return render_template('course.html')
	
	else: 
		error()

def error():
	print("error")
	return render_template('error.html')
			
if __name__ == "__main__":
    app.debug = True
    app.run()
