import csv
import os
import pandas as pd

from compare import same_restaurant
from import_csvfile import import_csvfile
from partition import find_partitions
from calculate_ratios import calculate_ratios

#import csv files
restaurants = pd.read_csv('restaurants.tsv', sep='\t')
goldstandard = pd.read_csv('goldstandard.tsv', sep='\t')
nonduplicates = pd.read_csv('restaurants_NDPL.tsv', sep='\t')


if __name__ == "__main__":

    # create new column real_id with function partition
    restaurants['real_id'] = find_partitions(
        df=restaurants,
        match_func=same_restaurant,

    )

    # get column names and data types
    print(restaurants.dtypes)
    restaurant_iterator = restaurants.set_index("id", drop=False)

    # create csv file id_duplicates and fill it with id from duplicates
    with open('id_duplicates.tsv', mode='w') as id_file:
         fieldnames = ['id1']
         id2 = []
         id_writer = csv.DictWriter(id_file, fieldnames=fieldnames)
         id_writer.writeheader()
         for i in range(1, len(restaurant_iterator) - 1):
             for j in range(1, len(restaurant_iterator) - 1):
                 if restaurant_iterator.loc[i, "id"] < restaurant_iterator.loc[j, "id"]:
                     if restaurant_iterator.loc[i, "real_id"] == restaurant_iterator.loc[j, "real_id"]:
                         id_writer.writerow({'id1': i})
                         id2.append(j)
    id = pd.read_csv('id_duplicates.tsv', sep='\t')
    id['id2']=id2
    id.to_csv('id_files.tsv', index=False, sep='\t')

    #compare id_duplicates to goldstandard
    calculate_ratios(goldstandard, id, nonduplicates)

    # remove duplicates
    restaurants = restaurants.drop_duplicates(subset='real_id', keep='first')

    # drop column real_id, save new csv file 'restaurants_cleaned'
    data = restaurants.drop('real_id', axis=1)
    data.to_csv('restaurants_cleaned.tsv', index=False, sep='\t')

    # import into MongoDB
    path = os.path.abspath("restaurants_cleaned.tsv")
    import_csvfile(path)
    print('the file has been exported...')
