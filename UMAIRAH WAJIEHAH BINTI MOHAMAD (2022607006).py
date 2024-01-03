import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="diving_center"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to calculate age based on birthdate
def calculate_age(birthyear):
    current_year = 2023
    age = current_year - int(birthyear)
    return age

# Function to insert data into the table
def collect_data():
    name = full_name_entry.get()
    birthyear = birthyear_entry.get()
    gender = gender_entry.get()
    phone_number = phone_number_entry.get()
    

    # Calculate age based on birthdate
    age = calculate_age(birthyear)

    # Apply discount if the person is under 18
    discount_percentage = 0.3 if age < 18 else 0

    # Calculate registration fee
    base_fee = 300
    registration_fee = base_fee - (base_fee * discount_percentage)

    # Insert data into the database
    sql = "INSERT INTO members (Full_Name, Gender, Birth_Year, Age, Phone_Number, Fee) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, gender, birthyear, age, phone_number, registration_fee)
    mycursor.execute(sql, val)
    mydb.commit()

    # Display the result
    output_label.config(text=f"Full Name: {name}\n\n Gender: {gender}\n\n Birth Year: {birthyear}\n\n Age: {age}\n\n"
                              f"Phone Number: {phone_number}\n\n Registration Fee: RM{registration_fee}\n\n")

# Tkinter GUI
root = tk.Tk()
root.title("Diving Centre Registration System")
root.geometry("600x600")
root.configure(bg="pink")

# Page Title
label = tk.Label(root, text='Welcome to Diving Center', font=("Times New Roman", 15, "bold"))
label.pack(ipadx=10, ipady=10)

label_full_name = tk.Label(root, text="Name:")
label_full_name.pack()
full_name_entry = tk.Entry(root)
full_name_entry.pack()

label_birthyear = tk.Label(root, text="Birth Year:")
label_birthyear.pack()
birthyear_entry = tk.Entry(root)
birthyear_entry.pack()

label_gender = tk.Label(root, text="Gender:")
label_gender.pack()
gender_entry = tk.Entry(root)
gender_entry.pack()

label_phone_number = tk.Label(root, text="Phone Number")
label_phone_number.pack()
phone_number_entry = tk.Entry(root)
phone_number_entry.pack()


# Buttons to perform operations
# Save Button
save_button = tk.Button(root, text="Enter", command=collect_data)
save_button.pack(pady=10)

# Output Label & result
label = tk.Label(root, text='Result:', font=("Times New Roman", 12))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
