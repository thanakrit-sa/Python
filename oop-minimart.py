class product:
    name: "ไม่ระบุ"
    prine: "ไม่ระบุ"
    amount: "ไม่ระบุ"

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def setAmount(self, amount):
        self.amount = amount

    def showData(self):
        print("ชื่อสินค้า : %s" % self.name)
        print("ราคา : %d บาท " % self.price)
        print("จำนวน : %d ชิ้น" % self.amount)


product1 = product("ทีวี", 3000, 5)
product2 = product("ตู้เย็น", 7800, 9)
product3 = product("เครื่องซักผ้า", 2300, 10)
product4 = product("คอมพิวเตอร์", 34526, 2)

dataProduct = [product1, product2, product3, product4]
dataBuy = []
dataCount = []

print()
c = 1
x = 0
while x <= len(dataProduct)-1:
    print("รายการที่ : %d" % c)
    dataProduct[x].showData()
    print("--------------------------------------------")
    x = x+1
    c = c+1

print("ใส่หมายเลขรายการเพื่อซื้อสินค้าชิ้นนั้น")
buy = int(input("หมายเลขรายการ : "))
print("--------------------------------------------")

if buy == 1:
    print("รายการที่ท่านเลือกคือ : ทีวี")
    print("มูลค่า 3000 บาท")
    count = input("จำนวนสินค้า : ")
    dataBuy.append(product1)
    dataCount.append(count)
elif buy == 2:
    print("รายการที่ท่านเลือกคือ : ตู้เย็น")
    print("มูลค่า 7800 บาท")
    count = input("จำนวนสินค้า : ")
    dataBuy.append(product2)
    dataCount.append(count)
elif buy == 3:
    print("รายการที่ท่านเลือกคือ : เครื่องซักผ้า")
    print("มูลค่า 2300 บาท")
    count = input("จำนวนสินค้า : ")
    dataBuy.append(product3)
    dataCount.append(count)
elif buy == 4:
    print("รายการที่ท่านเลือกคือ : คอมพิวเตอร์")
    print("มูลค่า 34526 บาท")
    count = input("จำนวนสินค้า : ")
    sum = (34526*int(count))
    print('รวมราคา : %d' % sum)
    answer = input('ท่าต้องการซื้อหรือไม่ [y,n] : ')
    print("--------------------------------------------")
    if answer == "y":
        dataBuy.append(product4)
        dataCount.append(count)
    else:
        print('เลือกซื้อรายการอื่นกด 1')
        print('ยกเลิกการทำรายการกด 2')
        print('ออกจากโปรแกรมกด 3')
        choice = input('หมายเลขที่ทำรายการ : ')
else:
    print("คุณทำรายการไม่ถูกต้อง")


