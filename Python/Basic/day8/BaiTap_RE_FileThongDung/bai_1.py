# Bai 1
import re

lst_dates = ['22/12/90a', '22/12a/90', '22a/12/90', '22/02/900', '22/02/90', '22/99/90', '99/02/90', '22/12/60', '22/12/90',
             '22/12/1970', '22/02/1990', '22/12/2000', '67/12/2000', '22/55/2000', '22/12/6789', '22/12/2089',
             '22/12/20692', '22/12/2090', '22/12/2100']

str_pattern = r'^([1-9]|[0-2]\d|3[0-1])/([1-9]|0[1-9]|1[0-2])/(\d{2}$|199\d$|20[0-8]\d$)'

for str_date in lst_dates:
    if re.match(str_pattern, str_date):
        print(str_date,'->','Correct')
    else:
        print(str_date, '->', 'Wrong')