from tkinter import *
from tkinter import ttk, LEFT, TOP, BOTH, CENTER
from constant import *

#=> ????  import a file
#=> access level : public private protected
class Country:
    id = -1
    name = ''
    image_path = ''

    def __init__(self, id, name, image):
        self.id = id
        self.name = name
        self.image_path = image

class User:
    id = ''
    name = ''
    gender = False
    country_id = -1

    def __init__(self, id, name, gender, country_id):
        self.id = id
        self.name = name
        self.gender = gender
        self.country_id = country_id
    
    def get_user(self, country_name):
        return (self.id, self.name, STR_MALE if self.gender else STR_FEMALE, country_name)


root = Tk()
root.title('Users Manager')
root.minsize(ROOT_WIDTH, ROOT_HEIGHT)
root.maxsize(ROOT_WIDTH, ROOT_HEIGHT)

#Frame:
frame_control_title = Frame(root)
frame_control_id = Frame(root)
frame_control_name = Frame(root)
frame_control_gender = Frame(root)
frame_control_national = Frame(root)
frame_control_button = Frame(root)
frame_list = Frame(root)

frame_control_title.pack(expand = False, fill=X)
frame_control_id.pack(expand = False, fill=X)
frame_control_name.pack(expand = False, fill=X)
frame_control_gender.pack(expand = False, fill=X)
frame_control_national.pack(expand = False, fill=X)
frame_control_button.pack(expand=False, fill=X)

frame_list.pack(expand = False, fill=X)

#Variables:
image_flag = PhotoImage(file='images/a.png')
lst_user = [User('PD347', 'Adam Parker', 1, 1),
    User('PD784', 'Charlotte Mckinney', 1, 2),
    User('PD342', 'Vanessa Williams', 0, 1),
    User('PD987', 'Oliver Kahn', 0, 3),
    User('PD674', 'Harper Cikarang', 0, 2)]

lst_country = [Country(1, 'America', 'a.png'),
              Country(2, 'Canada', 'b.png'),
             Country(3, 'Australia', 'c.png')]

def change_flag(name_file):
    image_flag = PhotoImage(file= 'images/' + name_file)
    img_national.configure(image=image_flag)
    img_national.image = image_flag


#Methods: => variable region image_flag ???
def on_cmb_national_selected(event):
    index_selected = cmb_national.current()
    change_flag(lst_country[index_selected].image_path)

def on_btn_reset_click():
    entry_id.delete(0, END)
    entry_name.delete(0, END)
    rd_female.select()
    cmb_national.current(0)
    img_national.configure(image=image_flag)
    img_national.image = image_flag

#?? LINQ select
def get_name_country_by_id(id):
    for item in lst_country:
        if(item.id == id):
            return item.name
    return 'N/A'

def get_id_country_by_name(name):
    for item in lst_country:
        if(item.name == name):
            return item.id
    return -1

def get_index_country_by_id(id):
    index = 0
    while(index < len(lst_country)):
        if(lst_country[index].id == id):
            return index
        index = index + 1
    return -1

def validate_id_name():
    if(entry_id.get() == '' or entry_name.get() == ''):
        return False
    return True

def on_btn_add_click():
    if(not validate_id_name()):
        return
    txt_id = entry_id.get()
    txt_name = entry_name.get()
    bl_gender = rd_gender.get()
    lst_user.append(User(txt_id, txt_name,bl_gender, lst_country[cmb_national.current()].id))
    show_data_on_tree()

def show_data_on_tree():
    for item in treeview.get_children():
        treeview.delete(item)
    index = 0
    while index < len(lst_user):
        treeview.insert("", index, values=lst_user[index].get_user(get_name_country_by_id(lst_user[index].country_id)))
        index += 1

def tree_selected_item(event):
    index_row_selected = treeview.index(treeview.focus())
    entry_id.delete(0, END)
    entry_name.delete(0, END)
    user = lst_user[index_row_selected]
    entry_id.insert(0,user.id)
    entry_name.insert(0, user.name)
    rd_gender.set(user.gender)
    cmb_national.current(get_index_country_by_id(user.country_id))
    change_flag(lst_country[get_index_country_by_id(user.country_id)].image_path)

