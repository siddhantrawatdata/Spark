import json

import pandas as pd
import random as rd
import datetime as dt
def data_generator():
    """
    The function is responsible for random data generation
    :return: Null
    """
    booking_id='B00'
    customer_id= "C00"
    car_id = 'CAR'
    booking_date = ['2024-08-01','2024-08-05','2024-08-10','2024-08-15','2024-08-20','2024-08-25','2024-08-30']
    # start_time = "2024-07-21T10:00:00Z"
    # end_time = "2024-07-21T18:00:00Z"
    total_amount = [150.75,160.75,170.75,180.45,156.78]
    status = ['completed','pending','inactive','active','cancelled']
    #file_append_date=['20240801','20240805','20240810','20240815','20240820','20240825','20240830']
    #file_append_date = ['20240801']
    booking_id_Start=1
    customer_id_start=1001
    car_id_start = 1021
    for i in range(len(booking_date)):
        split_date=booking_date[i].split('-')
        append_date=""
        for _ in split_date:
            append_date+=_
        # the data generation starts here
        cnt=0
        while cnt <100 :
            start_and_end_dates = create_start_time_and_end_time(split_date)
            final_booking_id=booking_id+str(booking_id_Start)
            final_customer_id=customer_id+str(customer_id_start)
            final_car_id=car_id+str(car_id_start)
            final_total_amount=rd.choice(total_amount)
            final_status=rd.choice(status)
            print(final_booking_id , final_customer_id , final_car_id,booking_date[i],start_and_end_dates[0],start_and_end_dates[1])

            json_data={
                "booking_id": final_booking_id,
                 "customer_id": final_customer_id,
                  "car_id": final_car_id,
                   "booking_date": booking_date[i],
                    "start_time": start_and_end_dates[0],
                     "end_time": start_and_end_dates[1],
                      "total_amount": final_total_amount,
                       "status": final_status
            }

            booking_id_Start += 1
            customer_id_start += 101
            car_id_start += 25
            cnt+=1

            zoom_car_bookings=pd.DataFrame(json_data,index=[0])
            # open the file and append data into it
            file_path = 'zoom_car_bookings_' + append_date +'.json'
            print(file_path)

            result=zoom_car_bookings.to_json(file_path,mode='a',orient='records',date_format='iso',lines=True)

            # write_to_file(file_path,json_data)

# def write_to_file(file_path,json_data):
#     with open(file_path,'r+') as file:
#         json.dump(json_data,file,indent=4)






def create_start_time_and_end_time(split_date):
    """
    As this is a random dataset the split date will be having only the date part and we are randomly generating the
    start timestamps . Post that end timestamp is randomly generated on the new start timestamps.
    :param split_date: Raw date coming from the booking_date array : input values are random
    :return: Randomly generated start time and end time
    """
    start_time_delta_in_minutes=[10,20,50,400,340,250,130]
    original_start_date=dt.datetime(int(split_date[0]),int(split_date[1]),int(split_date[2]))
    mins=rd.choice(start_time_delta_in_minutes)
    start_time_delta=dt.timedelta(minutes=mins)
    new_start_time=original_start_date+start_time_delta

    end_time_delta_in_minutes=[2,5,3,6,15,1,]
    end_mins=rd.choice(end_time_delta_in_minutes)
    end_time_delta=dt.timedelta(minutes=end_mins)
    new_end_time=new_start_time+end_time_delta

    print(f"start time is {new_start_time} , and end_time is {new_end_time}")
    dates=[]
    dates.append(new_start_time)
    dates.append(new_end_time)
    return dates




if __name__=='__main__':
    data_generator()