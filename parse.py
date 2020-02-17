from bs4 import BeautifulSoup
from datetime import datetime


def spends():
    my_spends = []
    file = open('html/card_info.html', 'r', encoding='utf-8')

    html = file.read()
    # print(html[:500])

    soup_spends = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    transactions = soup_spends.find_all('div', class_='trs_it')
    # print("Total transactions:", len(transactions))

    # print(soup.find_all('div', class_='trs_it'))
    # print(soup.find_all('div', class_='trs_sum-am'))

    for tr in transactions:
        one_tr = dict()
        name = tr.find(class_='trs_name').get_text().strip()

        date_hr = tr.find(class_='trs_date').get_text().strip()
        date_iso = tr.find('span', class_='idate')['data-date']
        date_to_plot = datetime.strptime(date_iso, "%d.%m.%Y")

        summ = tr.find(class_='trs_sum').get_text().strip()
        summ = summ.replace(',', '.')
        summ = summ.replace('\u202f', '')
        summ = float(summ)

        cat = tr.find(class_='trs_sic').get_text().strip()

        one_tr['name'] = name
        one_tr['date_hr'] = date_hr
        one_tr['date_iso'] = date_iso
        one_tr['date_to_plot'] = date_to_plot
        one_tr['summ'] = summ
        one_tr['cat'] = cat

        # print(type(tr))
        # print(tr.get_text())
        # print(tr.find(class_='trs_name').get_text())
        # print(tr.find(class_='trs_date').get_text())
        # print(tr.find(class_='trs_sum').get_text())
        # print(tr.find(class_='trs_sic').get_text())

        my_spends.append(one_tr)
    return my_spends


def incomes():
    my_incomes = list()

    file = open('html/incomes.html', 'r', encoding='utf-8')
    html = file.read()
    soup_incomes = BeautifulSoup(html, 'html.parser')

    transactions = soup_incomes.find_all('div', class_='trs_it')
    # print("Total transactions incomes:", len(transactions))

    for tr in transactions:
        # print(type(tr))
        one_tr = dict()
        name = tr.find(class_='trs_name').get_text().strip()

        date_hr = tr.find(class_='trs_date').get_text().strip()
        date_iso = tr.find('span', class_='idate')['data-date']
        date_to_plot = datetime.strptime(date_iso, "%d.%m.%Y")

        summ = tr.find(class_='trs_sum').get_text().strip()
        summ = summ.replace(',', '.')
        summ = summ.replace('\u202f', '')
        summ = float(summ)

        cat = tr.find(class_='trs_sic').get_text().strip()

        one_tr['name'] = name
        one_tr['date_hr'] = date_hr
        one_tr['date_iso'] = date_iso
        one_tr['date_to_plot'] = date_to_plot
        one_tr['summ'] = summ
        one_tr['cat'] = cat

        # print(name, date_to_plot, summ, cat)
        my_incomes.append(one_tr)

        '''
        SBOL перевод 5469****3493 А. ЕВГЕНИЙ ВИКТОРОВИЧ 2019-03-08 00:00:00 5600.0 Прочие поступления
        Зачисление стипендии 2019-03-05 00:00:00 3900.0 Прочие поступления
        
        {'name': 'Расчет при увольнении', 
         'date_hr': '5 февраля 2020 14:37:38', 
         'date_iso': '05.02.2020', 
         'date_to_plot': datetime.datetime(2020, 2, 5, 0, 0), 
         'summ': 4266.76, 'cat': 'Прочие поступления'
         }
        '''
    return my_incomes

