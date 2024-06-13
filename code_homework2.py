file_name = 'new.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line)
print(file.closed)
# closed для закрытия файла, но with интереснее потому что контролирует вход в блок хода и выход из него
# (как только блок кода выполнится или возникнет какая-либо ошибка with в любом случае закроет файл)