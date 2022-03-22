'''


Axis Flexicap Mutual Fund

#url_for
http://127.0.0.1:5000/


html files are- dash.html,work.html,update.html(for edit) 
main file is- main.py who is controller of all files


'''


from flask import Flask,render_template,request,redirect,url_for

import pymysql

app=Flask(__name__)


@app.route('/')

def index():

      #return render_template('work.html')
      try:
          db=pymysql.connect(host="localhost",user="root",password="",db="axisflexicap")
          cu=db.cursor()
          sql="select*from performance"
          cu.execute(sql)
          data=cu.fetchall()
          
          #return "Success"
          
          return render_template('dash.html',d=data)
          
      except Exception:
      
          return "Error"
      
#task route 

@app.route('/performance')

def create_performance():

      return render_template('work.html') 
      
#store route
@app.route('/store',methods=['POST','GET'])

def store():
     
 
     p=request.form['Period']
     r=request.form['Returns_in_Percent']
     
    # return no+cust+nam+cont+bal+typ+status 
 
     try:
        db=pymysql.connect(host="localhost",user="root",password="",db="axisflexicap")
        
        
        cu=db.cursor()
        sql="insert into performance(Period,Returns_in_Percent)values('{}','{}')".format(p,r)
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
        db=pymysql.connect(host="localhost",user="root",password="",db="axisflexicap")
        
        
        cu=db.cursor()
        sql="delete from performance where id={}".format(rid)
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
        db=pymysql.connect(host="localhost",user="root",password="",db="axisflexicap")
        
        
        cu=db.cursor()
        sql="select * from performance where id={}".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('update.html',d=data)
        
      except Exception:

        return "Error"
      
      
#update

@app.route('/update',methods=['POST','GET'])

def update():

        rec_id=request.form['recid']
        p=request.form['Period']
        r=request.form['Returns_in_Percent']
             
        try:
          db=pymysql.connect(host="localhost",user="root",password="",db="axisflexicap")      
        
          cu=db.cursor()
          sql="update performance SET Period='{}',Returns_in_Percent='{}' where id={}".format(p,r,rec_id) 
          cu.execute(sql)
          db.commit()
          return redirect('/')
        
        except Exception:
          db.rollback()
          return "Error"  
          
          
       

       
          
          
     
if __name__=='__main__':

       app.run(debug=True)
      
      

