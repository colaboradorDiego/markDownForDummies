import sys

from os import path
from os import walk


def getTags(texto):
    """
    TODO QUE APUNTES VENGA COMO PARAMETO
    """
    tStart = 'apuntes'
    tEnd = '.'

    iStart = texto.index(tStart)
    iEnd = texto.index(tEnd)

    tags = texto[iStart+len(tStart)+1:iEnd].split("\\")
    tag = ' '.join(tags)
    return tag


def siExiste(startPath):
    startPath = path.abspath(path.join(path.dirname(__file__), startPath))
    print("Start folder:", startPath)
    if path.exists(startPath):
        return startPath

    else:
        print("No existe la carpeta", startPath)
        return False


def startWalk(startPath):
    startPath = siExiste(startPath)

    if startPath:
        tags = []

        for root, dirs, files in walk(startPath):
            for name in files:
                archivo = path.join(root, name)
                if archivo.endswith('.txt') or archivo.endswith('.md'):
                    tags.append([getTags(archivo), archivo])

        with open('testData\\create.sql', 'w') as f:
            createDB = """
.open --new apuntes.db
create virtual table archivo using fts4(tag, text, path);

            """
            f.write('%s\n' % createDB)
            for tag in tags:
                sql = f"insert into archivo values('{tag[0]}', readfile('{tag[1]}'), '{tag[1]}');"
                f.write('%s\n' % sql)



def main(argv):
    if len(argv) == 2:
        print("Walker escaneando en:", argv[1])
        startWalk(argv[1])

    else:
        msg = """
Al menos debe indicar un path inicial de busqueda
ej:
    python walkForders.py start_folder
"""
        print(msg)


def init():
    if __name__ == '__main__':
        sys.exit(main(sys.argv))


init()
