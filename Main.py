from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

Turn = True
X=list()
O=list()
def All():
    class GameScreen(Widget):
        def gameplay(self,play,*args):
            global Turn
            if Turn is True: 
                self.ids[str(play)].background_color = (1,1,0,1)
                self.ids[str(play)].text = "X" 
                X.append(play)
                if wincheck(X) is True:
                    end("X")
                if len(X)==5:
                    draw()
            else:
                self.ids[str(play)].background_color = (0,1,1,1)
                self.ids[str(play)].text = "O" 
                O.append(play)
                if wincheck(O) is True:
                    end("O")
            self.ids[str(play)].disabled=True
            Turn = not Turn


    def wincheck(check):
        wins=[[11,12,13],[21,22,23],[31,32,33],[11,21,31],[12,22,32],[13,23,33],[11,22,33],[31,22,13]]
        for k in wins:
            if all(x in check for x in k) is True:
                return True
        return False

    def Reset():
        global Turn, X, O
        Turn = True
        X=list()
        O=list()
        xnoApp.get_running_app().stop()
        All()

    def end(winner):
            layout = GridLayout(cols = 1) 
            popupLabel = Label(text = winner + " Wins", font_size=20) 
            closeButton = Button(text = "Reset") 
            layout.add_widget(popupLabel) 
            layout.add_widget(closeButton)
            pop=Popup(title="Game Over", content=layout,size_hint=(None,None), size=(200,200))
            pop.open()
            closeButton.bind(on_press=lambda x:Reset())

    def draw():
            layout = GridLayout(cols = 1) 
            popupLabel = Label(text = "Its a Draw!", font_size=20) 
            closeButton = Button(text = "Reset") 
            layout.add_widget(popupLabel) 
            layout.add_widget(closeButton)
            pop=Popup(title="Game Over", content=layout,size_hint=(None,None), size=(200,200))
            pop.open()
            closeButton.bind(on_press=lambda x:Reset())




    class xnoApp(App):
        def build(self):
            return GameScreen()
    xnoApp().run()
All()