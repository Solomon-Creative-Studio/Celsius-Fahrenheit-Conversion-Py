# convertor Celsius to Fahrenheit


# << ---- Import ---- >>
import os
import datetime

# << ---- Variable ---- >>
welcome_Logo = " Welcome, to software. "
main_menu_sections = ['Start Work', 'Log', 'Info', 'Stop Work']
log_menu_sections = ['Session Log', 'Log for Save', 'Program Log', 'Read Save Log', 'Stop Work']

chose_menu_section = None
user_input_value = None
cf_conversion_data_log = None
cf_conversion_datatime = None

log_software_working = []
log_saved_software_working = []
log_calculate_sessions = []
log_calculate_sessions_for_save = []
log_directory_prefix = 'log'
log_items_prefix = 'log_cf.txt'
log_directory_path = None

main_loop = 1
program_stop_work = 1
mode_create = 0o755
display_welcome = 0

software_directory = os.getcwd()


# << ---- Functional function ---- >>
def welcome_displayed(welcome_logo):
    global display_welcome
    if display_welcome == 0:
        print(' ' + welcome_logo + '\n')
        display_welcome = 1


def menu_displayed(display_menu):
    for i in display_menu:
        print('    ' + str(display_menu.index(i) + 1) + ' ' + i)
    print('\n')


def dash_liner():
    dash = '-'
    repeater = 30
    liner = dash * repeater
    print(liner + '\n')


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def programs_info():
    clear_console()
    dash_liner()
    print(" This product is a simple command line converter. \n")
    print(" It converts celsius to fahrenheit entered by the user. \n")
    print(" You can view statistics of calculations per session in the section -- Info. \n")
    dash_liner()
    stop_program_or_main_menu_builder()
    clear_console()


def cf_converting(value_entered_by_the_user):
    global cf_conversion_datatime
    convert_cf = (value_entered_by_the_user * (212 - 32)) / 100 + 32
    cf_conversion_datatime = datetime.datetime.now()
    _log_data = 'cf conversion'
    log_program_work_builder(_log_data)
    return convert_cf


def cf_converting_print(conversion_cf):
    print(f' Weather is a -- {conversion_cf} F \n')


def cf_log_session_create(conversion_cf):
    global log_calculate_sessions
    log_calculate_sessions.append(conversion_cf)


def cf_log_session_reade(log_sessions):
    clear_console()
    dash_liner()
    print(' < ---- Session Log ---- > \n')
    if len(log_sessions) != 0:
        for i in log_sessions:
            print(f" Whether: {log_sessions.index(i) + 1} - {i}" + '\n')
    else:
        print(" Log is Empty " + '\n')
        _log_data = 'Session Log is Empty'
        log_program_work_builder(_log_data)
    _log_data = 'Display log sessions'
    log_program_work_builder(_log_data)
    dash_liner()
    stop_program_or_main_menu_builder()
    clear_console()


def log_directory_is_exists(path_to_soft_directory, prefix_log_directory):
    _log_dir = os.path.join(path_to_soft_directory, prefix_log_directory)
    _is_exist_dir = os.path.exists(_log_dir)
    return _is_exist_dir


def log_directory_reader(path_to_soft_directory, prefix_log_directory):
    global log_directory_path
    for i in os.listdir(path_to_soft_directory):
        if os.path.isdir(i):
            if i == prefix_log_directory:
                log_directory_path = i


def log_directory_create(path_to_soft_directory, prefix_log_directory):
    global mode_create
    global log_directory_path
    log_directory_path = os.path.join(path_to_soft_directory, prefix_log_directory)
    try:
        os.mkdir(log_directory_path, mode_create)
        _log_data = 'Create Log Directory'
        log_program_work_builder(_log_data)
    except FileExistsError:
        _log_data = 'Log Directory is not Empty'
        log_program_work_builder(_log_data)


def log_directory_delete(path_to_soft_directory, prefix_log_directory):
    _path_to_delete_dir = os.path.join(path_to_soft_directory, prefix_log_directory)
    try:
        os.rmdir(_path_to_delete_dir)
    except FileNotFoundError:
        _log_data = 'Log Directory is not exist'
        log_program_work_builder(_log_data)
    except OSError:
        _log_data = 'Log Directory not empty'
        log_program_work_builder(_log_data)


def save_log_creator():
    global cf_conversion_datatime
    global log_calculate_sessions_for_save
    global cf_conversion_data_log
    _log_date = tuple([cf_conversion_datatime, cf_conversion_data_log])
    log_calculate_sessions_for_save.append(_log_date)


def save_log_viewer(log_data_sessions):
    clear_console()
    dash_liner()
    print(' < ---- Log for Save ---- > \n')
    if len(log_data_sessions) != 0:
        for i in log_data_sessions:
            print(f" Whether: {log_data_sessions.index(i) + 1} - {str(i[0])[0:19]} - {i[1]} F" + '\n')
    else:
        print(" Log is Empty " + '\n')
        _log_data = 'Empty Log for Save'
        log_program_work_builder(_log_data)
    dash_liner()
    stop_program_or_main_menu_builder()
    clear_console()


def write_save_log_to_storage(log_path, log_data):
    with open(log_path, 'a', encoding='utf-8') as wsl:
        for i in log_data:
            wsl.writelines(str(i) + '\n')
    wsl.close()


def read_save_log_with_storage(log_path):
    _read_log = []
    with open(log_path, 'r', encoding='utf-8') as rsl:
        _read_log = rsl.readlines()
    rsl.close()
    return _read_log


def log_program_work_creator(loging_data, loging_time):
    global log_software_working
    log_software_working.append(tuple([loging_time, loging_data]))


