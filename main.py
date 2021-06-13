from io import BytesIO
from flask import Flask, send_file, request, send_from_directory,render_template
from determinant import Determinant


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


@app.route('/solve', methods=['post'])
def solve():
  """
  Returns HTTP response for render action
  """
  x1 = int(request.form.get('x1'))
  y1 = int(request.form.get('y1'))
  z1 = int(request.form.get('z1'))
  r1 = int(request.form.get('r1'))

  x2 = int(request.form.get('x2'))
  y2 = int(request.form.get('y2'))
  z2 = int(request.form.get('z2'))
  r2 = int(request.form.get('r2'))

  x3 = int(request.form.get('x3'))
  y3 = int(request.form.get('y3'))
  z3 = int(request.form.get('z3'))
  r3 = int(request.form.get('r3'))

  D = [
  [x1, y1, z1],
  [x2, y2, z2],
  [x3, y3, z3]
      ]

  Dx = [
  [r1, y1, z1],
  [r2, y2, z2],
  [r3, y3, z3]
      ]

  Dy = [
  [x1, r1, z1],
  [x2, r2, z2],
  [x3, r3, z3]
      ]

  Dz = [
  [x1, y1, r1],
  [x2, y2, r2],
  [x3, y3, r3]
      ]


  print("here")

  D_d = Determinant(D)
  D_x = Determinant(Dx)
  D_y = Determinant(Dy)
  D_z = Determinant(Dz)

  print("here")

  x = D_x.get_value() / D_d.get_value()
  y = D_y.get_value() / D_d.get_value()
  z = D_z.get_value() / D_d.get_value()

  return f"{x} {y} {z}"

app.run()
