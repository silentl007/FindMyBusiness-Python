from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRoundFlatButton
from kivymd.toast import toast
from SLogic import structure
import requests
import sqlite3
import random

# for production purpose
# Window.fullscreen = 'auto'

# for testing purpose
Window.size = (300, 500)


class SelectLga(Screen):
    pass


class SelectCategory(Screen):
    pass


class AvailableBusiness(Screen):
    pass


class AddBusiness(Screen):
    pass


class AddLGA(Screen):
    pass


class AddCategory(Screen):
    pass


screenmanager = ScreenManager()
screenmanager.add_widget(SelectLga(name='select lga'))
screenmanager.add_widget(SelectCategory(name='select category'))
screenmanager.add_widget(AvailableBusiness(name='available business'))
screenmanager.add_widget(AddBusiness(name='add business'))
screenmanager.add_widget(AddLGA(name='add lga'))
screenmanager.add_widget(AddCategory(name='add category'))


class FindMyBusiness(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # initialize my screen list holder
        self.screen_list = ['holder']

        # collecting text property of select lga of find business section
        self.textcollectorlocation = ['holder']

        # collecting text property of select category find business section
        self.textcollectorcategory = ['holder']

        # collecting text property of add lga of add business section
        self.addlga = []

        # collecting text property of add category add business section
        self.addcategory = []

        # Binding back function to the escape key
        Window.bind(on_keyboard=self.back_func_key)

    # def on_start(self):
        # self.connect_mongo()
        # self.populate_bookmark()

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Red'
        screen = Builder.load_string(structure)
        return screen

    # ------------------------ connect, read/write database logic------------------------------------
    def connect_mongo(self):
        try:
            connect = requests.get('https://deployment-fmb.herokuapp.com/query')
            if connect.status_code == 200:
                toast("Connected to Database")
                if self.root.current == 'available business':
                    self.root.current = 'select category'
                return True
            else:
                print(connect.status_code)
                self.failed_connection_box()
                toast("Failed to Connect")
        except Exception as ex:
            print(ex)
            self.failed_connection_box()
            toast("Failed to Connect")


    def text_collector_category(self, instance):
        try:
            self.textcollectorcategory.append(instance.text)
            urlink = "https://deployment-fmb.herokuapp.com/data/" +self.textcollectorlocation[-1]+"/"+self.textcollectorcategory[-1]
            connect_db = requests.get(urlink)
            get_data = connect_db.json()
            random.shuffle(get_data)
            if get_data:
                for data in get_data:
                    list_item = ThreeLineListItem(text='Name: ' + str(data["Name"]),
                                                  secondary_text='Location: ' + str(data["Location"]),
                                                  tertiary_text='Number: ' + str(data["Number"]),
                                                  on_release=self.extra_feature)
                    self.root.ids.available.add_widget(list_item)
            else:
                self.pop_box()
        except:
            self.failed_connection_box()

    def submit(self):
        try:
            urlink = "https://deployment-fmb.herokuapp.com/review/"+self.addlga[-1]
            data = {"Category": self.addcategory[-1], "Name": self.root.ids.add_name.text, "Location": self.root.ids.add_location.text, "Number": self.root.ids.add_number.text}
            connect_db = requests.post(urlink, data=data)
            if connect_db.status_code == 200:
                self.root.ids.add_name.text = ''
                self.root.ids.add_location.text = ''
                self.root.ids.add_number.text = ''
                self.root.ids.lga_btn.text = 'Select LGA'
                self.root.ids.category_btn.text = 'Select Category'
                self.submit_pop_box()
            else:
                self.failed_connection_box()
        except Exception as ex:
            self.failed_connection_box()

        # ----------- SQLite Bookmark -----------------

    def bookmark(self, obj):
        self.extra_feature_dismiss(obj)
        connect = sqlite3.connect('bookmark.db')
        cursor = connect.cursor()
        cursor.executemany("INSERT INTO savedbookmarks VALUES (?,?,?)", self.book)
        connect.commit()
        connect.close()
        toast("Bookmark Added")
        self.populate_bookmark()

    def populate_bookmark(self):
        self.root.ids.bookmark.clear_widgets()
        connect = sqlite3.connect('bookmark.db')
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM savedbookmarks")
        data = cursor.fetchall()
        for filler in data:
            fill = ThreeLineListItem(text='Name: ' + str(filler[0]),
                                     secondary_text='Location: ' + str(filler[1]),
                                     tertiary_text='Number: ' + str(filler[2]),
                                     on_release=self.book_pop)
            self.root.ids.bookmark.add_widget(fill)

    def remove_book(self):
        location = [(self.remove_location)]
        connect = sqlite3.connect('bookmark.db')
        cursor = connect.cursor()
        cursor.execute(" DELETE from savedbookmarks WHERE Location = (?)", location)
        connect.commit()
        toast("Bookmark Removed")

    # ----------- text changers -------------------
    def text_collector_location(self, instance):
        self.textcollectorlocation.append(instance.text)
        self.root.ids.category_title.title = "Categories" + " " + "for" + " " + self.textcollectorlocation[-1]

    def change_text_lga_btn(self, instance):
        self.addlga.append(instance.text)
        self.root.ids.lga_btn.text = self.addlga[-1]

    def change_text_category_btn(self, instance):
        self.addcategory.append(instance.text)
        self.root.ids.category_btn.text = self.addcategory[-1]

    # ---------- pop up boxes -------------------------------------
    def book_pop(self, obj):
        self.remove_location = str(obj.secondary_text)[10::]
        close_button = MDRoundFlatButton(text="Ok", on_release=self.book_pop_dismiss)
        remove_button = MDRoundFlatButton(text="Remove", on_release=self.update_remove)
        self.bookpop = MDDialog(title='Location',
                                buttons=[remove_button, close_button],
                                text=self.remove_location,
                                size_hint=(0.7, 1))
        self.bookpop.open()

    def book_pop_dismiss(self, obj):
        self.bookpop.dismiss()

    def pop_box(self):
        close_button = MDRoundFlatButton(text='Ok', on_release=self.pop_box_dismiss)
        self.dialog_box = MDDialog(title='No Business Found!',
                                   text='Please Be Patient, Coming Soon!',
                                   buttons=[close_button],
                                   size_hint=(0.7, 1))
        self.dialog_box.open()

    def pop_box_dismiss(self, obj):
        self.dialog_box.dismiss()

    def failed_connection_box(self):
        retry_button = MDRoundFlatButton(text='Retry', on_release=self.retry_connect)
        close_button = MDRoundFlatButton(text='Quit', on_release=self.failed_connection_box_dismiss)
        self.failed = MDDialog(title='Network Error',
                               text='Please Enable Internet Connection!',
                               buttons=[retry_button, close_button],
                               size_hint=(0.7, 1))
        self.failed.open()

    def failed_connection_box_dismiss(self, obj):
        self.failed.dismiss()


    def extra_feature(self, obj):
        self.book = [(obj.text[5::], obj.secondary_text[10::], obj.tertiary_text[7::])]
        close_button = MDRoundFlatButton(text='Ok', on_release=self.extra_feature_dismiss)
        book_button = MDRoundFlatButton(text='Bookmark', on_release=self.bookmark)
        self.extra = MDDialog(title='Location',
                              buttons=[book_button, close_button],
                              text=str(obj.secondary_text)[10::],
                              size_hint=(0.7, 1))
        self.extra.open()

    def extra_feature_dismiss(self, obj):
        self.extra.dismiss()

    def quit_box(self):
        yes_button = MDRoundFlatButton(text='Yes', on_release=self.end_app)
        no_button = MDRoundFlatButton(text='No', on_release=self.quit_box_dismiss)
        self.quit_dialog_box = MDDialog(text='You want to quit?',
                                        buttons=[yes_button, no_button],
                                        size_hint=(0.7, 1))
        self.quit_dialog_box.open()

    def quit_box_dismiss(self, obj):
        self.quit_dialog_box.dismiss()

    def submit_pop_box(self):
        close_button = MDRoundFlatButton(text='Ok', on_release=self.submit_dialog_box_dismiss)
        self.submit_dialog_box = MDDialog(title='Submit Successful!',
                                          text='Your Application is Under Review Within 48 Hours!',
                                          buttons=[close_button],
                                          size_hint=(0.7, 1))
        self.submit_dialog_box.open()
        toast("Submitted")

    def submit_dialog_box_dismiss(self, obj):
        self.submit_dialog_box.dismiss()

    # ------------------ misc code ---------------------------------------------------
    def update_remove(self, obj):
        self.book_pop_dismiss(obj)
        self.remove_book()
        self.populate_bookmark()

    def screen_list_func(self):
        self.screen_list.append(self.root.current)

    def back_func(self):
        if self.root.current == 'available business':
            self.root.current = 'select category'
            self.root.ids.available.clear_widgets()

        elif self.root.current == 'select category':
            self.root.current = 'select lga'

        elif self.root.current == 'select lga':
            self.quit_box()

        return True

        # Scrap MDNavigationBar because you have figured out how to implement back
        # and to close persistant MDNavigationBar open for a screen, on_release: nav_id.set_state("close")

    def back_func_key(self, window, key, *args):
        if key == 27:
            self.back_func()
            return True

    def retry_connect(self, obj):
        self.failed_connection_box_dismiss(obj)
        self.connect_mongo()

    def end_app(self, obj):
        FindMyBusiness().stop()


FindMyBusiness().run()
