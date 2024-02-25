#  Let's do it!!

# Importing required modules
from tkinter import *
from PIL import ImageTk
from time import strftime


#  User Input Processing
def user_input(type_value, value):
    global converted, type_converted
    converted = ''
    type_converted = ''

    # To process and confirm data type if not known
    # Also converting data to required type
    if type_value == 'unknown':
        c = 0
        if value.isdigit():
            user_input('int', value)
            c = 1
        if '.' in value:
            user_input('float', value)
        if ',' in value:
            if value[0] + value[-1] == '[]':
                user_input('list', value)
                c = 1
            elif value[0] + value[-1] == '()':
                user_input('tuple', value)
                c = 1
            elif value[0] + value[-1] == '{}':
                user_input('dict', value)
                c = 1
            else:
                user_input('tuple', value)
                c = 1
        if value in 'TrueFalse':
            user_input('bool', value)
            c = 1
        if c == 0:
            user_input('str', value)

    # To process and confirm data as int
    # Also converting data to int
    if type_value == 'int':
        try:
            converted = int(value)
            type_converted = int
        except:
            user_input('str', value)

    # To process and confirm data as float
    # Also converting data to float
    if type_value == 'float':
        try:
            converted = float(value)
            type_converted = float
        except:
            user_input('str', value)

    # To process and confirm data as num
    # Also converting data to num
    if type_value == 'num':
        try:
            try:
                converted = int(value)
                type_converted = int
            except:
                converted = float(value)
                type_converted = float
        except ValueError:
            user_input('str', value)

    # To process and confirm data as list
    # Also converting data to list
    if type_value == 'list':
        if value[0] + value[-1] == '[]':
            value = value[1:-1]
        try:
            l = value.split(',')
            x = len(l)
            for i in l[:x]:
                i = i.strip()
                user_input('unknown', i)
                l.append(converted)
            converted = l[x:]
            type_converted = list
        except:
            user_input('str', value)

    # To process and confirm data as tuple
    # Also converting data to tuple
    if type_value == 'tuple':
        if value[0] + value[-1] == '()':
            value = value[1:-1]
        try:
            l = value.split(',')
            x = len(l)
            for i in l[:x]:
                i = i.strip()
                user_input('unknown', i)
                l.append(converted)
            converted = l[x:]
            converted = tuple(converted)
            type_converted = tuple
        except:
            user_input('str', value)

    # To process and confirm data as dict
    # Also converting data to dict
    if type_value == 'dict':
        if value[0] + value[-1] == '{}':
            value = value[1:-1]
        try:
            l = value.split(',')
            x = len(l)
            for i in l[:x]:
                user_input('str', i)
                l.append(converted)
            d = dict()
            for j in l:
                d_key = ((j.partition(':'))[0]).strip()
                user_input('unknown', d_key)
                d_key = converted
                d_value = ((j.partition(':'))[-1]).strip()
                user_input('unknown', d_value)
                d_value = converted
                d[d_key] = d_value
            converted = d
            type_converted = dict
        except:
            user_input('str', value)

    # To process and confirm data as str
    # Also converting data to str
    if type_value == 'str':
        converted = value
        type_converted = str

    # To process and confirm data as bool
    # Also converting data to bool
    if type_value == 'bool':
        if value in 'True':
            converted = True
            type_converted = bool
        elif value in 'False':
            converted = False
            type_converted = bool
        else:
            user_input('str', value)


def home():
    main.destroy()
# Making of global varibles to call the functions through out the program

    global home_menu, home_menu_id, change_menu, change_menu_id, display_menu, display_menu_id, \
        search_menu, search_menu_id, state_menu, state_menu_id

# Making a database function to call all the required elements including images and text files
# Made a common file so that it will not affect any of the user with GUI and calling it through out the program

    def database():
        global data

# Calling the text file WORLD_HERITAGE_SITES having the total database as a string from the file named App Requirments

        my_file = open("App Requirements/WORLD_HERITAGE_SITES.txt", "r")
        file_contents = my_file.readlines() # Reading of each lines from the text file
        my_file.close()
        data = dict() # File converted to dictionary by slicing
        count = 1
        for i in file_contents:

# Slicing of the text file starts from here as required in the later part of the program during showing different informations of the world heritages

            i = i[1:-1]

            t = i.partition(':')
            t = list(t)
            z = 1
            data[t[0][z:-1]] = dict()
            colon = (t[-1][1:-2]).index(':')
            period = t[-1].index('Period')
            comma = (t[-1][period:1:-1]).index(',')
            comma = len(t[-1][period:1:-1]) - comma
            data[t[0][z:-1]]['State'] = t[-1][colon + 3:comma]
            t[-1] = t[-1][comma + 2:-2]
            colon = t[-1].index(':')
            description = t[-1].index('Description')
            comma = (t[-1][description::-1]).index(',')
            comma = len(t[-1][description::-1]) - comma - 1
            data[t[0][z:-1]]['Time'] = t[-1][colon + 2:comma - 1]
            t[-1] = t[-1][comma + 1:]
            colon = t[-1].index(':')
            data[t[0][z:-1]]['Info'] = t[-1][colon + 2:-1]
            count += 1

    database()

# Till now the backend was happening now thw frontend GUI starts from here
# GUI Login

    def GUI_home():
        global main_home, image_bg, bg_canvas #Global variables are created

# Dimension of the root window

        main_width = 650
        main_height = 650
        main_home = Tk()

# Main window framework starts
# Dimension of main window

        main_home.title('UNESCO Project Application')
        screen_width = main_home.winfo_screenwidth()
        screen_height = main_home.winfo_screenheight()
        main_home.geometry(f'{main_width}x{main_height}+{(int((screen_width - main_width) / 2))}+'
                           f'{(int((screen_height - main_height) // 2) - 40)}')
        main_home.maxsize(main_width, main_height)
        main_home.minsize(main_width, main_height)

# Background image and icon framework

        main_home.iconbitmap("App Requirements/UNESCO App Icon.ico") # Logo of the software
        image_bg = ImageTk.PhotoImage(file="App Requirements/homepage_UNESCO_canva.png") # Background image of the software login screen

# Dimension of the background image

        bg_canvas = Canvas(main_home, bg='white', bd=0, highlightthickness=0)
        bg_canvas.pack(side=RIGHT, anchor=CENTER, fill=BOTH, expand=TRUE)
        bg_canvas.create_image(0, 0, image=image_bg, anchor=NW, tags='bg_canvas')

    GUI_home()

    def canvas_heading():

# Making of global variable to show the user id in the second page during execution as a heading
# Dimensions of the Heading


        global user_id
        bg_canvas.create_text(195, 80, text='Hi!', font=('BankGothic', 70), fill='#E9E8E8', anchor=W)
        bg_canvas.create_text(345, 95, text='User', font=('Bank Gothic', 40), fill='#E9E8E8', anchor=SW)
        user_id = user_id
        bg_canvas.create_text(350, 85, text=user_id, font=('Courier New', 24, 'bold'), fill='#E9E8E8', anchor=NW)

    def time():

# Making a global variable to make a time stamp to show the current time to the user
# Dimensions of the time stamp

        canvas_heading()
        global label_time
        lbl_time = Label(bg_canvas, font=('Calibri', 12, 'bold'), background='#702666', foreground='#fff5fa')
        label_time = bg_canvas.create_window(606, 143, window=lbl_time)
        string = strftime('%H:%M:%S Hrs')
        lbl_time.config(text=string)
        lbl_time.after(1000, time)

    def active(button):
        time() # Calling of the time function

# Making of a global variable for conataining the active butttons

        global home_menu, bg_canvas
        widgets = bg_canvas.find_withtag(button)

# WIDGET 1- Home Menu and its corresponding widgets colour change during hovering over the home menu widget

        if button == 'home_menu' and len(widgets) == 1:
            home_menu.configure(bg='#E4D8D6')
            change_menu.configure(bg='#FFF1EF')
            display_menu.configure(bg='#FFF1EF')
            search_menu.configure(bg='#FFF1EF')
            state_menu.configure(bg='#FFF1EF')

# WIDGET 2- Change Menu and its corresponding widgets colour change during hovering over the change menu widget

        elif button == 'change_menu' and len(widgets) == 1:
            change_menu.configure(bg='#E4D8D6')
            home_menu.configure(bg='#FFF1EF')
            display_menu.configure(bg='#FFF1EF')
            search_menu.configure(bg='#FFF1EF')
            state_menu.configure(bg='#FFF1EF')

# WIDGET 3- Dispaly Menu and its corresponding widgets colour change during hovering over the display menu widget

        elif button == 'display_menu':
            display_menu.configure(bg='#E4D8D6')
            home_menu.configure(bg='#FFF1EF')
            change_menu.configure(bg='#FFF1EF')
            search_menu.configure(bg='#FFF1EF')
            state_menu.configure(bg='#FFF1EF')

