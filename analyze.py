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


def count_scholarship(incomes_list):
    scholarship = 0
    salary = 0
    vacation = 0

    for i in incomes_list:
        if i['name'] == 'Зачисление стипендии':
            scholarship += i['summ']

        if i['name'] == 'Зачисление зарплаты':
            salary += i['summ']

        if i['name'] == 'Зачисление зарплаты':
            salary += i['summ']

    print(scholarship)
