import tkinter as tk
import sys
import os
sys.path.append(os.path.join(sys.path[0], '../../Dropbox/Front end/Blocks/'))
import Face

root=tk.Tk()
root.title("Lazario  alfa 0.1.0") #Название окна
root.configure(bg='#313440')
root.geometry('900x700') #Разрешение окна
root.resizable(False, False) #запрет маштабирования п

'''
#файлы с граяическим созданием всех блоков, отдельно файл с классом  соединения всех блоков
'''

Menu=Face.TopMenu(root)
Time=Face.ChangeTime(root)
Set=Face.SetLog(root)
Date=Face.DateTime(root)
СurrentLog=Face.CurrentLog(root)


IPcontroll=Face.IPcontrol(root)

root.mainloop()