# WIDGET 4- Search Menu and its corresponding widgets colour change during hovering over the search menu widget

        elif button == 'search_menu':
            search_menu.configure(bg='#E4D8D6')
            home_menu.configure(bg='#FFF1EF')
            change_menu.configure(bg='#FFF1EF')
            display_menu.configure(bg='#FFF1EF')
            state_menu.configure(bg='#FFF1EF')

# WIDGET 5- State Menu and its corresponding widgets colour change during hovering over the state menu widget

        elif button == 'state_menu':
            state_menu.configure(bg='#E4D8D6')
            home_menu.configure(bg='#FFF1EF')
            change_menu.configure(bg='#FFF1EF')
            display_menu.configure(bg='#FFF1EF')
            search_menu.configure(bg='#FFF1EF')

    def clear():

# Making of global variables to show the icons and the data on the screen

        global home_menu_id, state_menu_id, change_menu_id, search_menu_id, display_menu_id, bg_canvas
        widgets = bg_canvas.find_all()
        menu_options = [home_menu_id, state_menu_id, change_menu_id, search_menu_id, display_menu_id, label_time]
        for i in widgets:
            if i not in menu_options:
                bg_canvas.delete(i)

    def home_page():

# Activation of WIDGET 1

        global bg_canvas, image_bg
        clear()
        active('home_menu')
        image_bg = ImageTk.PhotoImage(file="App Requirements/homepage_UNESCO_Canva_go_to_home.png") # Background image
        bg_canvas.create_image(0, 0, image=image_bg, anchor=NW, tags='bg_canvas')
        canvas_heading()

# Addition of the labels to show the text on the WIDGET 1

        about_label_1 = bg_canvas.create_text(230, 200, text='WELCOME', font=('HoboStd', 44), justify='center',
                                              anchor=NW)
        about_label_2 = bg_canvas.create_text(295, 280, text='About us-', font=('Another Day', 40), justify='center',
                                              anchor=NW)

# About UNESCO as a label

        about_unesco = '''The United Nations Educational, 
        Scientific and Cultural Organization (UNESCO)
        World Heritage Sites are the important places of
        cultural or natural heritage as described in the
        UNESCO World Heritage Convention, established
        in 1945. India accepted the convention on 14
        November 1977, making its sites eligible for
        inclusion on the list.'''
        about_label_3 = bg_canvas.create_text(70, 340, text=about_unesco, font=('Tw Cen MT', 19), justify='center',
                                              anchor=NW)

    def home_menu_hover(e):

# Hovering over WIDGET 1 and showing text

        global x
        x = Label(bg_canvas, bg='snow', fg='gray10', bd=5, text='HOME PAGE', font=('Leelawadee', 9))
        bg_canvas.create_window(100, 205, window=x, anchor=NW)

    def home_menu_leave(e):
        global x
        x.destroy()

# Making of WIDGET 1 icon containing dimension,colour,background image,functionality of the widget
# WIDGET 1 has option of GO TO HOME PAGE

    home_menu_image = ImageTk.PhotoImage(
        file="App Requirements/UNESCO Menu Options  transparent 1.png")
    home_menu = Menubutton(bg_canvas, image=home_menu_image, bd=0, bg='#FFF1EF', activebackground='#E4D8D6',
                           highlightthickness=0, direction=RIGHT, width=81, height=87)
    home_menu_id = bg_canvas.create_window(0, 195, window=home_menu, anchor=NW, tag='home_menu')
    home_menu.bind('<Enter>', home_menu_hover)
    home_menu.bind('<Leave>', home_menu_leave)
    home = Menu(home_menu, tearoff=0, font=('Garamond', 15, 'bold'), activebackground='#edbbe6',
                activeforeground='#3b373a',
                fg='#2e2b28')
    home_menu.configure(menu=home)
    home.add_command(label='Go to Home Page', command=home_page)

    def change_page(option):

# Changing of page and going to WIDGET 2
# Making of WIDGET 2 icon containing dimension,colour,background image,functionality of the widget
# WIDGET 2 containing 3 options- ADD,MODIFY,DELETE

        global image_bg, bg_canvas, data
        active('change_menu')
        if option in 'add modify delete':
            clear()
            image_bg = ImageTk.PhotoImage(file="App Requirements/homepage_UNESCO_canva.png")
            bg_canvas.create_image(0, 0, image=image_bg, anchor=NW, tags='bg_canvas')
        if option == 'add':

# Making of ADD function containing dimension,colour,background image,functionality of the button and labels

            add_tab_label = Label(text='ADD NEW SITE', font=('Verdana', 20), bg='#FF8A1D',
                                  fg='#FFFFFF')
            add_tab_label_id = bg_canvas.create_window(475, 170, window=add_tab_label, anchor=NE)
            site_name_label = bg_canvas.create_text(300, 235, text='Enter the name of site:', font=('Georgia', 16),
                                                    fill='black', anchor=NE)
            site_name_entry = Entry(bg_canvas, width=35, fg='#3b3b3b', bg='snow', font=('Microsoft Uighur', 20), bd=0,
                                    justify='center')
            bg_canvas.create_window(305, 230, window=site_name_entry, anchor=NW)

            def add():

# Making of what will happen after clicking the ADD button

                site = site_name_entry.get()
                add_widgets = ['message', 'add_site_state_label', 'add_site_state_entry', 'add_site_date_label',
                               'add_site_date_label_2', 'add_site_date_entry_1', 'add_site_date_entry_2',
                               'submit_details',
                               'add_site_info_label', 'add_site_date_label_1', 'add_site_info_entry',
                               'add_site_built_label', 'add_site_built_entry']
                sites_list = list()
                for i in data.keys():
                    sites_list.append(i.lower())
                if site.lower() in sites_list or site == '':
                    for i in add_widgets:
                        bg_canvas.delete(i)

# Showing different messages in different situations

                    bg_canvas.create_text(250, 275, text='Entered site is already present in database\n' # When site already available in the dictionary
                                                         'Try Modify tab or enter another site above', fill='red',
                                          font=('Helvetica', 13), justify='center', anchor=N, tags='message')
                else:
                    for i in add_widgets:
                        bg_canvas.delete(i)
                    bg_canvas.create_text(250, 275, text='Entered site is a new addition\n' # When site entered is not present in the dictionary
                                                         'Add rest of the details below', fill='green',
                                          font=('Helvetica', 13), justify='center', anchor=N, tags='message')
                    add_site_state_label = bg_canvas.create_text(300, 335, text='State of site:',
                                                                 font=('Georgia', 16), fill='black',
                                                                 anchor=NE, tags='add_site_state_label')
                    add_site_state_entry = Entry(bg_canvas, width=35, fg='#3b3b3b', bg='snow',
                                                 font=('Microsoft Uighur', 20), bd=0, justify='center')
                    bg_canvas.create_window(305, 330, window=add_site_state_entry, anchor=NW,
                                            tags='add_site_state_entry')
                    add_site_date_label = bg_canvas.create_text(320, 395, text='Period of construction\n'
                                                                               '[format- ddmmyyyy]', justify='center',
                                                                font=('Georgia', 16), fill='black',
                                                                anchor=NE, tags='add_site_date_label')
                    add_site_date_label_1 = bg_canvas.create_text(390, 385, text='Start:', justify='center',
                                                                  font=('Georgia', 16), fill='black', anchor=NE,
                                                                  tags='add_site_date_label_1')
                    add_site_date_label_2 = bg_canvas.create_text(390, 430, text='End:', justify='center',
                                                                  font=('Georgia', 16), fill='black', anchor=NE,
                                                                  tags='add_site_date_label_2')
                    add_site_date_entry_1 = Entry(bg_canvas, width=20, fg='#3b3b3b', bg='snow',
                                                  font=('Microsoft Uighur', 20), bd=0, justify='center')
                    bg_canvas.create_window(395, 380, window=add_site_date_entry_1, anchor=NW,
                                            tags='add_site_date_entry_1')
                    add_site_date_entry_2 = Entry(bg_canvas, width=20, fg='#3b3b3b', bg='snow',
                                                  font=('Microsoft Uighur', 20), bd=0, justify='center')
                    bg_canvas.create_window(395, 425, window=add_site_date_entry_2, anchor=NW,
                                            tags='add_site_date_entry_2')
                    add_site_info_label = bg_canvas.create_text(300, 475, text='Site info:',
                                                                font=('Georgia', 16), fill='black',
                                                                anchor=NE, tags='add_site_info_label')
                    add_site_info_entry = Entry(bg_canvas, width=35, fg='#3b3b3b', bg='snow',
                                                font=('Microsoft Uighur', 20),
                                                bd=0, justify='center')
                    bg_canvas.create_window(305, 470, window=add_site_info_entry, anchor=NW, tags='add_site_info_entry')

                    def submit():

