import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import subprocess
import os
import re
from objects import profile

#secondWindow
def get_profiles_location(path_to_profiles):
    dir_list = os.listdir(path_to_profiles)
    for i in dir_list:
        subprocess.run(f"SII_Decrypt.exe \"{path_to_profiles}\\{i}\\profile.sii\"")
    return dir_list
def profile_get_list(path_to_profiles,dir):
    location=f"{path_to_profiles}\\{dir}\\profile.sii"
    file = open(f"{location}", "r+")
    for i in file:
        if f"face:" in i:
            face = re.sub('[^0-9]', '', i)
        if f"company_name:" in i:
            company_name= i
    result = profile(location,company_name,face)
    return result

#login screen
def find_line(quote,file):
    file = open(f"{file}", "r+")
    file.seek(0)
    line = 0
    for i in file:
        line += 1
        if f"{quote}" in i:
            print(i)
            line
            file.close()
            return line
def input_file(topl,botl,pfile,etmpfile):
    pfile = open(f"{pfile}", "r+")
    mfile = open(f"{etmpfile}", "r+")
    open(f"nfile.sii", "x")
    nfile = open(f"nfile.sii", "r+")
    pfile.seek(0)
    for i in range(topl):
        nfile.write(pfile.readline())
    for i in mfile:
        nfile.write(i)
    for i in range((botl-topl)-2):
        pfile.readline()
    for i in pfile:
        nfile.write(i)
    pfile.close()
    mfile.close()



class Login(Screen):
    def __init__(self,**kwargs):
        path_to_profiles = "C:\\Users\\joshm\\Documents\\Euro Truck Simulator 2\\profiles"
        for i in get_profiles_location(path_to_profiles):
            profiles = []
            profiles.append(profile_get_list(path_to_profiles, i))
            for i in profiles:
                print(i)






class SecondWindow(Screen):
    etmp_file = ObjectProperty(None)
    profile_file = ObjectProperty(None)

    def btn(self):
        subprocess.run(f"SII_Decrypt.exe {str(self.profile_file.text)}")
        topl = find_line("active_mods:", str(self.profile_file.text))
        botl = find_line("customization:", str(self.profile_file.text))
        input_file(topl, botl, str(self.profile_file.text), str(self.etmp_file.text))
class WindowManger(ScreenManager):
    pass
kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        return kv
if __name__ == "__main__":
    MyMainApp().run()