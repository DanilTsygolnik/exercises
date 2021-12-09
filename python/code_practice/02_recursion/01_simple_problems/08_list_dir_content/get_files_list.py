import os


def get_files_list(src_dir:str = os.getcwd()) -> list:
    """Return all paths to files in src_dir and subdirs as a list"""

    src_dir_items = os.listdir(src_dir) # получить список содержимого src_dir
    all_paths_list = []                 # создать список-заготовку на вывод

    for item in src_dir_items:
        item_path = os.path.join(src_dir, item) # путь к текущему файлу, который проверяем
        if os.path.isfile(item_path):           # если это файл:
            all_paths_list.append(item_path)        # поместить в список на вывод (форматированная строка)
        else: # если директория:
            # добавить в общий список на вывод файлы из этой поддиректории
            all_paths_list.extend(get_files_list(item_path))

    return all_paths_list


# тестовый вывод путей к отдельным файлам, содержащимся в текущей директории и ее поддиректориях
for i in get_files_list():
    print(i)