# Making of the submit button function when under ADD
# Options of all the necessery information needed for creation of new site will show where the user can input the data
# Storing of the data in the text file

                        site_data = dict()
                        site_data['State'] = add_site_state_entry.get()
                        site_data['Time'] = ((add_site_date_entry_1.get()) + ' to ' + (add_site_date_entry_2.get()))
                        site_data['Info'] = add_site_info_entry.get()
                        data[site] = site_data
                        entered_data = dict()
                        entered_data[site] = site_data
                        my_file = open("App Requirements/WORLD_HERITAGE_SITES.txt", "a")
                        my_file.write('\n' + str(entered_data))
                        my_file.close()
                        change_page('add')

                    submit_details = Button(bg_canvas, text='SUBMIT', bd=0, highlightthickness=0, bg='#78286d',
                                            activebackground='#9e4d93', activeforeground='#ebf6ff', fg='#ebf6ff',
                                            font=('Microsoft Uighur', 18, 'bold'), height=0, width=20, command=submit)
                    bg_canvas.create_window(622, 580, window=submit_details, anchor=NE, tags='submit_details')

            site_name_check_button = Button(bg_canvas, text='CHECK IF PRESENT', bd=0, highlightthickness=0,
                                            bg='#0f5087',
                                            activebackground='#1c72ba', activeforeground='#ebf6ff', fg='#ebf6ff',
                                            font=('Microsoft Uighur', 18, 'bold'), height=0, width=20, command=add)
            bg_canvas.create_window(622, 275, window=site_name_check_button, anchor=NE)




        if option == 'modify':

# Making of MODIFY function containing dimension,colour,background image,functionality of the button and labels

            modify_tab_label = Label(text='MODIFY SITE DETAILS', font=('Verdana', 20), bg='#FF8A1D',
                                     fg='#FFFFFF')
            modify_tab_label_id = bg_canvas.create_window(530, 170, window=modify_tab_label, anchor=NE)
            site_name_label = bg_canvas.create_text(300, 235, text='Enter the name of site:', font=('Georgia', 16),
                                                    fill='black', anchor=NE)
            site_name_entry = Entry(bg_canvas, width=35, fg='#3b3b3b', bg='snow', font=('Microsoft Uighur', 20), bd=0,
                                    justify='center')
            bg_canvas.create_window(305, 230, window=site_name_entry, anchor=NW)

            def modify():

# Making of what will happen after clicking the MODIFY button

                site = site_name_entry.get()
                add_widgets = ['message', 'add_site_state_label', 'add_site_state_entry', 'add_site_date_label',
                               'add_site_date_label_2', 'add_site_date_entry_1', 'add_site_date_entry_2',
                               'submit_details',
                               'add_site_info_label', 'add_site_date_label_1', 'add_site_info_entry',
                               'add_site_built_label', 'add_site_built_entry']
                sites_list = list()
                for i in data.keys():
                    sites_list.append(i.lower())
                if site.lower() not in sites_list or site == '':
                    for i in add_widgets:
                        bg_canvas.delete(i)

# Showing different messages in different situations

                    bg_canvas.create_text(250, 275, text='Entered site is a new addition\n' # When site not available in the database
                                                         'Try Add tab or enter another site above', fill='red',
                                          font=('Helvetica', 13), justify='center', anchor=N, tags='message')
                else:
                    for i in add_widgets:
                        bg_canvas.delete(i)
                    bg_canvas.create_text(250, 275, text='Entered site is present in database\n' # When site already available in the dictionary
                                                         'Add rest of the modified details below', fill='green',
                                          font=('Helvetica', 13), justify='center', anchor=N, tags='message')
                    add_site_state_label = bg_canvas.create_text(300, 335, text='State of site:',
                                                                 font=('Georgia', 16), fill='black', anchor=NE,
                                                                 tags='add_site_state_label')
                    add_site_state_entry = Entry(bg_canvas, width=35, fg='#3b3b3b', bg='snow',
                                                 font=('Microsoft Uighur', 20), bd=0, justify='center')
                    bg_canvas.create_window(305, 330, window=add_site_state_entry, anchor=NW,
                                            tags='add_site_state_entry')
                    add_site_date_label = bg_canvas.create_text(320, 395, text='Period of construction\n'
                                                                               '[format- ddmmyyyy]', justify='center',
                                                                font=('Georgia', 16), fill='black', anchor=NE,
                                                                tags='add_site_date_label')
                    add_site_date_label_1 = bg_canvas.create_text(390, 385, text='Start:', justify='center',
                                                                  font=('Georgia', 16), fill='black', anchor=NE,
                                                                  tags='add_site_date_label_1')
                    add_site_date_label_2 = bg_canvas.create_text(390, 430, text='End:', justify='center',
                                                                  font=('Georgia', 16), fill='black', anchor=NE,
                                                                  tags='add_site_date_label_2')
                    add_site_date_entry_1 = Entry(bg_canvas, width=20, fg='#3b3b3b', bg='snow',
                                                  font=('Microsoft Uighur', 20), bd=0, justify='center')
                    bg_canvas.create_window(395, 380, window=add_site_date_entry_1, anchor=NW,
                                            tags='add_site_date_entry_1')
                    add_site_date_entry_2 = Entry(bg_canvas, width=20, fg='#3b3b3b', bg='snow',
                                                  font=('Microsoft Uighur', 20), bd=0, justify='center')
                    bg_canvas.create_window(395, 425, window=add_site_date_entry_2, anchor=NW,
                                            tags='add_site_date_entry_2')
                    add_site_info_label = bg_canvas.create_text(300, 475, text='Site info:',
                                                                font=('Georgia', 16), fill='black',
                                                                anchor=NE, tags='add_site_info_label')
                    add_site_info_entry = Entry(bg_canvas, width=35, fg='#3b3b3b', bg='snow',
                                                font=('Microsoft Uighur', 20),
                                                bd=0, justify='center')
                    bg_canvas.create_window(305, 470, window=add_site_info_entry, anchor=NW, tags='add_site_info_entry')

                    def submit():

# Making of the submit button function when under MODIFY
# Options of all the necessery information needed for modyfing the data will show where the user can input the data

                        site_data = dict()
                        data[site] = dict()
                        site_data['State'] = add_site_state_entry.get()
                        site_data['Time'] = ((add_site_date_entry_1.get()) + ' to ' + (add_site_date_entry_2.get()))
                        site_data['Info'] = add_site_info_entry.get()
                        change_page('modify')

                    submit_details = Button(bg_canvas, text='SUBMIT', bd=0, highlightthickness=0, bg='#78286d',
                                            activebackground='#9e4d93', activeforeground='#ebf6ff', fg='#ebf6ff',
                                            font=('Microsoft Uighur', 18, 'bold'), height=0, width=20, command=submit)
                    bg_canvas.create_window(622, 580, window=submit_details, anchor=NE, tags='submit_details')

            site_name_check_button = Button(bg_canvas, text='CHECK IF PRESENT', bd=0, highlightthickness=0,
                                            bg='#0f5087',
                                            activebackground='#1c72ba', activeforeground='#ebf6ff', fg='#ebf6ff',
                                            font=('Microsoft Uighur', 18, 'bold'), height=0, width=20, command=modify)
            bg_canvas.create_window(622, 275, window=site_name_check_button, anchor=NE)
        if option == 'delete':
            delete_tab_label = Label(text='DELETE SITE DETAILS', font=('Verdana', 20), bg='#FF8A1D',
                                     fg='#FFFFFF')
            delete_tab_label_id = bg_canvas.create_window(530, 170, window=delete_tab_label, anchor=NE)
            site_name_label = bg_canvas.create_text(300, 235, text='Enter the name of site:', font=('Georgia', 16),
                                                    fill='black', anchor=NE)
            site_name_entry = Entry(bg_canvas, width=35, fg='#3b3b3b', bg='snow', font=('Microsoft Uighur', 20), bd=0,
                                    justify='center')
            bg_canvas.create_window(305, 230, window=site_name_entry, anchor=NW)

            def delete():

# Making of DELETE function containing dimension,colour,background image,functionality of the button and labels

                site = site_name_entry.get()
                add_widgets = ['message', 'confirm_site_label', 'confirm_site_entry', 'submit_details']
                sites_list = list()
                for i in data.keys():
                    sites_list.append(i.lower())
                if site.lower() not in sites_list or site == '':
                    for i in add_widgets:
                        bg_canvas.delete(i)

# Showing different messages in different situations

                    bg_canvas.create_text(250, 275, text='Entered site is a new addition\n' # When the site not available in the dictionary
                                                         'Try Add tab or enter another site above', fill='red',
                                          font=('Helvetica', 13), justify='center', anchor=N, tags='message')
                else:
                    for i in add_widgets:
                        bg_canvas.delete(i)
                    bg_canvas.create_text(250, 275, text='Entered site is already present in database\n' # When available in the the dictionary
                                                         'Confirm site below', fill='green',
                                          font=('Helvetica', 13), justify='center', anchor=N, tags='message')
                    confirm_site_label = bg_canvas.create_text(300, 335, text='Confirm site:',
                                                               font=('Georgia', 16), fill='black', anchor=NE,
                                                               tags='confirm_site_label')
                    confirm_site_entry = Entry(bg_canvas, width=35, fg='#3b3b3b', bg='snow',
                                               font=('Microsoft Uighur', 20), bd=0, justify='center')
                    bg_canvas.create_window(305, 330, window=confirm_site_entry, anchor=NW, tags='confirm_site_entry')

                    def submit():

