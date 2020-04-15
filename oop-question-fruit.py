# class Car:
  
#   # Attributes
#   color = "No color"
#   brand = "No brand"
#   numOfwheels = 4 # จำนวนล้อ
#   numOfseats = 4  # จำนวนเบาะนั่ง
#   maxSpeed = 0
#   numberOfcar = 0
  
#   def __init__(self, color, brand, maxSpeed):
#     self.color = color
#     self.brand = brand
#     self.maxSpeed    = maxSpeed
  
#   # Methods
#   def setColor(self,c):
#     self.color = c
 
#   def setBrand(self,b):
#     self.brand = b
  
#   def setMaxSpeed(self,s):
#     self.maxSpeed = s
  
#   def printData(self):
#     print("The color of car is : ",self.color)
#     print("The car was built by :",self.brand)
#     print("The Maximun speed is :",self.maxSpeed," km/hr.")
    
#  # Create Object
# car1 = Car("blue","Honda",250)
# car1.printData()
# car1.setColor("Goldrose")
# print("After set color :",car1.color)

# car2 = Car("red","Toyota",670)
# car2.printData()

# class animal:

#     leg = "none"
#     catagory = "none"
#     location = "none" 
#     sound = "none"

#     def __init__(self,leg,catagory,location,sound):
#         self.leg = leg
#         self.catagory = catagory
#         self.location = location
#         self.sound = sound

#     def setleg(self,l):
#         self.leg = l

#     def setcatagory(self,c):
#         self.catagory = c

#     def setlocation(self,lo):
#         self.location = lo

#     def setsound(self,s):
#         self.sound = s 

#     def data(self):
#         print('มีขา',self.leg,'ขา')
#         print('เป็นสัตว์ประเภท',self.catagory)
#         print('สถานที่',self.location)
#         print('เสียงร้อง',self.sound)

# animal1 = animal(4,'เลี้ยงลูกด้วยนม','บนบก','เหมียวๆ')
# animal1.data()

class fruit:
    color = "ไม่ระบุ"
    taste = "ไม่ระบุ"
    skin = "ไม่ระบุ"
    signature = "ไม่ระบุ"

    def __init__(self,color,taste,skin,signature):
        self.color = color
        self.taste = taste
        self.skin = skin
        self.signature = signature

    def setColor(self,color):
        self.color = color

    def setTaste(self,taste):
        self.taste = taste
    
    def setSkin(self,skin):
        self.skin = skin

    def setSignature(self,signature):
        self.signature = signature

    def data(self):
        print('สีของผลไม้ : ',self.color)
        print('รสชาติของผลไม้ : ',self.taste)
        print('พื้นผิวของผลไม้ : ',self.skin)
        print('ลักษณะเฉพาะตัว : ',self.signature)

question1 = fruit('สีแดง','เปรี้ยวอมหวาน','เรียบเนียน','เป็นหนึ่ในโลโก้โทรศัพท์')
question2 = fruit('สีเหลือง','หวาน','เรียบเนียน','คิดเหมือนฉันมั้ยบีหนึ่ง')
question3 = fruit('สีม่วง','เปรี้ยวอมหวาน','หยาบๆ','ราชินีผลไม้ไทย')
question4 = fruit('สีเขียว','หวาน','มีหนาว','ราชาผลไม้ไทย')
question5 = fruit('สีเขียว','หวาน','เรียบเนียน','กะทิ')
choice = ['มะม่วง','แอปเปิ้ล','ทุเรียน','องุ่น','กล้วย','มะพร้าว','ลิ้นจี่','มังคุด','มะปราง']
data_answer = []
data_showAnswer = ['แอปเปิ้ล','กล้วย','ทุเรียน','มังคุด','มะพร้าว']
data_question = [question1,question2,question3,question4,question5]

print('มาทายชื่อผลไม้กัน')
print('ตัวเลือกสำหรับคุณ =>',end=" ")
print(choice)
print( )

i = 0
x = 1
while i <= 4:
    print('-------------------------------------------')
    print('คำถามข้อที่ %d' % x)
    print( )
    data_question[i].data()
    print('-------------------------------------------')
    answer = input('คำตอบของคุณ : ')
    data_answer.append(answer)
    i = i+1
    x = x+1

if data_answer[0] == data_showAnswer[0] and data_answer[1] != data_showAnswer[1] and data_answer[2] != data_showAnswer[2] and data_answer[3] != data_showAnswer[3] and data_answer[4] != data_showAnswer[4]:
    print('ถูกต้อง')
elif data_answer[0] == data_showAnswer[0] and data_answer[1] != data_showAnswer[1] and data_answer[2] != data_showAnswer[2] and data_answer[3] != data_showAnswer[3] and data_answer[4] != data_showAnswer[4]:
    print('ถูกต้อง')  
elif data_answer[0] == data_showAnswer[0] and data_answer[1] != data_showAnswer[1] and data_answer[2] != data_showAnswer[2] and data_answer[3] != data_showAnswer[3] and data_answer[4] != data_showAnswer[4]:
        print('ถูกต้อง')  
elif data_answer[0] == data_showAnswer[0] and data_answer[1] != data_showAnswer[1] and data_answer[2] != data_showAnswer[2] and data_answer[3] != data_showAnswer[3] and data_answer[4] != data_showAnswer[4]:
    print('ถูกต้อง')  
elif data_answer[0] == data_showAnswer[0] and data_answer[1] != data_showAnswer[1] and data_answer[2] != data_showAnswer[2] and data_answer[3] != data_showAnswer[3] and data_answer[4] != data_showAnswer[4]:
    print('ถูกต้อง')      
else:
    print('ผิด')
        



