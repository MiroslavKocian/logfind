import sys
import subprocess
from sets import Set

def run():
    file_with_duplicates = open('C:\Users\MiukoAdmin\projects\logfind\matching_files_with_duplicates.txt', 'w+')
    file_with_duplicates.close()
    with open('C:\Users\MiukoAdmin\projects\.logfind', 'r') as file_with_regex:
        string_with_regex = file_with_regex.readline()
    if sys.argv[1] == "-o":  
        for arg in range(2,len(sys.argv)-1):
            pattern_arguments = ""
            pattern_arguments += "\\b" + sys.argv[arg] + "\\b" + ","
        pattern_arguments += "\\b" + sys.argv[len(sys.argv)-1] + "\\b"
       
        p = subprocess.Popen(["powershell.exe",
                      """Get-ChildItem C:\Users\MiukoAdmin\projects -Recurse -ErrorAction SilentlyContinue |
                      Where-Object {$_.Name -match %s} | Select-String -Pattern %s""" % (string_with_regex, pattern_arguments)+ " | select fileName" +
                      "  | sc C:\Users\MiukoAdmin\projects\logfind\matching_files_with_duplicates.txt"
                      ])                 
        p.communicate()
       
    else:
        patterns = ""
        for arg in range(1,len(sys.argv)):
            patterns += " | Select-String -Pattern " + sys.argv[arg]
       
       
        p = subprocess.Popen(["powershell.exe",
                      """Get-ChildItem C:\Users\MiukoAdmin\projects -Recurse -ErrorAction SilentlyContinue |
                      Where-Object {$_.Name -match %s} """ %(string_with_regex) + patterns  + " | select fileName" +
                      "  | sc C:\Users\MiukoAdmin\projects\logfind\matching_files_with_duplicates.txt"
                      ])   
        p.communicate()  
       
    unique_files = Set([])
    file_with_duplicates = open('C:\Users\MiukoAdmin\projects\logfind\matching_files_with_duplicates.txt', 'r+')
    for line in file_with_duplicates:
        file_from_line = line[11:len(line) - 2]
        unique_files.add(file_from_line)
    file_with_duplicates.close()
    file = open('C:\Users\MiukoAdmin\projects\logfind\matching_files.txt', 'w+')
    file.write("\n".join(unique_files))
    file.close()
   
    p2 = subprocess.Popen(["powershell.exe", "Get-Content C:\Users\MiukoAdmin\projects\logfind\matching_files.txt"])   
    p2.communicate()
       
           
 
 