# Making of the submit button function when under DELETE
# Options of deleteing the site permenently from the dictionary


                        if confirm_site_entry.get() == site:
                            del data[site]
                            my_file = open("App Requirements/WORLD_HERITAGE_SITES.txt", "r")
                            file_contents = my_file.readlines()
                            my_file.close()
                            for i in range(len(file_contents)):
                                colon = file_contents[i].index(':')
                                if site in file_contents[i][:colon]:
                                    del file_contents[i]
                                    break
                            my_file = open("App Requirements/WORLD_HERITAGE_SITES.txt", "w")
                            my_file.writelines(file_contents)
                            my_file.close()
                            change_page('delete')
                        else:

# Showing message for rechecking the site name

                            bg_canvas.delete('message_confirm')
                            bg_canvas.create_text(250, 380, text='Unable to delete\nRecheck confirmation', fill='red',
                                                  font=('Helvetica', 13), justify='center', anchor=N,
                                                  tags='message_confirm')

                    submit_details = Button(bg_canvas, text='SUBMIT', bd=0, highlightthickness=0, bg='#78286d',
                                            activebackground='#9e4d93', activeforeground='#ebf6ff', fg='#ebf6ff',
                                            font=('Microsoft Uighur', 18, 'bold'), height=0, width=20, command=submit)
                    bg_canvas.create_window(622, 380, window=submit_details, anchor=NE, tags='submit_details')

            site_name_check_button = Button(bg_canvas, text='CHECK IF PRESENT', bd=0, highlightthickness=0,
                                            bg='#0f5087',
                                            activebackground='#1c72ba', activeforeground='#ebf6ff', fg='#ebf6ff',
                                            font=('Microsoft Uighur', 18, 'bold'), height=0, width=20, command=delete)
            bg_canvas.create_window(622, 275, window=site_name_check_button, anchor=NE)
            pass
        canvas_heading()

    def change_menu_hover(e):

# Hovering over WIDGET 2 and showing text

        global x
        x = Label(bg_canvas, bg='snow', fg='gray10', bd=5, text='ADD, MODIFY OR DELETE DETAILS', font=('Leelawadee', 9))
        bg_canvas.create_window(100, 296, window=x, anchor=NW)

    def change_menu_leave(e):
        global x
        x.destroy()

# Making of WIDGET 2 icon containing dimension,colour,background image,functionality of the widget
# WIDGET 2 has option of ADD, MODIFY and DELETE

    change_menu_image = ImageTk.PhotoImage(
        file="App Requirements/UNESCO Menu Options  transparent 2.png")
    change_menu = Menubutton(bg_canvas, image=change_menu_image, bd=0, bg='#FFF1EF', activebackground='#E4D8D6',
                             highlightthickness=0, direction=RIGHT, width=81, height=87)
    change_menu_id = bg_canvas.create_window(0, 286, window=change_menu, anchor=NW, tags='change_menu')
    change_menu.bind('<Enter>', change_menu_hover)
    change_menu.bind('<Leave>', change_menu_leave)
    change = Menu(change_menu, tearoff=0, font=('Garamond', 15, 'bold'), activebackground='#edbbe6',
                  activeforeground='#3b373a', fg='#2e2b28')
    change_menu.configure(menu=change)
    change.add_command(label='Add', command=lambda: change_page('add'))
    change.add_command(label='Modify', command=lambda: change_page('modify'))
    change.add_command(label='Delete', command=lambda: change_page('delete'))

    def display_page(option):

# Making of WIDGET 3 icon containing dimension,colour,background image,functionality of the widget
# WIDGET 3 containing 2 options- ALL SITES AND TOP 10 SITES

        global image_bg, bg_canvas
        active('display_menu') # Activation of display menu

# When TOP 10 SITES clicked
# Making of the GUI
# Configuring the text appearance by indexing

        if option in 'Top 10 All Sites':
            clear()
            image_bg = ImageTk.PhotoImage(file="App Requirements/homepage_UNESCO_canva.png")
            bg_canvas.create_image(0, 0, image=image_bg, anchor=NW, tags='bg_canvas')
        if option == 'Top 10':
            top_10_tab_label = Label(text='DISPLAY TOP 10 SITES', font=('Verdana', 20), bg='#FF8A1D',
                                     fg='#FFFFFF')
            top_10_tab_label_id = bg_canvas.create_window(530, 170, window=top_10_tab_label, anchor=NE)

            text_frame = Frame(bg_canvas)
            text_scrollbar = Scrollbar(text_frame, orient=VERTICAL)
            text_scrollbar.pack(side=RIGHT, fill=Y)
            top_10 = Text(text_frame, width=60, height=20, wrap=WORD, bd=0, bg='#FBFBFF', selectbackground='#BD89B6',
                          spacing1=3, state=DISABLED, yscrollcommand=text_scrollbar.set)
            top_10.pack()
            text_scrollbar.configure(command=top_10.yview)
            bg_canvas.create_window(130, 230, window=text_frame, anchor=NW, tags='text_frame')

            display_data = list(data.keys())
            top_10.configure(state=NORMAL)
            site_index = 1.0
            for i in display_data[:10]:
                s = ('SITE: ' + i + '\n' + 'LOCATED AT: ' + data[i]['State'] + '\n' + 'PERIOD: ' + data[i][
                    'Time'] + '\n' +
                     'ABOUT THE SITE: ' + data[i]['Info'] + '\n' + '-' * 60 + '\n')
                top_10.insert(END, s)
                top_10.tag_add('SITE', site_index, site_index + 0.5)
                top_10.tag_add('Site', site_index + 0.6, site_index + 1)
                site_index += 1
                top_10.tag_add('LOCATION', site_index, site_index + 0.11)
                top_10.tag_add('Location', site_index + 0.11, site_index + 1)
                site_index += 1
                top_10.tag_add('TIME', site_index, site_index + 0.7)
                top_10.tag_add('Time', site_index + 0.7, site_index + 1)
                site_index += 1
                top_10.tag_add('INFO', site_index, site_index + 0.15)
                top_10.tag_add('Info', site_index + 0.15, site_index + 1)
                site_index += 2
            top_10.insert(END, ('-' * 60))
            top_10.tag_configure(tagName='SITE', font=('Georgia', 14))
            top_10.tag_configure(tagName='LOCATION', font=('Georgia', 11))
            top_10.tag_configure(tagName='TIME', font=('Georgia', 11))
            top_10.tag_configure(tagName='INFO', font=('Georgia', 11))
            top_10.tag_configure(tagName='Site', font=('Microsoft Uighur', 20, 'underline'))
            top_10.tag_configure(tagName='Location', font=('Microsoft Uighur', 18))
            top_10.tag_configure(tagName='Time', font=('Microsoft Uighur', 18))
            top_10.tag_configure(tagName='Info', font=('Microsoft Uighur', 18))
            top_10.configure(state=DISABLED)

# When TOP 10 SITES clicked
# Making of the GUI
# Configuring the text appearance by indexing

        if option == 'All Sites':
            all_sites_tab_label = Label(text='DISPLAY ALL SITES', font=('Verdana', 20), bg='#FF8A1D',
                                        fg='#FFFFFF')
            all_sites_tab_label_id = bg_canvas.create_window(505, 170, window=all_sites_tab_label, anchor=NE)

            text_frame = Frame(bg_canvas)
            text_scrollbar = Scrollbar(text_frame, orient=VERTICAL)
            text_scrollbar.pack(side=RIGHT, fill=Y)
            all_sites = Text(text_frame, width=60, height=20, wrap=WORD, bd=0, bg='#FBFBFF', selectbackground='#BD89B6',
                             spacing1=3, state=DISABLED, yscrollcommand=text_scrollbar.set)
            all_sites.pack()
            text_scrollbar.configure(command=all_sites.yview)
            bg_canvas.create_window(130, 230, window=text_frame, anchor=NW, tags='text_frame')

            display_data = list(data.keys())
            all_sites.configure(state=NORMAL)
            site_index = 1.0
            for i in display_data:
                s = ('SITE: ' + i + '\n' + 'LOCATED AT: ' + data[i]['State'] + '\n' + 'PERIOD: ' + data[i][
                    'Time'] + '\n' +
                     'ABOUT THE SITE: ' + data[i]['Info'] + '\n' + '-' * 60 + '\n')
                all_sites.insert(END, s)
                all_sites.tag_add('SITE', site_index, site_index + 0.5)
                all_sites.tag_add('Site', site_index + 0.6, site_index + 1)
                site_index += 1
                all_sites.tag_add('LOCATION', site_index, site_index + 0.11)
                all_sites.tag_add('Location', site_index + 0.11, site_index + 1)
                site_index += 1
                all_sites.tag_add('TIME', site_index, site_index + 0.7)
                all_sites.tag_add('Time', site_index + 0.7, site_index + 1)
                site_index += 1
                all_sites.tag_add('INFO', site_index, site_index + 0.15)
                all_sites.tag_add('Info', site_index + 0.15, site_index + 1)
                site_index += 2
            all_sites.insert(END, ('-' * 60))
            all_sites.tag_configure(tagName='SITE', font=('Georgia', 14))
            all_sites.tag_configure(tagName='LOCATION', font=('Georgia', 11))
            all_sites.tag_configure(tagName='TIME', font=('Georgia', 11))
            all_sites.tag_configure(tagName='INFO', font=('Georgia', 11))
            all_sites.tag_configure(tagName='Site', font=('Microsoft Uighur', 20, 'underline'))
            all_sites.tag_configure(tagName='Location', font=('Microsoft Uighur', 18))
            all_sites.tag_configure(tagName='Time', font=('Microsoft Uighur', 18))
            all_sites.tag_configure(tagName='Info', font=('Microsoft Uighur', 18))
            all_sites.configure(state=DISABLED)

        canvas_heading()

    def display_menu_hover(e):

