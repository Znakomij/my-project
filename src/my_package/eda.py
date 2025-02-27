import os.path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def perform_eda():
    # Загрузка данных
    csv_path = os.path.join('../..', 'asset-v1_Skillfactory+URFUML2023+SEP2023+type@asset+block@Credit_Default.csv')
    df = pd.read_csv(csv_path)

    # Предварительный обзор данных
    print("Первые 5 строк данных:")
    print(df.head())

    # Анализ пропущенных значений
    print("\nПропущенные значения:")
    print(df.isnull().sum())

    # Визуализация пропущенных значений
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title("Пропущенные значения")
    plt.show()

    # Построение pairplot
    sns.pairplot(df, hue="Default")
    plt.show()

    # Корреляционный анализ
    corr_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.title("Матрица корреляций")
    plt.show()

    # Анализ баланса классов
    sns.countplot(x="Default", data=df)
    plt.title("Распределение классов Default")
    plt.show()
