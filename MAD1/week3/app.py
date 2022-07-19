#package declaration
import csv
import sys
from jinja2 import Template
from csv import DictReader
import matplotlib.pyplot as plt

#Template gen

TEMPLATE = '''
<!DOCTYPE html>
<html>
    <head>
    <style>
	table, th, td {
  	border: 1px solid black;
  	
	}
	</style>
        <meta charset="UTF-8"/>
        <title> Student Details </title>
    </head>
    {% if value == "-s" %}
    <h1>Student Details</h1>
    <body>
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
                    {% for id in student_id %}
                    <tr>
                        <td>{{id["Student id"]}}</td>
                        <td>{{id[" Course id"]}}</td>
                        <td>{{id[" Marks"]}}</td>
                    </tr>
                    {% endfor %}
                    <thead>
                    	<tr>
                        	<th id="total" colspan="2">Total Marks</th>
				<td>{{total}}</td>
						</tr>
                    </thead>
                </tbody>
	</body>

	{% elif value == "-c" %}
    <h1>Course Details</h1>
	<body>
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
                        <td>{{maxi}}</td>
                    </tr>                    
                </tbody>
            </table>            
        </div>
        <img src="my_plot.png"/>
    </body>
	{% else %}
             <h1>Wrong Input</h1>
             <p>Something Went wrong</p>
    {% endif %}
</html> 
'''

def main():
	
	template = Template(TEMPLATE)
    #Read CSV
	with open("data.csv") as file:
		rows = csv.DictReader(file)
		Details = list(rows)
		print(Details)
		L = []
		maxi = 0
		Avg = 0
		countc = 0
		counts = 0
		new_Dict = []
		total = 0
		if sys.argv[1] == "-c":
			for j in Details:
				if int(sys.argv[2]) == int(j[" Course id"]):
					countc = countc +1
					L.append(int(j[" Marks"]))
			if countc <1:
				sys.argv[1] = "-x"
			else:
				print(L)
				fig = plt.hist(L)
				plt.xlabel("Marks")
				plt.ylabel("Frequency")
				plt.savefig('my_plot.png')
				maxi = max(L)
				Avg = sum(L)/len(L)
		
		if sys.argv[1] == "-s":
			new_Dict = []
			total = 0
			for i in Details:
				print(int(sys.argv[2]),i["Student id"])
				if int(sys.argv[2]) == int(i["Student id"]):
					counts = counts +1
					new_Dict.append(i)
					total =  total + int(i[" Marks"])
			print(new_Dict)
			
			if counts < 1:
				sys.argv[1] = "-x"
				
	content = template.render(student_id = new_Dict, total = total,value = sys.argv[1],maxi = maxi,avg = Avg)
	
	my_html_document_file = open('output.html','w')
	my_html_document_file.write(content)
	my_html_document_file.close()
	
if __name__ == "__main__":
	main()