# Hovering over WIDGET 4 and showing text

        global x
        x = Label(bg_canvas, bg='snow', fg='gray10', bd=5, text='DISPLAY WORLD HERITAGE SITES', font=('Leelawadee', 9))
        bg_canvas.create_window(100, 387, window=x, anchor=NW)

    def display_menu_leave(e):
        global x
        x.destroy()

# Making of WIDGET 4 icon containing dimension,colour,background image,functionality of the widget
# WIDGET 4 has option of SEARCH BY NAME and SEARCH BY LOCATION

    display_menu_image = ImageTk.PhotoImage(
        file="App Requirements/UNESCO Menu Options  transparent 3.png")
    display_menu = Menubutton(bg_canvas, image=display_menu_image, bd=0, bg='#FFF1EF', activebackground='#E4D8D6',
                              highlightthickness=0, direction=RIGHT, width=81, height=87)
    display_menu_id = bg_canvas.create_window(0, 377, window=display_menu, anchor=NW, tags='display')
    display_menu.bind('<Enter>', display_menu_hover)
    display_menu.bind('<Leave>', display_menu_leave)
    display = Menu(display_menu, tearoff=0, font=('Garamond', 15, 'bold'), activebackground='#edbbe6',
                   activeforeground='#3b373a', fg='#2e2b28')
    display_menu.configure(menu=display)
    display.add_command(label='Top 10', command=lambda: display_page('Top 10'))
    display.add_command(label='All Sites', command=lambda: display_page('All Sites'))

    def search_page(option):
        global image_bg, bg_canvas, text_frame, text_scrollbar, search_results
        active('search_menu') # Activation of search menu

# When searching World heritage sites by the name of the sites
# By Name search option GUI design

        if option in 'By Name By Location':
            clear()
            image_bg = ImageTk.PhotoImage(file="App Requirements/homepage_UNESCO_canva.png")
            bg_canvas.create_image(0, 0, image=image_bg, anchor=NW, tags='bg_canvas')
        if option == 'By Name':
            search_name_tab = Label(text='SEARCH: BY NAME', font=('Verdana', 20), bg='#FF8A1D',
                                    fg='#FFFFFF')
            search_name_tab_id = bg_canvas.create_window(490, 170, window=search_name_tab, anchor=NE)
            site_name_label = bg_canvas.create_text(300, 235, text='Enter the name of site:', font=('Georgia', 16),
                                                    fill='black', anchor=NE)
            site_name_entry = Entry(bg_canvas, width=35, fg='#3b3b3b', bg='snow', font=('Microsoft Uighur', 20), bd=0,
                                    justify='center')
            bg_canvas.create_window(305, 230, window=site_name_entry, anchor=NW)
            text_frame = Frame(bg_canvas)
            text_scrollbar = Scrollbar(text_frame, orient=VERTICAL)
            text_scrollbar.pack(side=RIGHT, fill=Y)
            search_results = Text(text_frame, width=60, height=15, wrap=WORD, bd=0, bg='#FBFBFF',
                                  selectbackground='#BD89B6', spacing1=3, state=DISABLED,
                                  yscrollcommand=text_scrollbar.set)
            search_results.pack()
            text_scrollbar.configure(command=search_results.yview)
            bg_canvas.create_window(130, 330, window=text_frame, anchor=NW, tags='text_frame')

# Process of searching sites when checked by name

            def search_site():
                global text_frame, text_scrollbar, search_results
                site = site_name_entry.get()
                check = False
                for j in data.keys():
                    if site.lower() in j.lower() and site != '':
                        check = True
                        search_results.configure(state=NORMAL)
                        search_results.delete('1.0', 'end')
                        search_results.configure(state=DISABLED)
                if check:
                    bg_canvas.delete('message')
                    bg_canvas.create_text(250, 275, text='Entered site is present in database\n' # When entered site is already present in the database  
                                                         'Site information is displayed below', fill='green',
                                          font=('Helvetica', 13), justify='center', anchor=N, tags='message')
                    display_data = list(data.keys())
                    search_results.configure(state=NORMAL)
                    site_index = 1.0
                    for i in display_data:

# Displaying process using indexing
# GUI design process

                        if (site_name_entry.get()).lower() in i.lower():
                            s = ('SITE: ' + i + '\n' + 'LOCATED AT: ' + data[i]['State'] + '\n' + 'PERIOD: ' + data[i][
                                'Time'] + '\n' +
                                 'ABOUT THE SITE: ' + data[i]['Info'] + '\n' + '-' * 60 + '\n')
                            search_results.insert(END, s)
                            search_results.tag_add('SITE', site_index, site_index + 0.5)
                            search_results.tag_add('Site', site_index + 0.6, site_index + 1)
                            light_start = (s[4:].lower()).index((site_name_entry.get()).lower()) + 4
                            light_end = light_start + len(site_name_entry.get())
                            light_start = str(int(site_index)) + '.' + str(light_start)
                            light_end = str(int(site_index)) + '.' + str(light_end)
                            search_results.tag_add('Highlight', light_start, light_end)
                            site_index += 1
                            search_results.tag_add('LOCATION', site_index, site_index + 0.11)
                            search_results.tag_add('Location', site_index + 0.11, site_index + 1)
                            site_index += 1
                            search_results.tag_add('TIME', site_index, site_index + 0.7)
                            search_results.tag_add('Time', site_index + 0.7, site_index + 1)
                            site_index += 1
                            search_results.tag_add('INFO', site_index, site_index + 0.15)
                            search_results.tag_add('Info', site_index + 0.15, site_index + 1)
                            site_index += 2
                    search_results.tag_configure(tagName='SITE', font=('Georgia', 14))
                    search_results.tag_configure(tagName='LOCATION', font=('Georgia', 11))
                    search_results.tag_configure(tagName='TIME', font=('Georgia', 11))
                    search_results.tag_configure(tagName='INFO', font=('Georgia', 11))
                    search_results.tag_configure(tagName='Site', font=('Microsoft Uighur', 20, 'underline'))
                    search_results.tag_configure(tagName='Location', font=('Microsoft Uighur', 18))
                    search_results.tag_configure(tagName='Time', font=('Microsoft Uighur', 18))
                    search_results.tag_configure(tagName='Info', font=('Microsoft Uighur', 18))
                    search_results.tag_configure(tagName='Highlight', background='#BD89B6', foreground='white')
                    search_results.configure(state=DISABLED)
                else:
                    bg_canvas.delete('message')
                    bg_canvas.create_text(250, 275, text='Entered site is not present in database\n' # When site not present in the database
                                                         'Please re-enter the correct name of site', fill='red',
                                          font=('Helvetica', 13), justify='center', anchor=N, tags='message')
                    search_results.configure(state=NORMAL)
                    search_results.delete(1.0, END)
                    search_results.configure(state=DISABLED)

            site_name_check_button = Button(bg_canvas, text='SEARCH', bd=0, highlightthickness=0, bg='#0f5087',
                                            activebackground='#1c72ba', activeforeground='#ebf6ff', fg='#ebf6ff',
                                            font=('Microsoft Uighur', 18, 'bold'), height=0, width=20,
                                            command=search_site)
            bg_canvas.create_window(622, 275, window=site_name_check_button, anchor=NE)

