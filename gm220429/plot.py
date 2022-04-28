import pandas as pd, seaborn as sns, glob
import matplotlib.pyplot as plt


def load_data():
    for f in glob.glob('destar*/*_best.txt'):
        print(f)
    # dstar_sidetoside/test_dstar_headtotail_wspread_00.10_log.txt_best.txt
    # pd.load_dataset('/home/sheffler/Documents/GM220429/440447_tiptotip/')

    print(df)


def main():

    df = load_data()
    assert 0

    penguins = sns.load_dataset("penguins")
    g = sns.PairGrid(penguins)
    g.map(sns.scatterplot)
    plt.show()


if __name__ == '__main__':
    main()