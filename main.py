print("if you want to Add employee, Remove employee, Update existed employee data.\nEnter 0 for ID and 0000 for password to gain the admin privilege and to access admin menu\n\nelse if you want to just Display Employee Information, Calculate Bouns, Calculate Discount, Remind Legal Holidays.\nyou can enter a predefined employee ID and password used for testing porposes {ID : 100, Password : 123}\n")


from  tkinter import*
from employee_data import*
from operations import*
from authentication import*
import getpass
attempts = 0
print('\nWelcome to the Employee Management System\n\nPlease Login to Continue.\n')
while (True):
    if attempts == 3:
        break
    state = emp_athuntication(employee_list)
    if state == 1:
        while(True):
            print("Login successful!\n\nSelect an option:\n1. Display Employee Information\n2. Calculate Bouns\n3. Calculate Discount\n4. Remind Legal Holidays\n5. Exit\n")
            ans = input("Please Enter Your choise: ")
            if ans == '1':
                Display(employee_list)
                main = input("\nPress Enter to Turn to Main Menu")
            elif ans == '2':
                Calc_Bouns(employee_list)
                main = input("\nPress Enter to Turn to Main Menu")
            elif ans == '3':
                Calc_Discount(employee_list)
                main = input("\nPress Enter to Turn to Main Menu")
            elif ans == '4':
                Remind_Holidays(employee_list)
                main = input("\nPress Enter to Turn to Main Menu")
            elif ans == '5':
                print("\nThank You for Using Employee Management System\n")
                exit()
            
    elif state == 2:
        if(attempts < 2):
            print(f"\nWrong Password you have {2-attempts} attempts left!\n")
        else:
            print("\nAccess Denied\n")
        
        attempts+=1

    elif state == 0:
        print("\nwelcome to admin list:\n")
        while (True):
            print("1.Add employee\n2.Remove employee\n3.Update existed data\n4.Exit program\n")
            admin_ans = input("Enter your choise: ")
            if admin_ans == '1':
                add_employee(employee_list)
                admin_ans = input("\nPress Enter to Turn to admin Menu")
            elif admin_ans == '2':
                remove_employee(employee_list)
                admin_ans = input("\nPress Enter to Turn to admin Menu")
            elif admin_ans == '3':
                update_employee(employee_list)
                admin_ans = input("\nPress Enter to Turn to admin Menu")
            elif admin_ans == '4':
                exit()
else:
    exit()

