from flask import Flask,render_template,request, escape,session
from search4letters import search4letter
from time import sleep
from dbcm import useDatabase
from checker import check_logged_in
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)
app.config['dbconfig'] = {'host': '12777.0.0.1',
              'user': 'vsearch',
               'password': 'vsearchpasswd',
                'database': 'vsearchlogDB', }
app.secret_key = 'YouWillNeverGuessThiBro'
  
def log_request(req, res:str)->None:
  with useDatabase(app.config['dbconfig']) as cursor:
 
    _SQL = """insert into log 
        (phrase,letters, ip, browser_string,results) 
         values(%s,%s,%s,%s,%s)"""
    cursor.execute(_SQL, 
                 (req.form['phrase'], 
                  req.form['letters'], 
                  req.remote_addr,
                  req.user_agent.browser if req.user_agent.browser else 'N/A', res,))
  

@app.route('/search4', methods= ['POST','GET'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results= str(search4letter(phrase, letters))
    try:
     log_request(request, results)
    except Exception as err:
     print('*** Logging failed with this error:', str(err))
    return render_template('results.html', the_phrase=phrase, the_letters= letters, the_title=title, the_results = results,)
@app.route('/')
@app.route('/entry')
def entry_page():
    return  render_template('entry.html', the_title = "welcome to search4letters on the web!")

@app.route('/viewlog')

def view_the_log():
   try:
    with useDatabase(app.config['dbconfig'])as cursor:
   
      _SQL = """select phrase, letters, ip, browser_string, results from log"""
      cursor.execute(_SQL)
      contents = cursor.fetchall()
   except mysql.connector.errors.InterfaceError as err:
    print("Is your database switched on? Error:", str(err))
   except Exception as err:
    print("Something went wrong:", str(err))
    titles = ('Form Data', ' Remote_addr','user_agent', 'Results')
    return render_template('viewlog.html', the_title = 'view Log', row_titles= titles, the_data= contents,)
@app.route('/setuser/<user>')
def setuser(user:str) -> str:
   session['user']= user
   return 'User value set to: ' + session['user']


@app.route('/getuser')
def getuser()->str:
  
   return 'User value is currenly set to : ' + session['user']
@app.route('/login')
def do_login()->str:
   session['logged_in'] = True
   return 'You are now logged in.'


@app.route('/logout')
def do_logout() ->str:
   session.pop('logged_in')
   return 'You are now loged out.'

@app.route('/status')
@check_logged_in
def check_login():
   return 'check this page with Decorater functionality'   
app.run(debug=True)
if __name__ == '_main_':
    app.run(debug=True)