# When searching World heritage sites by the location name where it is situated
# By Location search option GUI design

        if option == 'By Location':
            search_state_tab = Label(text='SEARCH: BY LOCATION', font=('Verdana', 20), bg='#FF8A1D',
                                     fg='#FFFFFF')
            search_state_tab_id = bg_canvas.create_window(500, 170, window=search_state_tab, anchor=NE)
            site_state_label = bg_canvas.create_text(300, 235, text='Enter the site location:', font=('Georgia', 16),
                                                     fill='black', anchor=NE)
            site_state_entry = Entry(bg_canvas, width=35, fg='#3b3b3b', bg='snow', font=('Microsoft Uighur', 20), bd=0,
                                     justify='center')
            bg_canvas.create_window(305, 230, window=site_state_entry, anchor=NW)
            text_frame = Frame(bg_canvas)
            text_scrollbar = Scrollbar(text_frame, orient=VERTICAL)
            text_scrollbar.pack(side=RIGHT, fill=Y)
            search_results = Text(text_frame, width=60, height=15, wrap=WORD, bd=0, bg='#FBFBFF',
                                  selectbackground='#BD89B6', spacing1=3, state=DISABLED,
                                  yscrollcommand=text_scrollbar.set)
            search_results.pack()
            text_scrollbar.configure(command=search_results.yview)
            bg_canvas.create_window(130, 330, window=text_frame, anchor=NW, tags='text_frame')

# Process of searching sites when checked by location

            def search_state():
                global text_frame, text_scrollbar, search_results
                site = site_state_entry.get()
                check = False
                for j in data.keys():
                    if site.lower() in (data[j]['State']).lower() and site != '':
                        check = True
                        search_results.configure(state=NORMAL)
                        search_results.delete('1.0', 'end')
                        search_results.configure(state=DISABLED)
                if check:
                    bg_canvas.delete('message')
                    bg_canvas.create_text(250, 275, text='Entered location has the following sites\n' # When sites are present the entered location
                                                         'Site information is displayed below', fill='green',
                                          font=('Helvetica', 13), justify='center', anchor=N, tags='message')
                    display_data = list(data.keys())
                    search_results.configure(state=NORMAL)
                    site_index = 1.0
                    for i in display_data:

# Displaying process using indexing
# GUI design process

                        if (site_state_entry.get()).lower() in (data[i]['State']).lower():
                            s = ('SITE: ' + i + '\n' + 'LOCATED AT: ' + data[i]['State'] + '\n' + 'PERIOD: ' + data[i][
                                'Time'] + '\n' +
                                 'ABOUT THE SITE: ' + data[i]['Info'] + '\n' + '-' * 60 + '\n')
                            search_results.insert(END, s)
                            search_results.tag_add('SITE', site_index, site_index + 0.5)
                            search_results.tag_add('Site', site_index + 0.6, site_index + 1)
                            site_index += 1
                            search_results.tag_add('LOCATION', site_index, site_index + 0.11)
                            search_results.tag_add('Location', site_index + 0.11, site_index + 1)
                            located_at = s.index('LOCATED AT: ') + len('LOCATED AT: ')
                            light_start = (((s[located_at:]).lower()).index((site_state_entry.get()).lower())
                                           + located_at - len('SITE: ' + i) - 1)
                            light_end = light_start + len(site_state_entry.get())
                            light_start = str(int(site_index)) + '.' + str(light_start)
                            light_end = str(int(site_index)) + '.' + str(light_end)
                            search_results.tag_add('Highlight', light_start, light_end)
                            site_index += 1
                            search_results.tag_add('TIME', site_index, site_index + 0.7)
                            search_results.tag_add('Time', site_index + 0.7, site_index + 1)
                            site_index += 1
                            search_results.tag_add('INFO', site_index, site_index + 0.15)
                            search_results.tag_add('Info', site_index + 0.15, site_index + 1)
                            site_index += 2
                    search_results.tag_configure(tagName='SITE', font=('Georgia', 14))
                    search_results.tag_configure(tagName='LOCATION', font=('Georgia', 11))
                    search_results.tag_configure(tagName='TIME', font=('Georgia', 11))
                    search_results.tag_configure(tagName='INFO', font=('Georgia', 11))
                    search_results.tag_configure(tagName='Site', font=('Microsoft Uighur', 20, 'underline'))
                    search_results.tag_configure(tagName='Location', font=('Microsoft Uighur', 18))
                    search_results.tag_configure(tagName='Time', font=('Microsoft Uighur', 18))
                    search_results.tag_configure(tagName='Info', font=('Microsoft Uighur', 18))
                    search_results.tag_configure(tagName='Highlight', background='#BD89B6', foreground='white')
                    search_results.configure(state=DISABLED)
                else:
                    bg_canvas.delete('message')
                    bg_canvas.create_text(250, 275, text='Entered location has no sites to show\n' # When site is not present in the entered location
                                                         'Please re-enter the correct name of site', fill='red',
                                          font=('Helvetica', 13), justify='center', anchor=N, tags='message')
                    search_results.configure(state=NORMAL)
                    search_results.delete(1.0, END)
                    search_results.configure(state=DISABLED)

            site_name_check_button = Button(bg_canvas, text='SEARCH', bd=0, highlightthickness=0, bg='#0f5087',
                                            activebackground='#1c72ba', activeforeground='#ebf6ff', fg='#ebf6ff',
                                            font=('Microsoft Uighur', 18, 'bold'), height=0, width=20,
                                            command=search_state)
            bg_canvas.create_window(622, 275, window=site_name_check_button, anchor=NE)
        canvas_heading()

    def search_menu_hover(e):

# Hovering over WIDGET 5 and showing text

        global x
        x = Label(bg_canvas, bg='snow', fg='gray10', bd=5, text='SEARCH AMONG AVAILABLE HERITAGE SITES',
                  font=('Leelawadee',
                        9))
        bg_canvas.create_window(100, 478, window=x, anchor=NW)

    def search_menu_leave(e):
        global x
        x.destroy()

# Making of WIDGET 5 icon containing dimension,colour,background image,functionality of the widget
# WIDGET 5 has option of STATES AND UNION TERRITORIES

    search_menu_image = ImageTk.PhotoImage(
        file="App Requirements/UNESCO Menu Options  transparent 4.png")
    search_menu = Menubutton(bg_canvas, image=search_menu_image, bd=0, bg='#FFF1EF', activebackground='#E4D8D6',
                             highlightthickness=0, direction=RIGHT, width=81, height=87)
    search_menu_id = bg_canvas.create_window(0, 468, window=search_menu, anchor=NW, tags='search')
    search_menu.bind('<Enter>', search_menu_hover)
    search_menu.bind('<Leave>', search_menu_leave)
    search = Menu(search_menu, tearoff=0, font=('Garamond', 15, 'bold'), activebackground='#edbbe6',
                  activeforeground='#3b373a', fg='#2e2b28')
    search_menu.configure(menu=search)
    search.add_command(label='By Name', command=lambda: search_page('By Name'))
    search.add_command(label='By Location', command=lambda: search_page('By Location'))

    def state_page(option):
        global image_bg, bg_canvas, b_menu
        active('state_menu') # Activation of state menu
        if option in 'States and Union Territories':
            clear()
            image_bg = ImageTk.PhotoImage(file="App Requirements/homepage_UNESCO_canva.png")
            bg_canvas.create_image(0, 0, image=image_bg, anchor=NW, tags='bg_canvas')
            states_tab = Label(text='STATES AND UNION TERRITORIES', font=('Verdana', 20), bg='#FF8A1D',
                               fg='#FFFFFF')
            states_tab_id = bg_canvas.create_window(375, 170, window=states_tab, anchor=N)
            states_tab_instruction = bg_canvas.create_text(375, 225, anchor=N, justify=CENTER,
                                                           text='Click on the option with the first letter of\n' # Instructionfor what to do in the page
                                                                'the site you want to surf through to continue',
                                                           font=('Georgia', 18, 'italic'), fill='black')
        if option == 'States and Union Territories':

# Positioning of each letter in a box using x and y axis

            x_coord, y_coord = 145, 310
            j = k = 0

# States arrangement in alphabetical order in their respective letter boxes

            alphabet_buttons_command = [['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Andaman and Nicobar Islands'],
                                        ['Bihar'], ['Chhattisgarh', 'Chandigarh'],
                                        ['Dadra and Nagar Haveli', 'Daman and Diu',  'Delhi'],
                                        ['Goa', 'Gujarat'], ['Haryana', 'Himachal Pradesh'], ['Karnataka', 'Kerala'],
                                        ['Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram'],
                                        ['Nagaland'], ['Odisha'], ['Punjab', 'Puducherry'], ['Rajasthan'], ['Sikkim'],
                                        ['Tamil Nadu', 'Telangana', 'Tripura'], ['Uttar Pradesh', 'Uttarakhand'],
                                        ['West Bengal']]

