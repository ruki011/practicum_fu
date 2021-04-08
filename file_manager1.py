# -*- coding: utf-8 -*-

import os
import shutil

 
  #1 задание          
def create_new_folder():
    name_new = input('Им создаваемого файла: ')
    os.mkdir(name_new)    
        
    #2 задание
def delate_folder(name_delete):
    name_delete = input('Имя удаляемой папки: ')
    os.rmdir(name_delete)
    return 'папка удалена'
           
    #3 задание
        
    #4 задание
way='C:\универ\4 семестр\практикум(unix)\l2'
name = input('Введите имя нового файла: ')
way=way+'/'+name
def create_new_file(way):
    text_file = open("way", "w")
    return text_file
'''with open(name_new, 'w') as file:
        print('Создан')
        file.close()'''
    
       
    #5 задание
def write_on_file(way,text_file):
    new_text=input('Введите текст, который хотите добавить: ')
    text_file.write(new_text)
        
    return text_file
    
    
    #6 задание
def print_file_text(way):
    f = open('way','r') 
    return print(*f)
    
#7 задание
def delate_file(name_delete):
    name_delete = input('Имя удаляемого файла: ')
    os.remove(name_delete)
    return 'файл удален'

#8 задание
def copy_file(file,way_orig, way_copy):
    shutil.copy(way_orig, way_copy)
    return 'файл скопирован'
    
    #9 задание
def move_file(way_s,way_f):
    os.rename(way_s,way_f)
    return 'файл перемещен'
    
     #10 задание
def rename_file(way):
    name = input('Введите новое имя файла: ')
    if os.path.exists(name) == True:
        print('Такое имя уже есть')
    else:
        os.rename(way, name)
        print('файл переименован')
     



 
while True:
    come = input('Чтобы начать работу, напишите - YES : ')
    if come == 'YES':
        print('= = = Файловий менеджер = = =')
        print(' 1.	Создание папки')
        print(' 2.	Удаление папки по имени;')
        print(' 3.	Перемещение между папками')
        print(' 4.	Создание пустых файлов с указанием имени;')
        print(' 5.	Запись текста в файл;')
        print(' 6.	Просмотр содержимого текстового файла; /n 7.	Удаление файлов по имени; /n 8.	Копирование файлов из одной папки в другую; /n 9.	Перемещение файлов; /n 10.	Переименование файлов.')

    else:
        print('Выход из программы ')
        break
        
        
    manage = input('-- Выберите номер команды: -- ')
    if manage == '1':
        create_new_folder()       
    if manage == '2':
        delate_folder()
    if manage == '3':
        print('пустаааа')
    if manage == '4':
        way=os.getcwd()
        name = input('Введите имя нового файла: ')
        way=way+'/'+name
        create_new_file(way)
    if manage == '5':
        
        create_new_file(name_file)
        
    if manage == '6':
        pass
    if manage == '7':
        pass
    if manage == '8':
        pass
    if manage == '9':
        pass
    if manage == '10':
        pass
        
    
    
        
    
    
        
    
    
    
    
        
    
    
    
    
    
        
        
        
        
    
    
    
    
    
    