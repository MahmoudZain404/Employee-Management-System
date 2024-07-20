from employee_data import*

def Display(employee_list):
    employ_id = int(input("Please Enter Your Employee ID: "))
    for i in range(len(employee_list)):
        if(employee_list[i]['id']==employ_id):
            print(f"\n\nEmployee Information:\nName: {employee_list[i]['Name']}\nDepartment: {employee_list[i]['Department']}\nSalary: ${employee_list[i]['Salary']}\nDays of Absence: {employee_list[i]['Days_of_Absence']}\n")
            break
    else:
        print("Error ID Doesn't Exist!")


def Calc_Bouns(employee_list):
    employ_id = int(input("Please Enter Your Employee ID: "))
    for i in employee_list:
        if(i.get('id')==employ_id):
            print(f"\n\nBounse Calculation:\nBouns: ${round((i.get('Salary')*10)/100)}\n")
            break
    else:
        print("Error ID Doesn't Exist!")


def Calc_Discount(employee_list):
    employ_id = int(input("Please Enter Your Employee ID: "))
    for i in employee_list:
        if(i.get('id')==employ_id):
            print(f"\n\nDiscount Calculation:\nDiscount: ${round((i.get('Salary')*5)/100)}\n")
            break
    else:
        print("Error ID Doesn't Exist!")

def  Remind_Holidays(employee_list):
    num_of_Holidays_Days = 12
    employ_id = int(input("Please Enter Your Employee ID: "))
    for i in employee_list:
        if(i.get('id')==employ_id):
            print(f"\n\nReminder:\nRemaining Legal Holidays: {num_of_Holidays_Days - (i.get('Days_of_Absence'))} Days\n")
            break


#Display(employee_list)
#Calc_Bouns(employee_list)
#Calc_Discount(employee_list)
#Remind_Holidays(employee_list)