# Fetching and checking of data from database

            def fetch_state_sites(state):
                global text_frame, text_scrollbar, search_results

                for k in 'abcdghjklmnoprstuw'.upper():
                    bg_canvas.delete(k)

                text_frame = Frame(bg_canvas)
                text_scrollbar = Scrollbar(text_frame, orient=VERTICAL)
                text_scrollbar.pack(side=RIGHT, fill=Y)
                search_results = Text(text_frame, width=60, height=20, wrap=WORD, bd=0, bg='#FBFBFF',
                                      selectbackground='#BD89B6', spacing1=3, state=DISABLED,
                                      yscrollcommand=text_scrollbar.set)
                search_results.pack()
                text_scrollbar.configure(command=search_results.yview)
                bg_canvas.create_window(130, 220, window=text_frame, anchor=NW, tags='text_frame')
                display_data = list(data.keys())
                search_results.configure(state=NORMAL)
                check = False
                for j in range(len(alphabet_buttons_command)):
                    for m in range(len(alphabet_buttons_command[j])):
                        if state in alphabet_buttons_command[j][m] and state != '':
                            check = True
                            search_results.configure(state=NORMAL)
                            search_results.delete('1.0', 'end')
                            search_results.configure(state=DISABLED)
                if check:

# Checking and displaying state usinf index

                    site_index = 1.0
                    search_results.configure(state=NORMAL)
                    for i in display_data:
                        if state in data[i]['State']:
                            s = ('SITE: ' + i + '\n' + 'LOCATED AT: ' + data[i]['State'] + '\n' + 'PERIOD: ' + data[i][
                                'Time'] + '\n' +
                                 'ABOUT THE SITE: ' + data[i]['Info'] + '\n' + '-' * 60 + '\n')
                            search_results.insert(END, s)
                            search_results.tag_add('SITE', site_index, site_index + 0.5)
                            search_results.tag_add('Site', site_index + 0.6, site_index + 1)
                            site_index += 1
                            search_results.tag_add('LOCATION', site_index, site_index + 0.11)
                            search_results.tag_add('Location', site_index + 0.11, site_index + 1)
                            located_at = s.index('LOCATED AT: ') + len('LOCATED AT: ')
                            light_start = (((s[located_at:]).lower()).index(state.lower())
                                           + located_at - len('SITE: ' + i) - 1)
                            light_end = light_start + len(state)
                            light_start = str(int(site_index)) + '.' + str(light_start)
                            light_end = str(int(site_index)) + '.' + str(light_end)
                            search_results.tag_add('Highlight', light_start, light_end)
                            site_index += 1
                            search_results.tag_add('TIME', site_index, site_index + 0.7)
                            search_results.tag_add('Time', site_index + 0.7, site_index + 1)
                            site_index += 1
                            search_results.tag_add('INFO', site_index, site_index + 0.15)
                            search_results.tag_add('Info', site_index + 0.15, site_index + 1)
                            site_index += 2
                    search_results.tag_configure(tagName='SITE', font=('Georgia', 14))
                    search_results.tag_configure(tagName='LOCATION', font=('Georgia', 11))
                    search_results.tag_configure(tagName='TIME', font=('Georgia', 11))
                    search_results.tag_configure(tagName='INFO', font=('Georgia', 11))
                    search_results.tag_configure(tagName='Site', font=('Microsoft Uighur', 20, 'underline'))
                    search_results.tag_configure(tagName='Location', font=('Microsoft Uighur', 18))
                    search_results.tag_configure(tagName='Time', font=('Microsoft Uighur', 18))
                    search_results.tag_configure(tagName='Info', font=('Microsoft Uighur', 18))
                    if len(search_results.get(1.0, END)) == 1:
                        search_results.insert(END, 'The selected location does not have any World Heritage sites.' # When no site is present in the selected state 
                                                   '\nPlease check for another location-')
                        search_results.tag_add('Not present', site_index, END)
                        search_results.tag_configure(tagName='Not present', font=('Microsoft Uighur', 18))
                    search_results.configure(state=DISABLED)

            def add_command(state):

# Commands for each and every button having the first letter of the states

                global b_menu
                if state == alphabet_buttons_command[0][0]:
                    b_menu.add_command(label=alphabet_buttons_command[0][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[0][0]))
                if state == alphabet_buttons_command[0][1]:
                    b_menu.add_command(label=alphabet_buttons_command[0][1],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[0][1]))
                if state == alphabet_buttons_command[0][2]:
                    b_menu.add_command(label=alphabet_buttons_command[0][2],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[0][2]))
                if state == alphabet_buttons_command[0][3]:
                    b_menu.add_command(label=alphabet_buttons_command[0][3],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[0][3]))
                if state == alphabet_buttons_command[1][0]:
                    b_menu.add_command(label=alphabet_buttons_command[1][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[1][0]))
                if state == alphabet_buttons_command[2][0]:
                    b_menu.add_command(label=alphabet_buttons_command[2][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[2][0]))
                if state == alphabet_buttons_command[2][1]:
                    b_menu.add_command(label=alphabet_buttons_command[2][1],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[2][1]))
                if state == alphabet_buttons_command[3][0]:
                    b_menu.add_command(label=alphabet_buttons_command[3][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[3][0]))
                if state == alphabet_buttons_command[3][1]:
                    b_menu.add_command(label=alphabet_buttons_command[3][1],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[3][1]))
                if state == alphabet_buttons_command[3][2]:
                    b_menu.add_command(label=alphabet_buttons_command[3][2],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[3][2]))
                if state == alphabet_buttons_command[4][0]:
                    b_menu.add_command(label=alphabet_buttons_command[4][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[4][0]))
                if state == alphabet_buttons_command[4][1]:
                    b_menu.add_command(label=alphabet_buttons_command[4][1],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[4][1]))
                if state == alphabet_buttons_command[5][0]:
                    b_menu.add_command(label=alphabet_buttons_command[5][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[5][0]))
                if state == alphabet_buttons_command[5][1]:
                    b_menu.add_command(label=alphabet_buttons_command[5][1],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[5][1]))
                if state == alphabet_buttons_command[6][0]:
                    b_menu.add_command(label=alphabet_buttons_command[6][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[6][0]))
                if state == alphabet_buttons_command[6][1]:
                    b_menu.add_command(label=alphabet_buttons_command[6][1],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[6][1]))
                if state == alphabet_buttons_command[7][0]:
                    b_menu.add_command(label=alphabet_buttons_command[7][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[7][0]))
                if state == alphabet_buttons_command[7][1]:
                    b_menu.add_command(label=alphabet_buttons_command[7][1],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[7][1]))
                if state == alphabet_buttons_command[7][2]:
                    b_menu.add_command(label=alphabet_buttons_command[7][2],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[7][2]))
                if state == alphabet_buttons_command[7][3]:
                    b_menu.add_command(label=alphabet_buttons_command[7][3],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[7][3]))
                if state == alphabet_buttons_command[7][4]:
                    b_menu.add_command(label=alphabet_buttons_command[7][4],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[7][4]))
                if state == alphabet_buttons_command[8][0]:
                    b_menu.add_command(label=alphabet_buttons_command[8][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[8][0]))
                if state == alphabet_buttons_command[9][0]:
                    b_menu.add_command(label=alphabet_buttons_command[9][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[9][0]))
                if state == alphabet_buttons_command[10][0]:
                    b_menu.add_command(label=alphabet_buttons_command[10][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[10][0]))
                if state == alphabet_buttons_command[10][1]:
                    b_menu.add_command(label=alphabet_buttons_command[10][1],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[10][1]))
                if state == alphabet_buttons_command[11][0]:
                    b_menu.add_command(label=alphabet_buttons_command[11][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[11][0]))
                if state == alphabet_buttons_command[12][0]:
                    b_menu.add_command(label=alphabet_buttons_command[12][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[12][0]))
                if state == alphabet_buttons_command[13][0]:
                    b_menu.add_command(label=alphabet_buttons_command[13][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[13][0]))
                if state == alphabet_buttons_command[13][1]:
                    b_menu.add_command(label=alphabet_buttons_command[13][1],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[13][1]))
                if state == alphabet_buttons_command[13][2]:
                    b_menu.add_command(label=alphabet_buttons_command[13][2],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[13][2]))
                if state == alphabet_buttons_command[14][0]:
                    b_menu.add_command(label=alphabet_buttons_command[14][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[14][0]))
                if state == alphabet_buttons_command[14][1]:
                    b_menu.add_command(label=alphabet_buttons_command[14][1],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[14][1]))
                if state == alphabet_buttons_command[15][0]:
                    b_menu.add_command(label=alphabet_buttons_command[15][0],
                                       command=lambda: fetch_state_sites(alphabet_buttons_command[15][0]))

