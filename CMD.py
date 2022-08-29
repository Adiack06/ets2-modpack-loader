import os
import re
import subprocess
from objects import profile

print("were is your ets2 documents folder")

path_to_profiles = input()
profiles=[]
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
    profiles.append(profile_get_list(path_to_profiles,i))
print("witch profile do you want to mod (1 , 2 ....")
x=0
for i in profiles:
    x+=1
    print(f"{x}:{i.company_name}")
profilepicked = input()
m = 0
for i in profiles:
    m+=1
    if m==int(profilepicked):
        profilepicked = i
print("were is the mod pack file")
etmp_file=input()
profile_file=profilepicked.location
print("running installation")
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



subprocess.run(f"SII_Decrypt.exe {profile_file}")
topl =find_line("active_mods:",profile_file)
botl =find_line("customization:",profile_file)
input_file(topl,botl,profile_file,etmp_file)
print("done")




