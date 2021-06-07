def datesFinder():
    dates = []
    for i in range(5):
        if potential_dates[i].get('age') > 30 and 'art' in potential_dates[i].get('hobbies') \
                and potential_dates[i].get('city') == 'Berlin':
            dates.append(potential_dates[i].get('name'))
    return(', '.join(dates))
