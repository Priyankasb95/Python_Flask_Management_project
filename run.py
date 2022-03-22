'''
BANKING MANAGEMENT SYSTEM

http://127.0.0.1:5000/
'''


from flask import Flask,render_template,request,redirect,url_for

import pymysql

app=Flask(__name__)


@app.route('/')

def index():

      #return render_template('user.html')
      try:
          db=pymysql.connect(host="localhost",user="root",password="",db="bankdata")
          cu=db.cursor()
          sql="select*from accounts"
          cu.execute(sql)
          data=cu.fetchall()
          
          #return "Success"
          
          return render_template('flask.html',d=data)
          
      except Exception:
      
          return "Error"
      
#task route 

@app.route('/accounts')

def create_accounts():

      return render_template('user.html') 
      
#store route
@app.route('/store',methods=['POST','GET'])

def store():
     
 
     no=request.form['Account_No']
     cust=request.form['Customer_Id']
     nam=request.form['Name_of_the_Customer']
     cont=request.form['Contact_No']
     bal=request.form['Account_Balance']
     typ=request.form['Account_Type']
     status=request.form['Status']
     
    # return no+cust+nam+cont+bal+typ+status 
 
     try:
        db=pymysql.connect(host="localhost",user="root",password="",db="bankdata")
        
        
        cu=db.cursor()
        sql="insert into accounts(Account_No,Customer_Id,Name_of_the_Customer,Contact_No,Account_Balance,Account_Type,Status)values('{}','{}','{}','{}','{}','{}','{}')".format(no,cust,nam,cont,bal,typ,status)
        cu.execute(sql)
        db.commit()


        return redirect('/')
        #return "data inserted into table"
        #return "Success in Connection"
        
        
     except Exception:
     
        db.rollback()
        return "Error"
     
     
    
#delete operation
@app.route('/delete/<rid>')

def delete(rid):

      try:
        db=pymysql.connect(host="localhost",user="root",password="",db="bankdata")
        
        
        cu=db.cursor()
        sql="delete from accounts where id={}".format(rid)
        cu.execute(sql)
        db.commit()
      
      
        return redirect('/')
        
        
      except Exception:
        db.rollback()
        return "Error"
        
#edit operation 
@app.route('/edit/<rid>')  
        
def edit(rid):

      try:
        db=pymysql.connect(host="localhost",user="root",password="",db="bankdata")
        
        
        cu=db.cursor()
        sql="select * from accounts where id={}".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('edit.html',d=data)
        
      except Exception:

        return "Error"
      
      
#update

@app.route('/update',methods=['POST','GET'])

def update():

       
        rec_id=request.form['recid']
        no=request.form['Account_No']
        cust=request.form['Customer_Id']
        nam=request.form['Name_of_the_Customer']
        cont=request.form['Contact_No']
        bal=request.form['Account_Balance']
        typ=request.form['Account_Type']
        status=request.form['Status']
         
        
     # return "i am in update"
          
        try:
          db=pymysql.connect(host="localhost",user="root",password="",db="bankdata")      
        
          cu=db.cursor()
          sql="update accounts SET Account_No='{}',Customer_Id='{}',Name_of_the_Customer='{}',Contact_No='{}',Account_Balance='{}',Account_Type='{}',Status='{}' where id={}".format(no,cust,nam,cont,bal,typ,status,rec_id) 
          cu.execute(sql)
          db.commit()
          return redirect('/')
        
        except Exception:
          db.rollback()
          return "Error"  
          
          
       

       
          
          
     
if __name__=='__main__':

       app.run(debug=True)
      
      

