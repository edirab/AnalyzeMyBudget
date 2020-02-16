from parse import incomes
import matplotlib
import matplotlib.pyplot as plt


def plot_scatter():
    incomes_list = incomes()
    DATES = list()
    SUMS = list()

    print()
    for i in incomes_list:
        DATES.append(i['date_to_plot'])
        SUMS.append(i['summ'])

    plt.plot(DATES, SUMS)
    plt.savefig('./outputs/incomes_plot.png')
    plt.show()

    plt.scatter(DATES, SUMS)
    plt.savefig('./outputs/incomes_scatter.png')
    plt.show()

    plt.gcf().autofmt_xdate()
    # plt.savefig('./outputs/incomes_gcf.png')
    plt.show()


def plot_per_month(incomes_list):

    per_month = [0.0] * 12
    for i in range(len(incomes_list)):
        m = incomes_list[i]['date_to_plot'].month
        per_month[m-1] += incomes_list[i]['summ']

    # for j in range(len(per_month)):
    #    print(j+1, per_month[j])

    return per_month


'''
Зачисление стипендии
Зачисление зарплаты
SBOL перевод
Прочие выплаты
Отпускные
Командировочные
Расчет при увольнении
'''


def get_names(incomes_list):
    names = set()
    for i in incomes_list:
        if i['name'] not in names:
            names.add(i['name'])
    return names


def count_categories(incomes_list):
    scholarship = 0
    salary = 0
    from_others = 0
    vacation = 0

    rest = 0

    for i in incomes_list:
        str_name = i['name']
        if str_name == 'Зачисление стипендии':
            scholarship += i['summ']

        elif str_name == 'Зачисление зарплаты' or str_name == 'Командировочные' or str_name == 'Расчет при увольнении':
            salary += i['summ']

        elif 'SBOL перевод' in str_name or 'TINKOFF' in str_name:
            from_others += i['summ']

        elif str_name == 'Отпускные':
            vacation += i['summ']

        else:
            rest += i['summ']

    # print(scholarship, salary, from_others, vacation, rest)
    cats_dict = dict()
    cats_dict['Стипендия'] = int(scholarship)
    cats_dict['Зарплата'] = int(salary)
    cats_dict['От физ. лиц'] = int(from_others)
    cats_dict['Отпускные'] = int(vacation)
    cats_dict['Прочее'] = int(rest)

    return cats_dict

