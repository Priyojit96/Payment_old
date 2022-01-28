import razorpay
import requests,json

key='rzp_test_9LYWFiUVU6c33e'
key_secret='MJ2p0LB3vKMpFtPh73BBaxu0'
For='Test'
amount=100 #to be changed from frontend
receipt_no=str(1) #to be changed from ids
pre='#'
receipt=pre+receipt_no
Name='Test Person' # to be added from database
For='Campaign_Name' #to be added from the page
client = razorpay.Client(auth=(key, key_secret))
DATA={
    "amount":amount*100, #From Front end
    "currency":"INR",
    'receipt':receipt, #Backend incremented
    "notes":{
        "name":Name, #FrontEnd
        "Payment_for":For #FrontEnd Page
    }
}
order=client.order.create(data=DATA)
#print(order)
Order_ID=order['id']
print(Order_ID)





