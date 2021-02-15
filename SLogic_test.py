structure = """
ScreenManager:
    transition: 
    id: screen_manager
#---------------------- Select LGA ------------------------------------------         
    Screen:
        name: 'select lga'
        MDBottomNavigation:
            MDBottomNavigationItem:
                name: 'find business'
                text: 'Find Business'
                icon: 'account-search'
        #         MDBoxLayout:
        #             orientation: 'vertical'
        #             MDToolbar:
        #                 title: "Select Your LGA"
        #             ScrollView:
        #                 MDList:
        #                     OneLineListItem:
        #                         id: alimosho
        #                         text: 'Alimosho'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: ajeromi
        #                         text: 'Ajeromi-Ifelodun'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: kosofe
        #                         text: 'Kosofe'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: mushin
        #                         text: 'Mushin'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: oshodi
        #                         text: 'Oshodi-Isolo'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: ojo
        #                         text: 'Ojo'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: ikorodu
        #                         text: 'Ikorodu'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: surulere
        #                         text: 'Surulere'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: agege
        #                         text: 'Agege'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: ifako
        #                         text: 'Ifako-Ijaiye'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: somolu
        #                         text: 'Somolu'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: amuwo
        #                         text: 'Amuwo-Odofin'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: lagos_mainland
        #                         text: 'Lagos Mainland'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: ikeja
        #                         text: 'Ikeja'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: eti
        #                         text: 'Eti-Osa'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: badagry
        #                         text: 'Badagry'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: apapa
        #                         text: 'Apapa'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: lagos_island
        #                         text: 'Lagos Island'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: epe
        #                         text: 'Epe'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        #                     OneLineListItem:
        #                         id: ibeju_lekki
        #                         text: 'Ibeju-Lekki'
        #                         on_release: screen_manager.current = 'select category'
        #                         on_release: app.text_collector_location(self)
        #                         on_release: app.screen_list_func()
        # 
        #     MDBottomNavigationItem:
        #         name: 'Add'
        #         text: 'Add Business'
        #         icon: 'plus'
        #         MDBoxLayout:
        #             orientation: 'vertical'
        #             MDToolbar:
        #                 title: "Add Business"
        #             ScrollView:
        #             MDRectangleFlatButton:
        #                 id: lga_btn
        #                 text: 'Select LGA'
        #                 pos_hint: {'x':0.2, 'y':.8}
        #                 on_release: screen_manager.current = 'add lga'
        #             MDRectangleFlatButton:
        #                 id: category_btn
        #                 text: 'Select Category'
        #                 pos_hint: {'x':0.2, 'y':.7}
        #                 on_release: screen_manager.current = 'add category'
        #             MDTextField:
        #                 id: add_name
        #                 hint_text: "Enter Business Name:"
        #                 multiline: True
        #                 pos_hint: {'x':0.2, 'y':0.55}
        #                 size_hint_x: None
        #                 width: 400
        #             MDTextField:
        #                 id: add_location
        #                 hint_text: "Enter Business Location:"
        #                 pos_hint: {'x':0.2, 'y':0.45}
        #                 multiline: True
        #                 size_hint_x: None
        #                 width: 400
        #             MDTextField:
        #                 id: add_number
        #                 hint_text: "Enter Business Number (080xxxxxxxx):"
        #                 pos_hint: {'x':0.2, 'y':0.35}
        #                 multiline: True
        #                 size_hint_x: None
        #                 width: 400
        #                 input_filter: 'int'
        #             MDRectangleFlatButton:
        #                 text: 'Submit'
        #                 pos_hint: {'x':0.4, 'y':.25}
        #                 on_release: app.submit()
        #                         
        #                         
        #     MDBottomNavigationItem:
        #         name: 'bookmark'
        #         text: 'Bookmarks'
        #         icon: 'bookmark'
        #         MDBoxLayout:
        #             orientation: 'vertical'                
        #             MDToolbar:
        #                 title: "Added Bookmarks"
        #             ScrollView:
        #                 MDList:
        #                     id: bookmark                                             
#---------------------- Select Category ------------------------------------------     
    Screen:
        name: 'select category'
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: "images/blackback.png"
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                id: category_title
                title: "Select Category"
                right_action_items: [["images/back.png", lambda x: app.back_func()]]
            Screen:
                canvas.before:
                    Rectangle:
                        pos: self.pos
                        size: self.size
                        source: "images/background.png"
                ScrollView:
                    MDList:
                        OneLineListItem:
                            id: ict
                            text: 'ICT'
                            on_release: screen_manager.current = 'available business'
                            on_release: app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: photography
                            text: 'Photography'
                            on_release:  screen_manager.current = 'available business'
                            on_release: app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: phone_stores
                            text: 'Phone Stores'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: fashion
                            text: 'Fashion Designer'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self) 
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: makeup
                            text: 'Makeup Artiste and Studios'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: hair
                            text: 'Hair Vendor'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: boutique
                            text: 'Boutique'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: graphics_designer
                            text: 'Graphics Designer'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: restaurants
                            text: 'Restaurants'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)  
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: handy_men
                            text: 'Handy Men'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: game_centers
                            text: 'Game Centers'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: wedding
                            text: 'Wedding Essentials and Souvenirs'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: household
                            text: 'Household Appliances'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: telecomms
                            text: 'Telecomms Office'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: banks
                            text: 'Banks'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: isp
                            text: 'Internet Service Providers'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: bakery
                            text: 'Bakery'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: hotels
                            text: 'Hotels'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                        OneLineListItem:
                            id: hangouts
                            text: 'Hangout Spots'
                            on_release: screen_manager.current = 'available business'
                            on_release:  app.text_collector_category(self)
                            on_release: app.screen_list_func()
                                        
#---------------------- Available Business ------------------------------------------                                    
    Screen:
        name: 'available business'
        id: available_screen
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: "images/blackback.png"
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: "Available Businesses"
                right_action_items: [["images/back.png", lambda x: app.back_func()]]
            Screen:
                canvas.before:
                    Rectangle:
                        pos: self.pos
                        size: self.size
                        source: "images/background.png"
                ScrollView:
                    MDList:
                        id: available
                                                              
#---------------------- Add LGA ------------------------------------------         
    Screen:
        name: 'add lga'
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: "images/blackback.png"
        MDBoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: "Add Your LGA"
            Screen:
                canvas.before:
                    Rectangle:
                        pos: self.pos
                        size: self.size
                        source: "images/background.png"
                ScrollView:
                    MDList:
                        OneLineListItem:
                            text: 'Alimosho'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Ajeromi-Ifelodun'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Kosofe'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Mushin'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Oshodi-Isolo'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Ojo'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Ikorodu'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Surulere'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Agege'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Ifako-Ijaiye'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Somolu'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Amuwo-Odofin'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Lagos Mainland'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Ikeja'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Eti-Osa'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Badagry'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Apapa'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Lagos Island'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Epe'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                        OneLineListItem:
                            text: 'Ibeju-Lekki'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_lga_btn(self)
                                        
#---------------------- Add Category ------------------------------------------     
    Screen:
        name: 'add category'
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source: "images/blackback.png"
        BoxLayout:
            orientation: 'vertical'
            MDToolbar:
                title: "Add Category"
            Screen:
                canvas.before:
                    Rectangle:
                        pos: self.pos
                        size: self.size
                        source: "images/background.png"
                ScrollView:
                    MDList:
                        OneLineListItem:
                            id: ict
                            text: 'ICT'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Photography'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Phone Stores'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Fashion Designer'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Makeup Artiste and Studios'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Hair Vendor'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Boutique'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Graphics Designer'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Restaurants'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Handy Men'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Game Centers'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Wedding Essentials and Souvenirs'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Household Appliances'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Telecomms Office'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Banks'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Internet Service Providers'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Bakery'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Hotels'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)
                        OneLineListItem:
                            text: 'Hangout Spots'
                            on_release: screen_manager.current = 'select lga'
                            on_release: app.change_text_category_btn(self)                                      
                                    
"""