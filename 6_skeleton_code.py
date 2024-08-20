# Class Code
class Bank :
       def __init__(self) :
              self.__user = []
              self.__atm = []
       
class user :
       def __init__(self, user_id, user_name) :
              self.__user_id = user_id
              self.__user_name = user_name
       
       @property
       def user_id(self) :
              return self.__user_id

class Account :
       def __init__(self, account_id, owner, balance) :
              self.__account_id = account_id
              self.__owner = owner
              self.__balance = balance
              self.__transaction = []
              self.__atm_card = None

       @property
       def account_id(self) :
              return self.__account_id
       
       @property
       def owner(self) :
              return self.__owner
       
       def add_atm_card(self, atm_card) :
              self.__atm_card = atm_card
       
       def deposit (self, amount) :
              if amount > 0 :
                     self.__balance += amount
                     self.__transaction.append(transaction('D', self.__atm_card.atm_id, amount, self.__balance))
              else :
                     return 'Error'
              
       def withdraw (self, amount) :
              if amount > 0 and amount <= self.__balance :
                     self.__balance -= amount
                     self.__transaction.append(transaction('W', self.__atm_card.atm_id, amount, self.__balance))
              else :
                     return 'Error'
       def transfer (self, amount, account) :
              if amount > 0 and amount <= self.__balance :
                     self.__balance -= amount
                     account.__balance += amount
                     self.__transaction.append(transaction('T', self.__atm_card.atm_id, amount, self.__balance))
                     account.__transaction.append(transaction('T', self.__atm_card.atm_id, amount, account.__balance))
              else :
                     return 'Error'
              
class ATM_card :
       limit_money_per_day = 40000
       annual_fee = 150

       def __init__ (self, card_id, pin) :
              self.__card_id = card_id
              self.__card_pin = pin
              self.__daily_spend = ATM_card.limit_money_per_day

       @property
       def id(self) :
              return self.__card_id
       
       @property
       def pin(self) :
              return self.__card_pin
       
       @property
       def daily_spend(self) :
              return self.__daily_spend
       
       @daily_spend.setter
       def daily_spend(self, amount) :
              self.__daily_spend -= amount


class ATM :
       init_money = 1000000
       def __init__(self, atm_id, balance) :
              self.__atm_id = atm_id
              self.__remain_money = balance


class transaction :
    pass

##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, หมายเลข ATM, จำนวนเงิน ]}
# *** Dictionary นี้ ใช้สำหรับสร้าง user และ atm instance เท่านั้น
user ={'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm ={'1001':1000000,'1002':200000}

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance จากข้อมูล Dictionary
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง


# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 3 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card 3) entered Pin ที่ user input ให้เครื่อง ATM
# TODO     return ถ้าบัตร และ Pin ถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 2 ตัว คือ 
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 2 ตัว คือ 
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 3 ตัว คือ 
# TODO     1) instance ของ account ตนเอง 2) instance ของ account ที่โอนไป 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harry
# และ Pin ที่รับมา เรียกใช้ function หรือ method จากเครื่อง ATM 
# ผลที่คาดหวัง : พิมพ์ หมายเลขบัตร ATM อย่างถูกต้อง และ หมายเลข account ของ harry อย่างถูกต้อง
# Ans : 12345, 1234567890, Success


# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000


# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error


# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500


# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# กำหนดให้เรียกใช้ method __str__() เพื่อใช้คำสั่งพิมพ์ข้อมูลจาก transaction ได้
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500