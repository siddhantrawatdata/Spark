# Zoom Booking and Customer data load project 

### Introduction
Zoom is a company that provides online cab services to it's users. You can book a Cab and go anywhere you want . As a data-Engineer my responsibility is to process the booking and customer related data . 

### Tech-Stack
1. Processing - Databricks
2. Storage - GCP
3. Data Generation - Python

### Mock data Generation
I have generated mock data using python.\
```Zoom_booking_data_generation.py``` : Generaes the booking data and creates a CSV file.\
```Zoom_customer_data_generation.py``` : Generates the customer data and creates a CSV file.\
```extract_bookings_data.py``` : Link between both the datasets as I need to make sure the customer_doing the bookings are existing in both the tables.


### Flow diagram
![image](https://github.com/user-attachments/assets/6a9e2bae-6c32-4066-a927-363b0429de97)

```Zoom_car_booking_analysis``` : Load and process the booking data in databricks and load into Delta staging tables.\
```Zoom_car_customer_analysis``` : Load and process the booking data in databricks and load into Delta staging tables.\
```Zoom_car_and_customer_merge``` : Merge the data from customer and bookings.

![image](https://github.com/user-attachments/assets/7c2d2a0e-67e6-4194-8b99-bcfc069baf1e)



