def add_time(start, duration,day = ''):
    week = ['MONDAY' , 'TUESDAY' , 'WEDNESDAY' , 'THURSDAY' , 'FRIDAY' , 'SATURDAY' , 'SUNDAY']
    week1 = ['Monday' , 'tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday' , 'Sunday']

    count = 0
    start_time = start.split()
    init_tag = start_time[1]
    temp = start_time[0].split(':')
    init_hrs = int(temp[0])
    init_mins = int(temp[1])
    temp = duration.split(':')
    duration_hrs = int(temp[0])
    duration_mins = int(temp[1])
    new_mins_temp = int(init_mins + duration_mins)
    new_hrs_temp = init_hrs + duration_hrs + (new_mins_temp//60)
    new_mins = new_mins_temp % 60
    new_hrs = new_hrs_temp % 12
    temp = new_hrs_temp // 12
    if init_tag == 'AM':
        if temp % 2 == 0:
            new_tag = 'AM'
        elif temp % 2 != 0:
            new_tag = 'PM'
    elif init_tag == 'PM':
        if temp % 2 == 0:
            new_tag = 'PM'
        elif temp % 2 != 0:
            new_tag = 'AM'

    gap = 12 - init_hrs
    no_of_days = (new_hrs_temp - gap - init_hrs)//24

    if init_tag == new_tag and duration_hrs >= 24 :
        no_of_days = no_of_days + 1
    if init_tag  == 'PM' and  new_tag == 'AM'  :
        no_of_days = no_of_days + 1
    no_of_days_tag = ''
    if no_of_days < 1 :
        no_of_days = 0
    if no_of_days == 1 :
        no_of_days_tag = ' (next day)'
    elif no_of_days > 1 :
        no_of_days_tag = ' (' + str(no_of_days) + ' days later)'




    if new_hrs == 0:
        new_hrs = 12
    if new_mins < 10:
        new_mins = '0' + str(new_mins)

    new_result = str(new_hrs)  + ':' + str(new_mins) + ' ' + str(new_tag)

    if (day != '') and (day.upper() in week)  :
        day_pos = week.index(day.upper())
        day_pos = no_of_days + day_pos
        day_pos = day_pos % 7
        if no_of_days_tag == '' :
            new_result = str(new_hrs)  + ':' + str(new_mins) + ' ' + str(new_tag) + ', ' + week1[day_pos]
        else :
            new_result = str(new_hrs)  + ':' + str(new_mins) + ' ' + str(new_tag) + ', ' + week1[day_pos] + no_of_days_tag
    elif (day == '') and  no_of_days_tag != '' :
        new_result = str(new_hrs)  + ':' + str(new_mins) + ' ' + str(new_tag) +  no_of_days_tag


    return new_result
