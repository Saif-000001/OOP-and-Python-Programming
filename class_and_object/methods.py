def call():
    print("Calling someone i don't know!")
    return 'call done'

class Phone:
    price = 19000
    color = 'Blue'
    brand = 'samsung'
    feature = ['camera', 'speaker', 'hammer']

    def call(self):
        print('Calling one person')
    def send_sms(self, phone, sms):
        txt = f'sending SMS to: {phone} and message to: {sms}'
        return txt
    

my_phone = Phone()
print(my_phone.feature)

my_phone.call()

ans = my_phone.send_sms(45245, 'Hey, laddy!')
print(ans)

# print(call())