def on_btn_remove_click():
    if (not validate_id_name()):
        return
    # index_row_selected => self????
    treeview_focus = treeview.focus()
    if (treeview_focus != ''):
        index_row_selected = treeview.index(treeview_focus)
        del lst_user[index_row_selected]
        show_data_on_tree()
        on_btn_reset_click()


def on_btn_update_click():
    if (not validate_id_name()):
        return
    treeview_focus = treeview.focus()
    if(treeview_focus != ''):
        index_row_selected = treeview.index(treeview_focus)
        txt_id = entry_id.get()
        txt_name = entry_name.get()
        bl_gender = rd_gender.get()
        lst_user[index_row_selected] = User(txt_id, txt_name, bl_gender, lst_country[cmb_national.current()].id)
        show_data_on_tree()

#Title:
Label(frame_control_title, text='Python is Fun!', width=LABEL_WIDTH, compound='center', fg='red', font=('Arial', 14, 'bold')).pack(fill=X)

#Entry ID:
Label(frame_control_id, text='ID:', width=LABEL_WIDTH, justify='left').pack(side=LEFT)
entry_id = Entry(frame_control_id)
entry_id.pack(fill=X,padx=5, pady=5)

#Entry Name:
Label(frame_control_name, text='Name:', width=LABEL_WIDTH, compound='left').pack(side=LEFT)
entry_name = Entry(frame_control_name)
entry_name.pack(fill=X,padx=5, pady=5)

#RadioButton Male
rd_gender = BooleanVar()
Label(frame_control_gender, text='Gender:', width=LABEL_WIDTH, compound='left').pack(side=LEFT)
rd_female = Radiobutton(frame_control_gender, text='Female', variable = rd_gender, value=False)
rd_female.pack(side=LEFT)
rd_male = Radiobutton(frame_control_gender, text='Male', variable = rd_gender, value=True)
rd_male.pack(side=LEFT)
#rd_female.select()

#Combobox National:
arr_cmb = []
for item in lst_country:
    arr_cmb.append(item.name)

Label(frame_control_national, text='National:', width=LABEL_WIDTH, compound='left').pack(side=LEFT)
cmb_national = ttk.Combobox(frame_control_national, values=arr_cmb, state='readonly')
cmb_national.pack(side=LEFT, padx=5, pady=5)
cmb_national.bind('<<ComboboxSelected>>', on_cmb_national_selected)
cmb_national.current(0)

#Label(PictrueBox) Flag
img_national = Label(frame_control_national, width='80', height='41', image = image_flag)
img_national.pack(side=LEFT)

#Buttons: => set button alway center in a frame
Button(frame_control_button, text='Add', command=on_btn_add_click).pack(side=LEFT, padx=10, pady =5)
Button(frame_control_button, text='Update', command=on_btn_update_click).pack(side=LEFT, padx=10, pady =5)
Button(frame_control_button, text='Remove', command = on_btn_remove_click).pack(side=LEFT, padx=10, pady =5)
Button(frame_control_button, text='Reset', command=on_btn_reset_click).pack(side=LEFT, padx=10, pady =5)

#TreeView => loop for i?


treeview = ttk.Treeview(frame_list)
treeview.pack(fill=BOTH, padx=5, pady=5)
treeview['columns'] = ['col_id', 'col_name', 'col_gender', 'col_national']
treeview['show'] = 'headings'

# scrollbar = Scrollbar(treeview,orient=VERTICAL, command=treeview.yview)
# scrollbar.pack(side=RIGHT)
# treeview.configure(yscrollcommand = scrollbar)

treeview.heading('col_id', text='ID')
treeview.column('col_id', width = '100')
treeview.heading('col_name', text='Name')
treeview.column('col_name', width = '100')
treeview.heading('col_gender', text='Gender',)
treeview.column('col_gender', width = '100')
treeview.heading('col_national', text='National')
treeview.column('col_national', width = '100')
treeview.bind('<<TreeviewSelect>>', tree_selected_item)
show_data_on_tree()


#Main Loop
root.mainloop()


