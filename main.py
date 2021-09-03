from flask import Flask, send_file, request, send_from_directory,render_template
from determinant import Determinant
from io import BytesIO
import my_plot_lib
from PIL import Image
from typing import Tuple


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.static_folder = r'public\static'

def hex2dec(hex_num: str) -> int:
  """
  Method resposible for converting hexadecimal number to decimal number

  hex_num - string with hexadecimal number
  """

  hex_num = hex_num.replace("\n","")
  convertion = {
      "a": 10, "b": 11, "c": 12, 
      "d": 13, "e": 14, "f": 15
      }
  decimal = 0

  for index in range(len(hex_num)):

    if hex_num[index].lower() in convertion:
      decimal += (16**(len(hex_num) - index - 1)) * convertion[hex_num[index].lower()]
    else:
      decimal += (16**(len(hex_num) - index - 1)) * int(hex_num[index].lower())
  
  return decimal


def hexColor(color: str) -> Tuple:
  """
  Method responsible for converting color hexcode to rgb tuple

  color - string with color hexcode
  """
  color = color.replace("\n", "")
  r = hex2dec(color[1:3])
  g = hex2dec(color[3:5])
  b = hex2dec(color[5:])

  return (r, g, b)

def serve_pil_image(img):
  """
  Allows to save PIL image object to a
  virtual file in memory and then return
  it as a HTTP response
  """

  img_io = BytesIO()
  img.save(img_io, 'PNG', quality=70)
  img_io.seek(0)
  return send_file(img_io, mimetype='image/png')




@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  """
  HTTP response for other actions
  """
  
  if (len(path) == 0):

    return send_from_directory('public', 'main_page.html')

  return send_from_directory('public', path)


@app.route('/linear', methods=['post', "get"])
def linear():

  return send_from_directory('public', 'linear_system.html')


@app.route('/graph', methods=['post', "get"])
def graph():

  return send_from_directory('public', 'graph_visualization.html')


@app.route('/get_graph', methods=["post"])
def get_graph():

  canvas = Image.new('RGB', (400, 400), (0,0,0))
  my_plot_lib.create_cartesian(canvas)
  selected = request.form.get("selected")
  color = request.form.get("color")

  r, g, b = hexColor(color)

  if selected == "linear":
    my_plot_lib.draw_plot(canvas, my_plot_lib.linear, (r, g, b))
  elif selected == "quadratic":
    my_plot_lib.draw_plot(canvas, my_plot_lib.quadratic, (r, g, b))
  elif selected == "cubic":
    my_plot_lib.draw_plot(canvas, my_plot_lib.cubic, (r, g, b))

  return serve_pil_image(canvas)


@app.route('/solve', methods=['post'])
def solve():
  """
  Returns HTTP response for render action
  """
  x1 = float(request.form.get('x1'))
  y1 = float(request.form.get('y1'))
  z1 = float(request.form.get('z1'))
  r1 = float(request.form.get('r1'))

  x2 = float(request.form.get('x2'))
  y2 = float(request.form.get('y2'))
  z2 = float(request.form.get('z2'))
  r2 = float(request.form.get('r2'))

  x3 = float(request.form.get('x3'))
  y3 = float(request.form.get('y3'))
  z3 = float(request.form.get('z3'))
  r3 = float(request.form.get('r3'))

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


  D_d = Determinant(D)
  D_x = Determinant(Dx)
  D_y = Determinant(Dy)
  D_z = Determinant(Dz)


  x = D_x.get_value() / D_d.get_value()
  y = D_y.get_value() / D_d.get_value()
  z = D_z.get_value() / D_d.get_value()


  if abs(x) == 0:   # Weird glitch (its possible to get -0)
    x = abs(x)
  if abs(y) == 0:
    y = abs(y)
  if abs(z) == 0:
    z = abs(z)

  return f"{x} {y} {z}"

app.run()
