import os
from webDemo.common.singleton import Singleton
class handle_del_file(Singleton):
    def del_file(slef,path):
        for root, dir,file in os.walk(path,topdown=False):
            for name in file:
                if name.endswith((".html",".webm",'.xlsx','.json')):
                    os.remove(os.path.join(root,name))
        return path
    if __name__ == '__main__':
        do_del_file=del_file()