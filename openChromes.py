
import os
import webbrowser
import time
 
def traverse(root_path):
    list_path = os.listdir(root_path)  
    
    for path in list_path:
        spath = os.path.join(root_path, path)
        print(spath)
        os.startfile(spath)
        time.sleep(3)
root_path = r"D:\Chromes"  
traverse(root_path)