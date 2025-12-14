import matplotlib.pyplot as plt

def show_bmi_trend(data, name):
    dates = [row[0] for row in data]
    bmis = [row[1] for row in data]

    plt.plot(dates, bmis, marker='o')
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.title(f"BMI Trend for {name}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
