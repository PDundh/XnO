from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import time
from Algo import *

Side = True
Turn = True
X=list()
O=list()

def All():
    global Side
    Side = not Side
    class GameScreen(Widget):
        
        def on_kv_post(self,touch):
            if Side == False:
                PC = str(Algo(X,O))
                self.ids[PC].background_color = (1,1,0,1)
                self.ids[PC].text = "X" 
                X.append(int(PC))
                self.ids[str(PC)].disabled=True
            print("heheh")
        def gameplay(self,play,*args):
            #global Turn
            if Side is True: 
                self.ids[str(play)].background_color = (1,1,0,1)
                self.ids[str(play)].text = "X" 
                X.append(play)
                self.ids[str(play)].disabled=True
                if wincheck(X) is True:
                    end("X")
                elif len(X)==5:
                    draw()
                else:
                    PC = str(Algo(O,X))
                    self.ids[PC].background_color = (0,1,1,1)
                    self.ids[PC].text = "O" 
                    O.append(int(PC))
                    self.ids[str(PC)].disabled=True
                    if wincheck(O) is True:
                        end("O")
            else:
                self.ids[str(play)].background_color = (0,1,1,1)
                self.ids[str(play)].text = "O" 
                O.append(play)
                self.ids[str(play)].disabled=True
                if wincheck(O) is True:
                    end("O")
                else:
                    PC = str(Algo(X,O))
                    self.ids[PC].background_color = (1,1,0,1)
                    self.ids[PC].text = "X" 
                    X.append(int(PC))
                    self.ids[str(PC)].disabled=True
                    if wincheck(X) is True:
                        end("X")
                    elif len(X)==5:
                        draw()            

    def wincheck(check):
        wins=[[11,12,13],[21,22,23],[31,32,33],[11,21,31],[12,22,32],[13,23,33],[11,22,33],[31,22,13]]
        for win in wins:
            if all(play in check for play in win) is True:
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