#### How to change matplotlib figsize in jupyter Notebook

[Link] ("https://matplotlib.org/3.1.3/api/_as_gen/matplotlib.pyplot.figure.html")

    import matplotlib as mpl
    import matplotlib.pyplot as plt

- Обращаемся к свойству объекта plt:


    plt.figure(figsize=(15, 5))
    plt.scatter(DATES, SUMS, color='y')
    plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='y', alpha=0.7)
    plt.show()

- Обращаемся к свойству объекта matplotlib:


    mpl.rcParams['figure.figsize'] = (15,5)
    plt.rcParams['figure.dpi'] = 150 # default for me was 75