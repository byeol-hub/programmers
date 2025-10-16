def solution(schedules, timelogs, startday):
    
    def to_minutes(hhmm):
        hh = hhmm // 100
        mm = hhmm % 100
        return hh * 60 + mm

    answer = 0

    for person_idx, logs in enumerate(timelogs):
        want_min = to_minutes(schedules[person_idx])
        
        on_time_count = 0

        for day_index in range(7):
            weekday = ((startday + day_index - 1) % 7) + 1
            if weekday in (6, 7):
                continue

            actual_min = to_minutes(logs[day_index])

            if (actual_min is None) or (actual_min > want_min + 10):
                break
            else:
                on_time_count += 1

        if on_time_count == 5:
            answer += 1

    return answer
