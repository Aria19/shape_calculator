class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height
    
  def __repr__(self):
    if self.width != self.height:
      n = "Rectangle(width={}, height={})".format(str(self.width), str(self.height))
    else:  
      n = "Square(side={})".format(str(self.width))
    return n
  
  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  def get_diagonal(self):
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture(self):
    ch = ""
    if (self.height > 50) or (self.width > 50):
      ch = "Too big for picture."
    else:
      for i in range(self.height):
        c = ""
        ch = ch + c.center(self.width, '*') + "\n"
    return ch
      

  def get_amount_inside(self, shape):
    sh = int((self.width / shape.width) * (self.height / shape.height))
    return sh
    
class Square(Rectangle):

  def __init__(self, sidelen):
    self.width = sidelen
    self.height = sidelen
    
  def set_side(self, sidelen):
    self.width = sidelen
    self.height = sidelen
    
  def set_width(self, width):
    self.width = width
    self.height = width
    
  def set_height(self, height):
    self.width = height
    self.height = height