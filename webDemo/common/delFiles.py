import os

def del_file(path):
    for root, dir,file in os.walk(path,topdown=False):
        for name in file:
            if name.endswith((".html",".webm",'.xlsx','.json')):
                os.remove(os.path.join(root,name))
    return path
if __name__ == '__main__':
    do_del_file=del_file()