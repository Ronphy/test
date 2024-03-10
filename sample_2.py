import json
def main_2():

   x = [1]
   y = x
   y += [1]
   print(x)
   if x is y:
      print('True')
   else:
      print('False')

   #class イメージは画像参照
   class Point:
      #パラメータ的なclass 画像参照
      def __init__(self, x=0., y=0.):
          self.x = x
          self.y = y
      
      #関数的な役割を持つclass
      def set(self, x, y):
          self.x = x
          self.y = y

      def transpose(self):
          self.x, self.y = self.y, self.x

      def hamming(self):
          return self.x + self.y

      def dot(self, other):
          return self.x * other.x + self.y * other.y




if __name__ == "__main__":
    main_2()