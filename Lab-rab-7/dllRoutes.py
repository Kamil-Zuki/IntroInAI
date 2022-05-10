
def add_destination():
    distenationName = input("Название пункта назначения? ")
    number = input("Номер поезда? ")

    my_string = str(input('Время отправления(yyyy-mm-dd hh:mm): '))    
    departureTime = datetime.strptime(my_string, "%Y-%m-%d %H:%M")

    schedule = {
        'distenationName': distenationName,
        'number': number,
        'departureTime': departureTime,
    }


    # Добавить словарь в список.
    schedules.append(schedule)
    # Отсортировать список в случае необходимости.
    if len(schedules) > 1:
        schedules.sort(key=lambda item: item.get('distenationName', ''))

def destination_list():
    my_string2 = str(input('Введите время отправки для поиска существующих рейсов: (yyyy-mm-dd hh:mm): '))
    departureTime2=datetime.strptime(my_string2, "%Y-%m-%d %H:%M")

    if next((x for x in schedules if x["departureTime"] >= departureTime2), None)!=None:

        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )


        count = 0    
        for schedule in schedules:
            if schedule["departureTime"] >= departureTime2:
                count += 1 
                print('  ',count,'\t\t  ',schedule.get('distenationName', ''),'\t\t\t   ', schedule.get('number', ''),'\t ', schedule.get('departureTime', ''))

    else:
        print("Рейсов нет после указанного времени")

        


# In[ ]:




