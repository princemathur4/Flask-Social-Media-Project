from app import app

@app.route('/')
@app.route('/index')
def index():
    user ={"username":"Prince Mathur"}
    return '''
    <html>
        <head>
            <title>My Awesome webpage</title>    
        </head>
        <body>
            <h1>
                Hey ,'''+user['username']+'''! 
                \nWelcome to my awesome webpage :)
            </h1>
        </body>
    </html>
    '''
