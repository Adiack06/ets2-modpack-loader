import os
import re
import subprocess
from objects import profile

path_to_profiles = "C:\\Users\\joshm\\Documents\\Euro Truck Simulator 2\\profiles"
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
for i in get_profiles_location(path_to_profiles):
    profiles=[]
    profiles.append(profile_get_list(path_to_profiles,i))
    for i in profiles:
        print(i)