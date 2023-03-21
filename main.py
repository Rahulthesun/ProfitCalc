from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.lang import Builder





class ProfitCalcApp(MDApp):
    def find_result(self,args):
        if self.cost.text=="":
            self.SP_val.text= self.Total_SP_Val.text = "PLEASE ENTER A VALUE ABOVE"
            self.SP_val.theme_text_color=self.Total_SP_Val.theme_text_color="Error"
        else:
            cost = int(self.cost.text)
            quantity= int(self.quantity.text)
            p_margin= self.profit_margin.value

            sp = cost/(1-(p_margin/100))
            Total_sp= sp * quantity

            self.SP_val.text = str(round(sp,2))
            self.Total_SP_Val.text=str(round(Total_sp,2))






    def build(self):
        screen =Screen()
        self.theme_cls.primary_palette = "Teal"
        self.toolbar=MDTopAppBar(title= "PROFIT CALC", pos_hint= {'top': 1})
        self.cost=MDTextField(hint_text= "Cost",  helper_text= "In Rupees",helper_text_mode= "on_focus",mode= "rectangle",size_hint= (0.5,0.1),pos_hint={'center_x':0.3,'center_y': 0.8})
        self.quantity=MDTextField(hint_text= "Quantity" , helper_text= "In Tons",helper_text_mode= "on_focus",mode= "rectangle",size_hint= (0.5,0.1),pos_hint= {'center_x':0.3,'center_y': 0.65})
        self.profit_margin=MDSlider(min= 0,max= 50,value=20,step= 0.5,hint= True,hint_bg_color= "white",track_color_active= "red",size_hint= (0.5,0.1),pos_hint= {'center_x':0.3,'center_y': 0.5})

        print(self.cost.text)

        self.SP_val=MDLabel(text= '---',size_hint=(0.5, 0.1),pos_hint={'center_x': 0.5, 'center_y': 0.2},theme_text_color= "Primary")
        self.Total_SP_Val=MDLabel(text= "---",size_hint= (0.5, 0.1),pos_hint= {'center_x': 0.5, 'center_y': 0.1},theme_text_color= "Primary")

        self.SP=MDLabel(text= "SELLING PRICE",
        size_hint=(0.5,0.1),
        pos_hint= {'center_x':0.3,'center_y': 0.25},
        theme_text_color= "Secondary"
        )


        self.Total_SP=MDLabel(text= "TOTAL SELLING PRICE",
        size_hint=(0.5,0.1),
        pos_hint= {'center_x':0.3,'center_y': 0.15},
        theme_text_color= "Secondary"
        )





        screen.add_widget(self.toolbar)
        screen.add_widget(self.cost)
        screen.add_widget(self.quantity)
        screen.add_widget(self.profit_margin)
        screen.add_widget(MDFillRoundFlatButton(
            text="CALCULATE",
            font_size=17,
            pos_hint={"center_x": 0.3, "center_y": 0.35},
            on_press=self.find_result))
        screen.add_widget(self.SP)
        screen.add_widget(self.SP_val)
        screen.add_widget(self.Total_SP)
        screen.add_widget(self.Total_SP_Val)


        return screen




ProfitCalcApp().run()