import runpy
enter = int(input("1 = User_Info Table, 2 = Theater Table  \n"))

def chooseTable(enter):
    if enter == 1:
        runpy.run_path(path_name='user_info_table.py')
    if enter == 2:
        runpy.run_path(path_name='theater_table.py')

chooseTable(enter)