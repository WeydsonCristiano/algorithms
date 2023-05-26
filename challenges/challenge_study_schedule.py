def is_valid_period(period):
    if (
        isinstance(period, tuple)
        and len(period) == 2
        and isinstance(period[0], int)
        and isinstance(period[1], int)
        and period[0] <= period[1]
    ):
        return True
    return False


def study_schedule(permanence_periods, target_time):
    if (
        not all(is_valid_period(period) for period in permanence_periods)
        or target_time is None
    ):
        return None
    people = []
    for period in permanence_periods:
        start_time, end_time = period
        if (start_time <= target_time) and (end_time >= target_time):
            people.append(period)

    return len(people)
