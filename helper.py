insertPodLibrary="""
# Tools
pod 'SwiftFormat/CLI', '~> 0.40.0'
pod 'SwiftLint', '~> 0.35.0'
"""

# make Podfile
def podInit(path):
    import os
    os.chdir(path)
    os.system('pod init')

# write library to Podfile
def writeLibrary(path):
    insertText(path+'/Podfile', 3, insertPodLibrary)

def insertText(path, insert_line, text):
    with open(path, 'r') as file:
        lines = file.readlines()

    if len(lines) > int(insert_line):
        lines.insert(2, text)

    with open(path, 'w') as file:
        file.writelines( lines )

def podInstall(path):
    import os
    os.system('pod install')

if __name__ == "__main__":
    import sys
    podInit(sys.argv[1])
    writeLibrary(sys.argv[1])
    podInstall(sys.argv[1])
