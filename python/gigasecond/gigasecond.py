from datetime import timedelta

def add_gigasecond(date):
    ''' returns the date someone reaches / reached their gigasecond birthday '''
    return date + timedelta(seconds = 10 ** 9)
