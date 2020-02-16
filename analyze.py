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
# plt.savefig('./outputs/incomes_gcf.png')
plt.show()

per_month = [0.0] * 12
for i in range(len(incomes_list)):
    m = incomes_list[i]['date_to_plot'].month
    per_month[m-1] += incomes_list[i]['summ']

for j in range(len(per_month)):
    print(j+1, per_month[j])
