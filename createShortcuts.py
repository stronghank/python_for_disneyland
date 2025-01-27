import os, shutil
import winshell
folder = "C:\\Chromes"
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

for i in range(1, 21):
    winshell.CreateShortcut(
        Path=os.path.join("C:\\Chromes", str(i) + ".lnk"),
        Target=r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        Icon=(r"C:\Program Files\Google\Chrome\Application\chrome.exe", 0),
        Arguments="--user-data-dir=C:\\Chromes_data\\" + str(i) + r" https://www.hongkongdisneyland.com/zh-hk/merchstore/limited/",
        Description="Create shortcut"
    )