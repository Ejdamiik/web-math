from typing import List

class Determinant:

  def __init__(self, matrix: List) -> None:
    self.data = matrix

    self.value = self.calculate(self.data)
  
  def __repr__(self) -> None:
  
    res = []
    for row in self.data:
      s_row = [str(e) for e in row]
      res.append(("  ".join(s_row)))
    
    return "\n".join(res)


  def get_develop_determinant(self, det: List, e_index: int) -> List:  # Always developing by first row
    res = []

    for row_index in range(1, len(det)):  # looping through determinant
      row = []
      for column_index in range(len(det[0])):
        if column_index != e_index: 

          """we need just elements which are not in same row or column 
          (rows wont be same bcs we are not looping through first row)
          """

          row.append(det[row_index][column_index])
      res.append(row)

    return res


  def calculate(self, det: List) -> int:
    if len(det[0]) == 2:  # If it is elementary 2x2 determinant

      """
      |a  b|
      |c  d|  ==  ad - bc
      """

      return det[0][0] * det[1][1] - det[0][1] * det[1][0]

    # If it is complex determinant we use calculation by development (rozvoj)
    # We always develop based on first row

    develop = []  # Values of developed determinant
    for e_index in range(len(det[0])):  # Developing

      dev = self.get_develop_determinant(det, e_index)
      elem = det[0][e_index] * (-1) ** (0 + e_index + 2) * self.calculate(dev)
      develop.append(elem)

    # Result is sum of those values

    sum = 0
    for e in develop:
      sum += e
      
    return sum


  def get_value(self) -> int:
    return self.value
