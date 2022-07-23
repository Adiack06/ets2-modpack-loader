import subprocess
profile_file ="profile.sii"
etmp_file="maps.etmp"
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