def read_program_log(log_date):
    clear_console()
    dash_liner()
    print(' < ---- Program Work Log ---- > \n')
    if len(log_date) != 0:
        for i in log_date:
            print(f" {log_date.index(i) + 1} - {str(i[0])} - {i[1]}" + '\n')
    else:
        print(" Log is Empty " + '\n')
        _log_data = 'Program Work Log is Empty'
        log_program_work_builder(_log_data)
    dash_liner()
    stop_program_or_main_menu_builder()
    clear_console()


def select_menu_section():
    _index = 1
    menu_section = None
    while _index:
        get_user_input = input(" Entered Menu chose sections : ")
        try:
            menu_section = int(get_user_input)
        except ValueError:
            print('\n Input the number, not character \n')
            _log_data = 'User entered Menu section is not integer'
            log_program_work_builder(_log_data)
            continue
        _index = 0
    return menu_section


def user_input():
    _index = 1
    _user_input = None
    while _index:
        user_value = input(" Input the values in celsius : ")
        try:
            _user_input_value = int(user_value)
            _user_input = _user_input_value
        except ValueError:
            print("\n Value is not number. Entered the number. \n")
            _log_data = 'User entered Celsius is not Integer'
            log_program_work_builder(_log_data)
            continue
        _index = 0
        return _user_input


# << ---- Constructor function ---- >>

def log_menu_builder():
    global log_menu_sections
    clear_console()
    dash_liner()
    menu_displayed(log_menu_sections)
    dash_liner()
    _user_menu_select = select_menu_section()
    if _user_menu_select == 1:
        # ++++  Session Log  ++++
        cf_log_session_reade(log_calculate_sessions)

    elif _user_menu_select == 2:
        # ++++  Log for Save  ++++
        save_log_viewer(log_calculate_sessions_for_save)

    elif _user_menu_select == 3:
        # ++++  Program Work Log  ++++
        read_program_log(log_software_working)

    elif _user_menu_select == 4:
        # ++++  Read Save Log  ++++
        log_items_read_builder()

    elif _user_menu_select == 5:
        # ++++  Stop Work  ++++
        stop_program_or_main_menu_builder()
        clear_console()

    else:
        print(" Input is non renge menu ")
        _log_data = 'User entered number sections menu is non range log menu'
        log_program_work_builder(_log_data)


def cf_conversion_builder():
    global cf_conversion_data_log
    clear_console()
    dash_liner()
    cf_conversion_data_log = cf_converting(user_input())
    cf_log_session_create(cf_conversion_data_log)
    print('\n < ---- Calculate ---- > \n')
    cf_converting_print(cf_conversion_data_log)
    save_log_creator()
    _log_data = 'Cf convertor to convert and display result'
    log_program_work_builder(_log_data)
    dash_liner()
    stop_program_or_main_menu_builder()
    clear_console()


def log_program_work_builder(data_log):
    _date_log = datetime.datetime.now()
    log_program_work_creator(data_log, _date_log)


def log_directory_builder():
    if log_directory_is_exists(software_directory, log_directory_prefix):
        log_directory_reader(software_directory, log_directory_prefix)
    else:
        log_directory_create(software_directory, log_directory_prefix)


def log_items_write_builder():
    global log_directory_path
    global log_items_prefix
    global log_software_working
    _log_data = []
    for i in log_software_working:
        _log_data.append(f" {log_software_working.index(i) + 1} - {str(i[0])} - {i[1]}")
    _log_items_path = os.path.join(log_directory_path, log_items_prefix)
    write_save_log_to_storage(_log_items_path, _log_data)


def log_items_read_builder():
    global log_items_prefix
    global log_directory_prefix
    global log_saved_software_working
    clear_console()
    dash_liner()
    _log_items_path = os.path.join(log_directory_prefix, log_items_prefix)
    _log_data = read_save_log_with_storage(_log_items_path)
    for i in _log_data:
        print(i)
    dash_liner()
    stop_program_or_main_menu_builder()
    clear_console()


def stop_program_or_main_menu_builder():
    global program_stop_work
    global main_loop
    _user_input = None
    try:
        _user_input = input(" Enter the 'y' - to stop. or pressed Enter : ")
    except ValueError:
        print("\n Entered is not 'y' or 'Enter' \n")
    if _user_input == 'y' or _user_input == 'Y':
        main_loop = 0
        program_stop_work = 1
        _log_data = 'User stopped work software'
        log_program_work_builder(_log_data)
        return 0
    else:
        _log_data = 'User to continue work'
        log_program_work_builder(_log_data)
        return 1


def main_menu_builder():
    global chose_menu_section
    global main_loop
    while main_loop:
        clear_console()
        dash_liner()
        welcome_displayed(welcome_Logo)
        menu_displayed(main_menu_sections)
        dash_liner()
        log_directory_builder()
        chose_menu_section = select_menu_section()
        if program_stop_work == 1:
            if chose_menu_section == 1:
                # ++++  Start Work  ++++
                cf_conversion_builder()

            elif chose_menu_section == 2:
                # ++++  Log  ++++
                log_menu_builder()

            elif chose_menu_section == 3:
                # ++++  Info  ++++
                programs_info()

            elif chose_menu_section == 4:
                # ++++  Stop Work  ++++
                main_loop = 0
                _log_data = 'User stopped work software'
                log_program_work_builder(_log_data)
                clear_console()
            else:
                print(" User input is non renge menu ")
                _log_data = 'User entered number section is non rang main menu range'
                log_program_work_builder(_log_data)
        else:
            main_loop = 0
            _log_data = 'User Exit Software'
            log_program_work_builder(_log_data)
    _log_data = 'User Exit Software'
    log_program_work_builder(_log_data)
    log_items_write_builder()


# << ---- Main Work ---- >>
if __name__ == '__main__':
    main_menu_builder()
