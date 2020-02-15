from astropy.table import Table, vstack
import os


def clean(year_lim, directory='../data', data_file='../processed_data/clean_data.csv'):
    print('cleaning data')
    table4 = Table()
    for file in os.listdir(directory):
        if file.endswith(".csv") & file.startswith("Surf"):
            file = os.path.join(directory, file)
            table1 = Table.read(file)
            date = table1['yyyy-mm-ddThh:mm']
            lat = table1['Latitude [degrees_north]']
            long = table1['Longitude [degrees_east]']
            temp = table1['TEMP [deg C]']
            year = list()
            for elt in date:
                year.append(int(elt[0:4]))

            table2 = Table()
            table2.add_column(year, name='year')
            table2.add_column(lat, name='lat')
            table2.add_column(long, name='long')
            table2.add_column(temp, name='temp')

            table3 = table2[(table2['year'] >= year_lim) & (table2['temp'] > 0)]
            table4 = vstack([table4, table3])

    table4.write(data_file, format='csv', overwrite=True)
