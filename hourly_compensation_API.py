global _hour_dict


def _init_params():
    global _hour_dict

    _hour_dict = {
        'WEEKDAY': {
            '00': 25,
            '09': 15,
            '18': 20,
        },
        'WEEKEND': {
            '00': 30,
            '09': 20,
            '18': 25,
        }
    }


def _get_day_type(day: str):
    if day.upper().startswith('S'):
        return 'WEEKEND'
    return 'WEEKDAY'


def _get_hour_frame(hour: str):
    split_hour = hour.split(':')

    hour_num = int(split_hour[0])
    minute_num = int(split_hour[1])

    if hour_num > 18 or (hour_num == 18 and minute_num > 0) or (hour_num == 0 and minute_num == 0):
        return '18'
    elif hour_num > 9 or (hour_num == 9 and minute_num > 0):
        return '09'

    return '00'


def _get_compensation(day_hour_interval: str):
    global _hour_dict

    first_day_letter = day_hour_interval[0]
    day_type = _get_day_type(first_day_letter)

    hour_interval = day_hour_interval[2:]
    hour_interval_split = hour_interval.split('-')
    first_hour = hour_interval_split[0]
    second_hour = hour_interval_split[1]

    hour_frame = _get_hour_frame(first_hour)

    day_frame_price = _hour_dict[day_type][hour_frame]

    first_hour_split = first_hour.split(':')
    second_hour_split = second_hour.split(':')

    first_hour_num = float(first_hour_split[0])
    second_hour_num = float(second_hour_split[0])

    first_minute_num = float(first_hour_split[1])
    first_minute_num_to_hour = first_minute_num / 60
    second_minute_num = float(second_hour_split[1])
    second_minute_num_to_hour = second_minute_num / 60

    first_hour_plus_minutes = first_hour_num + first_minute_num_to_hour
    second_hour_plus_minutes = second_hour_num + second_minute_num_to_hour

    hour_num_difference = second_hour_plus_minutes - first_hour_plus_minutes

    return hour_num_difference * day_frame_price


def process_worker_compensation(text_line: str):
    _init_params()

    line_split = text_line.split('=')
    name = line_split[0]
    schedule = line_split[1]

    schedule_split = schedule.split(',')

    total_sum = 0
    for hour_day in schedule_split:
        total_sum += _get_compensation(hour_day)
    
    total_sum = int(total_sum) if total_sum.is_integer() else round(total_sum, 2)
    final_str = 'The amount to pay {0} is: {1} USD'.format(name, total_sum)

    return final_str

