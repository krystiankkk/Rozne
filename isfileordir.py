import os
check=b'C:\\Users\\Admin\\Desktop\\drvs\\xpy501af40zva0.exe'

if os.path.isfile(check):
    print('this is file')
elif os.path.isdir(check):
    print('this is dir')
else:
    print('file not existing')