import os
import time
import zipfile

source = '/home/alex/Изображения'

target_dir = '/home/alex/backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('Введите комментарий--->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
print ('Каталог успешно создан')


try:
    zip_create = zipfile.ZipFile(target, 'w')
    zip_create.write(source)
    zip_create.close()
    print ('Резервная копия успешно создана в', target)
except:
    print ('Создание резервной копии не удалось')
