import glob
import os
files=glob.glob('C:\\Users\\Admin\\Desktop\\drvs\\*.*')
files.sort(key=os.path.getmtime)
print('\n'.join(files))