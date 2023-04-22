
import subprocess
import chardet

ping_list_1 = ['ping', 'yandex.ru']
ping_list_2 = ['ping', 'youtube.com']
my_list = [ping_list_1, ping_list_2]
form_encoding = ''
for i in range(len(my_list)):
    ping_process = subprocess.Popen(my_list[i], stdout=subprocess.PIPE)
    for bytes_line in ping_process.stdout:
        detect_form = chardet.detect(bytes_line)
        form_encoding = detect_form['encoding']
        print(bytes_line.decode(encoding=detect_form['encoding']))

print(f'Тип используемой кодировки: {form_encoding}')
