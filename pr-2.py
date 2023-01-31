import csv
answ_dict = {'appid': '', 'name': '', 'release_date': '', 'english': '', 'developer': '', 'publisher': '', 'platforms': '', 'required_age': '', 'categories': '', 'genres': '', 'steamspy_tags': '', 'achievements': '', 'positive_ratings': '', 'negative_ratings': '', 'average_playtime': '', 'median_playtime': '', 'owners': '', 'price': ''}

a = input('Укажите год релиза или нажмите Enter, чтобы пропустить:')
answ_dict['release_date'] = a
a = input('Укажите язык игры (1 - английский, 0 - нет) или нажмите Enter, чтобы пропустить:')
answ_dict['english'] = a
a = input('Укажите разработчика игры или нажмите Enter, чтобы пропустить:')
answ_dict['developer'] = a
a = input('Укажите издателя игры или нажмите Enter, чтобы пропустить:')
answ_dict['publisher'] = a
a = input('Укажите платформу (windows;mac;linux - если вариантов несколько, указать через точку с запятой) или нажмите Enter, чтобы пропустить:')
answ_dict['platforms'] = a
a = input('Укажите возрастную категорию (0, 3, 7, 12, 16, 18) или нажмите Enter, чтобы пропустить:')
answ_dict['required_age'] = a
a = input('Укажите категорию игры (если вариантов несколько, указать через точку с запятой) или нажмите Enter, чтобы пропустить:')
answ_dict['categories'] = a
a = input('Укажите жанр игры (если вариантов несколько, указать через точку с запятой) или нажмите Enter, чтобы пропустить:')
answ_dict['genres'] = a
a = input('Укажите тэги (если вариантов несколько, указать через точку с запятой) или нажмите Enter, чтобы пропустить:')
answ_dict['steamspy_tags'] = a
a = input('Желаемые ачивки игры (количество, не менее) или нажмите Enter, чтобы пропустить:')
answ_dict['achievements'] = a
a = input('Укажите позитивный рейтинг (не менее) или нажмите Enter, чтобы пропустить: ')
answ_dict['positive_ratings'] = a
a = input('Укажите негативный рейтинг (не более) или нажмите Enter, чтобы пропустить: ')
answ_dict['negative_ratings'] = a
a = input('Укажите количество пользователей игры или нажмите Enter, чтобы пропустить:')
answ_dict['owners'] = a
a = input('Укажите максимальную цену игры или нажмите Enter, чтобы пропустить:')
answ_dict['price'] = a

#answ_dict = {'appid': '', 'name': '', 'release_date': '2005', 'english': '1', 'developer': '', 'publisher': '', 'platforms': 'linux', 'required_age': '0', 'categories': '', 'genres': '', 'steamspy_tags': '', 'achievements': '0', 'positive_ratings': '', 'negative_ratings': '', 'average_playtime': '', 'median_playtime': '', 'owners': '', 'price': ''}
#print (answ_dict)

group_compare = ['english', 'required_age']
group_list = ['platforms', 'developer', 'publisher', 'categories', 'genres', 'steamspy_tags']
group_more = ['achievements', 'positive_ratings']
group_less = ['negative_ratings', 'price']
flag = 0

with open('RESULT.csv', 'w+', encoding='utf-8-sig') as f_res:

    with open('steam.csv', 'r', encoding='utf-8-sig') as f1:
        f2 = csv.DictReader(f1)
        writer = csv.DictWriter(f_res, answ_dict.keys())
        for row in f2:
            flag = 0

            date = row.get('release_date')
            date = date[:4]
            date_a = answ_dict.get('release_date')
            if len(date_a) <= 1:
                date_a = 0
            if (date != date_a) and (date_a != 0):
                #print (row.get('appid'), ': ', 'date не сошлось')
                continue

            for i in group_compare:
                if (row.get(i) != answ_dict.get(i)) and (len(answ_dict.get(i)) != 0):
                    flag = 1
                    #print(row.get('appid'), ': ', i, ' не сошлось')
                    continue
            if flag == 1:
                continue

            for i in group_list:
                i_cat = row.get(i).lower().split(';')
                i_answ = answ_dict.get(i).lower().split(';')
                if (i_answ != ['']) and ((set(i_answ).issubset(i_cat)) != True):
                    flag = 1
                    #print(row.get('appid'), ': ', i, ' не сошлось. ')
                    break#continue#
            if flag == 1:
                continue

            for i in group_more:
                if (len(answ_dict.get(i)) != 0) and (int(row.get(i)) < int(answ_dict.get(i))):
                    flag = 1
                    #print(row.get('appid'), ': ', i, ' не сошлось')
                    continue
            if flag == 1:
                continue

            for i in group_less:
                if (len(answ_dict.get(i)) != 0) and (float(row.get(i)) > float(answ_dict.get(i))):
                    flag = 1
                    #print(row.get('appid'), ': ', i, ' не сошлось')
                    continue
            if flag == 1:
                continue

            ownrs = row.get('owners').split('-')
            ownrs_a = int(answ_dict.get('owners')) if len(answ_dict.get('owners')) > 0 else ''
            if (ownrs_a != '') and ((ownrs_a < int(ownrs[0])) or (ownrs_a > int(ownrs[1]))):
                #print(row.get('appid'), ': ', 'ownrs не сошлось')
                continue

            print ('Выбрана игра: ', row.get('name'))

            writer.writerow(row)