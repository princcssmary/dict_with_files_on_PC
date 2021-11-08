import os

path = 'C:\\Users\\Admin\\Desktop\\проги для проги\\Practice Python\\'

def make_dict(path):
    main_dict = {path:[]}
    files = os.listdir(path)
    for elem in files:
        filename = os.path.splitext(elem)[-1]
        if filename == '':
            elem = os.path.join(path, elem)
            main_dict[path].append(make_dict(elem))
        else:
            main_dict[path].append(elem)
    return main_dict


print(make_dict(path))


