from parse import incomes
import matplotlib
import matplotlib.pyplot as plt

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
plt.savefig('./outputs/incomes_gcf.png')
plt.show()
