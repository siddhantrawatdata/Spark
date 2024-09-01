import pandas as pd
from os import *
import faker
import random as rd

def generate_customer_id_data():
    path=r"C:\Users\siddhant.rawat\Desktop\GrowDataSkills-Studymaterial\Kafka\Project-1\zoom_car_bookings_data"
    for files in listdir(path):
        new_path=path + "\\" + files
        print(new_path)
        customer_id = pd.read_json(new_path\
                                   ,orient='records',lines=True)
        unique_customer_id= customer_id['customer_id']
        customer_id=[]

        for id in unique_customer_id:
            customer_id.append(id)

    return customer_id

def generate_random_names():
    # Initialize the Faker library
    fake = faker.Faker()

    # Function to generate a random email
    def generate_email(name):
        name_part = name.lower().replace(" ", "")
        domain = rd.choice(["gmail.com", "yahoo.com", "outlook.com", "hotmail.com"])
        return f"{name_part}@{domain}"

    # Generate 50 random names and emails
    name_and_email_phone = []
    for _ in range(50):
        name = fake.name()
        email = generate_email(name)
        phno=fake.phone_number()
        name_and_email_phone.append({
            "name": name,
            "email": email,
            "phone_number":phno
        })
        name_and_email_phone.append({
            "name": "test",
            "email": "xxxx",
            "phone_number": "2222222"
        })



    return name_and_email_phone



if __name__=='__main__':
    customer_id = generate_customer_id_data()
    print(customer_id)

    name_and_email_phone = generate_random_names()

    print(name_and_email_phone)
