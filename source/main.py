from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/redirect')
def redirect_route():
    # Retrieve the redirect link from the environment variable
    redirect_link = os.environ.get('REDIRECT_LINK', 'http://example.com')
    return redirect(redirect_link, code=302)

if __name__ == '__main__':
    # Run the app
    app.run(host='0.0.0.0', port=80)
