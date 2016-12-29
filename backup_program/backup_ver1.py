import os
import time

source = ['/home/alex/Изображения', '/home/alex/Музыка']

target_dir = '/home/alex/backup'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

print (zip_command)

if os.system(zip_command) == 0:
    print ('Резервная копия успешно создана в', target)
else:
    print ('Создание резервной копии не удалось')