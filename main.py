#MIT License
#
#Copyright (c) 2021 Michele Maione
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import requests
import pandas
import matplotlib.pyplot as plt

from datetime import datetime
from io import BytesIO


def plotColumn(name, title):
    value_prev = 0
    values = []

    for i, row in extracted_data.iterrows():
        value_last = row[name]
        value_now = value_last - value_prev
        value_prev = value_last
        values.append([datetime.strptime(row['data'][0:10], '%Y-%m-%d'), value_now])

    value_data_frame = pandas.DataFrame(values, columns=['data', name])

    x = value_data_frame['data']
    y = value_data_frame[name]

    plt.title(title)
    plt.bar(x, y)
    plt.show()

url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
r = requests.get(url)
data_frame = pandas.read_csv(BytesIO(r.content), parse_dates=True)
extracted_data = data_frame[['data', 'deceduti', 'dimessi_guariti']]

plotColumn('deceduti', 'Decessi da inizio pandemia')
plotColumn('dimessi_guariti', 'Guariti da inizio pandemia')