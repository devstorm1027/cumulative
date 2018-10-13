import pandas as pd


class cumulative(object):
    def chart_cummulate(self):
        try:
            df = pd.read_csv('input.csv')
            cols = list(df.columns.values)[1:]
            df.loc[:, cols] = df.loc[:, cols].cumsum()
            df.to_excel('input.csv', index=False)
            print("Successed!")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    cum = cumulative()
    cum.chart_cummulate()