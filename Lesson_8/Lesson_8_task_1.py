# 1) Определить количество различных подстрок с использованием хеш-функции. Задача: на вход
# функции дана строка, требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


def all_substr(s):
    hash_lst = []      # Для хранения хэшей
    str_lst = []      # для хранения подстрок

    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            k = hashlib.sha1(s[j:j+i].encode('utf-8')).hexdigest()
            if k not in hash_lst:
                str_lst.append(s[j:j+i])

    if len(str_lst) > 0:
        return f'In string "{s}" {len(str_lst)} unique substrings were found: \n{str_lst}'
    return 'Nothing. Empty str (-_-)'


some_str = input('Enter something: ')
print(all_substr(some_str))