# Showing the buttons on the screen using GUI

            for i in 'abcdghkmnoprstuw'.upper():
                if j == 4:
                    j = 0
                    x_coord = 145
                    y_coord += 77
                b = Menubutton(bg_canvas, text=i, width=10, bd=0, highlightthickness=0,
                               font=('Microsoft Uighur', 20, 'bold'),
                               bg='#2d2e33', activebackground='#53545c', fg='#d8dbf2', activeforeground='#d8dbf2',
                               height=0)
                b_id = bg_canvas.create_window(x_coord, y_coord, window=b, anchor=NW, tags=i)
                b_menu = Menu(b, tearoff=False, font=('Garamond', 15, 'bold'), activebackground='#edbbe6',
                              activeforeground='#3b373a', fg='#2e2b28')
                b.configure(menu=b_menu)
                for l in alphabet_buttons_command[k]:
                    add_command(l)
                x_coord += 120
                j += 1
                k += 1
        canvas_heading()

    def state_menu_hover(e):

# Hovering over WIDGET 5 and showing text

        global x
        x = Label(bg_canvas, bg='snow', fg='gray10', bd=5, text='STATE-WISE HERITAGE SITES', font=('Leelawadee', 9))
        bg_canvas.create_window(100, 567, window=x, anchor=NW)

    def state_menu_leave(e):
        global x
        x.destroy()

# Making of WIDGET 5 icon containing dimension,colour,background image,functionality of the widget
# WIDGET 5 has option of STATES AND UNION TERRITORIES

    state_menu_image = ImageTk.PhotoImage(
        file="App Requirements/UNESCO Menu Options  transparent 5.png")
    state_menu = Menubutton(bg_canvas, image=state_menu_image, bd=0, bg='#FFF1EF', activebackground='#E4D8D6',
                            highlightthickness=0, direction=RIGHT, width=81, height=87)
    state_menu_id = bg_canvas.create_window(0, 559, window=state_menu, anchor=NW, tags='state')
    state_menu.bind('<Enter>', state_menu_hover)
    state_menu.bind('<Leave>', state_menu_leave)
    state = Menu(state_menu, tearoff=0, font=('Garamond', 15, 'bold'), activebackground='#edbbe6',
                 activeforeground='#3b373a', fg='#2e2b28')
    state_menu.configure(menu=state)
    state.add_command(label='States and Union Territories', command=lambda: state_page('States and Union Territories'))

    active('home_menu')

    home_page()

    main_home.mainloop()

# END OF THE SECOND PAGE HAVING ALL THE DATA
# START OF THE GUI LOGIN
#  GUI Login
#  Main Window framework

def GUI_login():
    global main, image_bg, bg_canvas
    main = Tk()
    main.title('UNESCO PROJECT APPLICATION')

# Dimension of the page

    main_width = 650
    main_height = 650
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    main.geometry(f'{main_width}x{main_height}+{(int((screen_width - main_width) / 2))}+'
                  f'{(int((screen_height - main_height) // 2) - 40)}')
    main.maxsize(main_width, main_height)
    main.minsize(main_width, main_height)

# Background image and icon framework
# Icon of the software

    main.iconbitmap("App Requirements/UNESCO App Icon.ico")
    image_bg = ImageTk.PhotoImage(file="App Requirements/UNESCO 650x650 (1).png")

    bg_canvas = Canvas(main, bg='white', bd=0, highlightthickness=0)
    bg_canvas.pack(side=RIGHT, anchor=CENTER, fill=BOTH, expand=TRUE)
    bg_canvas.create_image(0, 0, image=image_bg, anchor=NW)

#  Login ID And PASSWORD framework using GUI
# Creation of show and hide button

def login():
    GUI_login()
    global show_value, b_text_1, disp, font, entry_id, entry_pwd, login_data, user_id
    label_title1 = bg_canvas.create_text(385, 65, text='UNESCO', font=('Constantia', 50), fill='#E9E8E8')
    label_title2 = bg_canvas.create_text(385, 120, text='Software Application', font=('Billion Dreams', 45),
                                         fill='#E9E8E8')
    label_id = bg_canvas.create_text(200, 320, text='Enter your login ID:', font=('Georgia', 16), # Text box for entering login id
                                     fill='black', anchor=E)
    label_pwd = bg_canvas.create_text(200, 400, text='Enter the Password:', font=('Georgia', 16), # Text box for entering login id
                                      fill='black', anchor=E)
    entry_id = Entry(bg_canvas, width=40, fg='#3b3b3b', bg='#adddf7', font=('Microsoft Uighur', 20), bd=0)
    entry_id_n = bg_canvas.create_window(205, 320, window=entry_id, anchor=W)
    show_value = '*'
    font = ('Microsoft Uighur', 20, 'bold')
    entry_pwd = Entry(bg_canvas, width=36, fg='#3b3b3b', bg='#adddf7', font=font, show=show_value, bd=0)
    entry_pwd_n = bg_canvas.create_window(205, 400, window=entry_pwd, anchor=W)
    b_text_1 = 'SHOW'
    login_data = {"kushal.sir": 1, "akashdeep.04": 4, "samrajnee.29": 29, "shounak.30": 30,
                  "suhina.39": 39, "swastika.40": 40} # USER ID PASSWORD for each member including Kushal sir,s

    #  Show or hide the password framework

    def see():
        global show_value, b_text_1, font
        if show_value == '*':
            show_value = ''
            font = ('Microsoft Uighur', 20)
            entry_pwd.configure(width=40, show=show_value, font=font)
            b_text_1 = 'HIDE'
            show.configure(text=b_text_1)
        elif show_value == '':
            show_value = '*' # Used for hiding the password
            font = ('Microsoft Uighur', 20, 'bold')
            entry_pwd.configure(width=36, show=show_value, font=font)
            b_text_1 = 'SHOW'
            show.configure(text=b_text_1)

    show = Button(bg_canvas, text=b_text_1, bg='#ff9326', bd=0, width=11, height=2, highlightthickness=0, command=see)
    show_n = bg_canvas.create_window(648, 399, window=show, anchor=E)

# Checking ID and PASSWORD validity process
# GUI Design for the validity checking

    def check(Id, pwd):
        global warning_id, warning_pwd, login_data, converted, type_converted, user_id
        warning_id = bg_canvas.create_text(205, 380, text='', font='Helvetica', fill='red', anchor=W, tags='warning')
        warning_pwd = bg_canvas.create_text(205, 440, text='', font='Helvetica', fill='red', anchor=W, tags='warning')

        user_input('unknown', Id)
        Id = converted
        user_input('unknown', pwd)
        pwd = converted

        if Id in login_data.keys():
            if login_data[Id] == pwd:
                bg_canvas.delete('warning')
                warning_id = bg_canvas.create_text(205, 350, text='Correct ID', font='Helvetica', fill='green',
                                                   anchor=W, tags='warning')
                warning_pwd = bg_canvas.create_text(205, 430, text='Correct Pwd', font='Helvetica', fill='green',
                                                    anchor=W, tags='warning')
                user_id = Id
                home()
            else:
                bg_canvas.delete('warning')
                warning_pwd = bg_canvas.create_text(205, 430, text='**Invalid PASSWORD for entered ID',
                                                    font='Helvetica', fill='red', anchor=W, tags='warning')
        else:
            bg_canvas.delete('warning')
            warning_id = bg_canvas.create_text(205, 350, text='**Invalid ID', font='Helvetica', fill='red', anchor=W,
                                               tags='warning')

    logged_in_b = Button(bg_canvas, text='ENTER', font=18, bd=0, bg='#114774', fg='#e3effa', width=39, height=2,
                         command=lambda: check(entry_id.get(), entry_pwd.get()))
    logged_in_b_n = bg_canvas.create_window(208, 485, window=logged_in_b, anchor=W)

# Member button to show of members of the group

    def members(Id):
        global entry_id, entry_pwd, login_data
        entry_id.delete(0, END)
        entry_id.insert(0, Id)
        entry_pwd.delete(0, END)
        entry_pwd.insert(0, login_data[Id])
        check(entry_id.get(), entry_pwd.get())

    my_menu = Menubutton(bg_canvas, width=20, height=2, bd=0, highlightthickness=0, bg='#783e70', fg='#fff5fa',
                         text='Members', font=('Arial', 15, 'bold'), activebackground='#3d1c39',
                         activeforeground='#e8dfe3', direction='above')
    bg_canvas.create_window(640, 640, window=my_menu, anchor=SE)
    members_m = Menu(my_menu, title='Click to use info', tearoff=0, font=('Garamond', 15, 'bold'),
                     activebackground='#ff9c2b', activeforeground='black', fg='#2e2b28')

# Name of the members including Kushal Sir's name will be displayed when the memver buttpn os clicked

    my_menu.configure(menu=members_m)
    members_m.add_command(label='Kushal Sir', command=lambda: members("kushal.sir"))
    members_m.add_command(label='Akashdeep', command=lambda: members("akashdeep.04"))
    members_m.add_command(label='Samrajnee', command=lambda: members("samrajnee.29"))
    members_m.add_command(label='Shounak', command=lambda: members("shounak.30"))
    members_m.add_command(label='Suhina', command=lambda: members("suhina.39"))
    members_m.add_command(label='Swastika', command=lambda: members("swastika.40"))


login()
main.mainloop()
# End of framework of Login Page
