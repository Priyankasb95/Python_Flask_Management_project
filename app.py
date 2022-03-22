'''
===================================
TODO LIST APPLICATION-FLASK PROJECT
http://127.0.0.1:5000/
===================================
'''
from flask import Flask,render_template,request,redirect
import pymysql

app=Flask(__name__)  #object app of Flask is created.


@app.route('/')

def index():

      try:
         db=pymysql.connect(host="localhost",user="root",password="",db="todolist")
         cu=db.cursor()
         sql="select * from task"
         cu.execute(sql)
         data=cu.fetchall()
         
         return render_template('dashboard.html',d=data)
         #return "Success" 
         
      except Exception:
      
         return "Error"

      
      #return render_template('dashboard.html')
      
       
#task route

@app.route('/task')

def create_task():

      return render_template('task.html') 
      
#store route
@app.route('/store',methods=['POST','GET'])

def store():

      t=request.form['title']
      det=request.form['details']
      dt=request.form['date']
      
      try:
         db=pymysql.connect(host="localhost",user="root",password="",db="todolist")
         
         cu=db.cursor()
         sql="insert into task(title,details,date)values('{}','{}','{}')".format(t,det,dt)
         cu.execute(sql)
         db.commit()
      
         #return "data inserted into table"
         return redirect ('/')
         
         
      except Exception:
         db.rollback()
         return "Error"
      

#delete operation
@app.route('/delete/<rid>')

def delete(rid):

      try:
         db=pymysql.connect(host="localhost",user="root",password="",db="todolist")
      
         cu=db.cursor()
         sql="delete from task where id={}".format(rid)
         cu.execute(sql)
         db.commit()
      
         
         return redirect ('/')
         
      
      except Exception:
         db.rollback()
         return "Error"
      

#edit operation
@app.route('/edit/<rid>')

def edit(rid):


      try:
         db=pymysql.connect(host="localhost",user="root",password="",db="todolist")
         cu=db.cursor()
         sql="select * from task where id={}".format(rid)
         cu.execute(sql)
         data=cu.fetchone()
         return render_template('editform.html',d=data)
       
       #return "Success"
       
      except Exception:
	   
         return "Error"	 
         
#update

@app.route('/update',methods=['POST','GET'])

def update():
      
     
      rec_id=request.form['recid']      
      t=request.form['title']
      det=request.form['details']
      dt=request.form['date']
      
     # return rec_id+"-"+t+"-"+det+dt 
      
      
      try:
       db=pymysql.connect(host="localhost",user="root",password="",db="todolist")
       cu=db.cursor()
       sql="update task SET title 
       return "Success"
       
        
      except Exception:
	     
         db.rollback()
         return "Error"	 
         
        
           
     #return " i am in update"
     
     
           
      
if __name__=='__main__':

      app.run(debug=True)   #run() is the method of Flask class
      
      