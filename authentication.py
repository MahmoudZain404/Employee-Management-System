from employee_data import*
admin_Passwd = '0000'

try:
    from msvcrt import getch
    def getpass(prompt):
        """Replacement for getpass.getpass() which prints asterisks for each character typed"""
        print(prompt, end='', flush=True)
        buf = b''
        while True:
            ch = getch()
            if ch in {b'\n', b'\r', b'\r\n'}:
                print('')
                break
            elif ch == b'\x08': # Backspace
                buf = buf[:-1]
                print(f'\r{(len(prompt)+len(buf)+1)*" "}\r{prompt}{"*" * len(buf)}', end='', flush=True)
            elif ch == b'\x03': # Ctrl+C
                raise KeyboardInterrupt
            else:
                buf += ch
                print('*', end='', flush=True)
        return buf.decode(encoding='utf-8')
except ImportError:
    from getpass import getpass

def emp_athuntication(employee_list):
    login_Id = int(input("Please Enter Your Employee ID: "))
    passwd = getpass("Please Enter Your Password: ")
    for x in employee_list:
        if(str(passwd) == admin_Passwd and login_Id == 0):
            return 0
        elif(x.get('Password') == passwd and x.get('id') == login_Id):
            return 1
    else:
        return 2







#print(emp_athuntication(employee_list))