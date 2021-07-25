import os
from tabulate import tabulate as t
os.system("clear")

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def ShowMenu():
    print(" LIST DIR ".center(50,"#"))
    table_data = [['FILE NAME', 'TYPE', 'SIZE'],]
    # insert file to table data
    for items in os.listdir():
        table_data.append([items,"?",convert_bytes(os.stat(items).st_size)])

    print(t(table_data, headers='firstrow', tablefmt='grid'))
    # list_dir=[str(x+1)+". "+os.listdir()[x] for x in range(len(os.listdir()))]
    # print(*list_dir,sep="\n")
# Menu
while(True):
    print(" FILE MANAGER 0.0 ".center(50,"#"))
    print("#"+" 1. View Dir".ljust(48)+"#")
    print("".center(50,"#"))
    menu=input("# Select menu : ")
    print("".center(50,"#"))

    if(menu=="1"):
        ShowMenu()
    print("".center(50,"#"))
    
    program_status=input("# Quit? (y/n) : ").lower()
    if(program_status=="y"): break
    else: continue

