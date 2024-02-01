# convertor celsius to fahrenheit

# << ---- Import ---- >>
import os

# << ---- Variable ---- >>
menu = ['Start Work - 1', 'Log - 2', 'Info - 3', 'Stop Work - 4']
welcom_Logo = "Welcom, to software."
display_welcom = 0
chose_menu_section = None
user_input_value = None
convertation_cf = None
wather_fahrenheit = None
log_sessions = []
main_loop = 1


# << ---- Functional function ---- >>
def welcom_displayed(display_welcom):
    global welcom_Logo
    if display_welcom == 0:
        print(welcom_Logo)
        display_welcom = 1

def display_main_menu(menu):
    for i in menu:
        print(i)

def convertor_cf(user_input_value):
    convert_cf = (user_input_value * (212 - 32)) / 100 + 32
    return convert_cf

def log_creator(convertation_cf):
    global log_sessions
    log_sessions.append(convertation_cf)

def log_reader(log_sessions):
    _index_session = 1
    if (len(log_sessions) == 0):
        print("Log is Empty " + '\n')
    for i in log_sessions:
        print(f"Whether: {_index_session} - {i}" + '\n')
        _index_session += 1

def info_programs():
    print("simple convertor \n")

def print_cf(convertation_cf):
    print(f'Wather is a -- {convertation_cf} F \n')

def clear_consol():
    os.system('cls' if os.name == 'nt' else 'clear')


# << ---- Input function ---- >>
def select_menu_section():
    _index = 1
    while(_index):
        get_user_input = input("Entered Menu chose sections : ")
        try:
            menu_section = int(get_user_input)
        except ValueError:
            print('Input the number, not character')
            continue
        _index = 0
    return menu_section

def input_user_value():
    _index_ = 1
    global user_input_value
    while(_index_):
        user_value = input("Input the values in celsius : ")
        try:
            _user_input_value = int(user_value)
            user_input_value = _user_input_value
        except ValueError:
            print("Value is not number. Entered the number.")
            continue
        _index_ = 0

def stop_program():
    raw_date = input("Enter the 'n' - to stop or prese Enter : ")
    if raw_date == 'n' or raw_date == 'N':
        return 0
    else:
        return 1


# << ---- Constructor function ---- >>
def menu_option():
    global chose_menu_section
    _used_menu = chose_menu_section
    if (_used_menu == 1):
        # Start Work
        calculation_fahrenheit()
    elif (_used_menu == 2):
        # Log
        clear_consol()
        log_reader(log_sessions)
    elif (_used_menu == 3):
        # Info
        clear_consol()
        info_programs()
    elif(_used_menu == 4):
        # Stop Work
        global main_loop
        main_loop = 0
    else:
        print("user input is non renge menu")

def calculation_fahrenheit():
    global convertation_cf
    clear_consol()
    input_user_value()
    convertation_cf = convertor_cf(user_input_value)
    log_creator(convertation_cf)
    print_cf(convertation_cf)

def start_menu():
    global chose_menu_section
    while(main_loop):
       welcom_displayed(display_welcom)
       display_main_menu(menu)
       chose_menu_section = select_menu_section()
       menu_option()


# << ---- Main Work ---- >>display_welcom
if __name__ == '__main__':
    start_menu()

