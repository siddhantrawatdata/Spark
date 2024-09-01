import pandas as pd
import datetime as dt
import random as rd
from extract_bookings_data import generate_random_names , generate_customer_id_data

def data_generator():
    signup_date= ["2024-01-15","2024-01-10","2024-02-12","2024-03-10","2024-04-18","2024-04-18","2024-04-20","2024-04-25","2024-05-18","2024-06-18"]
    signup_char_dates=["20240115","20240110","20240212","20240310","20240418","20240418","20240420","20240425","20240518","20240618"]
    status= ['active','inactive']
    customer_ids = generate_customer_id_data()
    name_and_email_phone = generate_random_names()
    #Generate 10 customer files each with 100 records
    for signup in signup_char_dates:
        cnt=0
        while cnt<100:
            name_phone_email=rd.choice(name_and_email_phone)

            customer_data={
                "customer_id":rd.choice(customer_ids),
                "name": name_phone_email['name'],
                "email": name_phone_email['email'],
                "phone_number": name_phone_email['phone_number'],
                "signup_date": rd.choice(signup_date),
                "status": rd.choice(status)
            }
            cnt+=1
            print(customer_data)
            file_path = 'zoom_car_customer_' + signup + '.json'
            print(file_path)
            zoom_customer_data=pd.DataFrame(customer_data,index=[0])
            res=zoom_customer_data.to_json(file_path,mode='a',orient='records',lines=True)

if __name__=='__main__':
    data_generator()