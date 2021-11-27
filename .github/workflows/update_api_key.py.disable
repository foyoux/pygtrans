import re
import sys

if __name__ == '__main__':
    # 读取文件
    init_py = 'pygtrans/__init__.py'
    init = open(init_py, encoding='utf-8').read()
    new_init = re.sub('\n__apikey__.*\n', f"\n__apikey__ = '{sys.argv[1]}'\n", init)
    open(init_py, 'w', encoding='utf-8').write(new_init)
