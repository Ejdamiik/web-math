from io import BytesIO
from flask import Flask, send_file, request, send_from_directory,render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  """
  HTTP response for other actions
  """
  
  if (len(path) == 0):
    # ak nezadany ziaden subor, teda cesta / chceme index.html
    return send_from_directory('public', 'index.html')

  return send_from_directory('public', path)

@app.route('/equation', methods=['post'])
def render():
  """
  Returns HTTP response for render action
  """
  print("here")
  res = request.form.get('equation')
  print(res)

  return "Done"

app.run()
