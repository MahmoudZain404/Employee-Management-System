
def add_employee(employee_list):
    temp_dict = {'id': 0, 'Name': "0", 'Department': "0", 'Salary': 0, 'Password': "0", 'Days_of_Absence': 0}
    

    while temp_dict.get('id') == 0:
        temp_dict.update({'id':int(input("Please Enter employee id: "))})
        for i in range(len(employee_list)):
            if(employee_list[i]['id'] == temp_dict.get('id')):
                print("\nid already exists! please try new id\n")
                temp_dict.update({'id':0})
                break
            

    temp_dict.update({'Name':input("Please Enter employee Name: ")}) 
    temp_dict.update({'Department':input("Please Enter employee Department: ")}) 
    temp_dict.update({'Salary':input("Please Enter employee Salary: ")}) 
    temp_dict.update({'Password':input("Please Enter employee Password: ")}) 
    temp_dict.update({'Days_of_Absence':input("Please Enter employee Days_of_Absence: ")}) 
    employee_list.append(temp_dict)
    print("*Updated List*")
    for i in range(1,len(employee_list)):
        print("\n---------------------------------------------------------\n")
        print (" ".join(["{0}:{1}".format(k, v) for k, v in employee_list[i].items()]))

def remove_employee(employee_list):
    remove_id = int(input("Please enter the employee id you want to remove: "))

    for i in  range(len(employee_list)):
        if(employee_list[i]['id'] == remove_id):
            if(remove_id != 0):
                del employee_list[i]
                break
            else:
                print("\nYou don't have the privilege to delete admin!")
                break
        else:
            continue
    else:
        print("\nThe id you want to remove doesn't exist!\n")
        return 1
    print("\n*Updated List*")
    for i in range(1,len(employee_list)):
        print("\n---------------------------------------------------------\n")
        print (" ".join(["{0}:{1}".format(k, v) for k, v in employee_list[i].items()]))

def update_employee(employee_list):
    update_id = int(input("Please enter the employee id you want to update: "))
    
    for i in  range(len(employee_list)):
        if(employee_list[i]['id'] == update_id and employee_list[i]['id'] != 0):
            update_field = input("Please enter the field you want to update!, avilable fields(id, Name, Department, Salary, Password, Days_of_Absence): ")
            if(update_field == 'id' or update_field == 'Salary' or update_field == 'Days_of_Absence'):
                update_value = int(input("Please enter the field update value: "))
                employee_list[i][update_field] = update_value
            elif(update_field == 'Name' or update_field == 'Department' or update_field == 'Password'):
                update_value = input("Please enter the field update value: ")
                employee_list[i][update_field] = update_value
            else:
                print("Error field not found!")
                break
        else:
            continue
        print("*Updated List*")
        for i in range(1,len(employee_list)):
            print("\n---------------------------------------------------------\n")
            print (" ".join(["{0}:{1}".format(k, v) for k, v in employee_list[i].items()]))
        break
    else:
        print("\nThe id you want to update doesn't exist!\n") 

employee_list = [ {'id': 0, 'Name': "Admin", 'Department': "Admin", 'Salary': 0, 'Password': "0000", 'Days_of_Absence': 0},
                  {'id': 100, 'Name': "Mahmoud", 'Department': "Developers", 'Salary': 5000, 'Password': "123", 'Days_of_Absence': 2},
                  {'id': 101, 'Name': "Ahmed", 'Department': "Testers", 'Salary': 7000, 'Password': "123", 'Days_of_Absence': 2}]

#add_employee(employee_list)

#remove_employee(employee_list)

#update_employee(employee_list)