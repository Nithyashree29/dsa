import itertools
import constants
import csv
import os
print(os.getcwd())
import parse_utils
from datetime import datetime
from functools import partial
# see a sample of what is in each file

# for fname in constants.fnames:
#     print(fname)
#     with open(fname) as f:
#         print(next(f), end ='')
#         print(next(f), end ='')
#         print(next(f), end ='')
#     print()

# for fname in constants.fnames:
#     with open(fname) as f:
#         reader = csv.reader(f, delimiter=',', quotechar='"')
#         # print(type(reader))
#         print(next(reader))
#         print(next(reader))
#     print()
    
# header row(field names)
# for fname in constants.fnames:
#     print(fname)
#     reader = parse_utils.csv_parser(fname, include_header=True)
#     print(next(reader))
    
# # Just the data
# for fname in constants.fnames:
#     print(fname)
#     reader = parse_utils.csv_parser(fname)
#     print(next(reader))
#     print(next(reader), end = '\n')


# for fname, class_name, parser in zip(constants.fnames, constants.class_names, constants.parsers):
#     file_iter = parse_utils.iter_file(fname, class_name, parser)
#     print(fname)
#     for _ in range(3):
#         print(next(file_iter))
#     print()       
    
# gen  = parse_utils.iter_combined_plain_tuple(constants.fnames, constants.class_names, constants.parsers, constants.compress_fileds) 
# print(list(next(gen)))
# print(list(next(gen)))   

# nt  = parse_utils.create_combo_named_tuple_class(constants.fnames,constants.compress_fileds) 
# print(nt._fields)

data_iter  = parse_utils.iter_combined(constants.fnames,constants.class_names, constants.parsers, constants.compress_fileds) 
for row in itertools.islice(data_iter, 5):
    print(row)
    
print('-------------------------------')

def group_key(item):
    return item.gender, item.vehicle_make

filtered_iter = parse_utils.filter_iter_combined(constants.fnames,constants.class_names, constants.parsers, constants.compress_fileds
                                                 , key=lambda row:row.ssn == '100-53-9824')
cutoff_date = datetime(2017, 3, 1)
data = parse_utils.filter_iter_combined(constants.fnames,constants.class_names, constants.parsers, constants.compress_fileds
                                                 , key=lambda row:row.last_updated >= cutoff_date)
# for row in data:
#     print(row)
# sorted_data = sorted(data, key=group_key)
# groups = itertools.groupby(sorted_data, key=group_key)

# # group_1, group_2 = itertools.tee(groups, 2)
# # rg1 = next(group1)
# # rg2 = next(group2)
# # print(rg1[0], id(rg1[1]))
# # print(rg2[0], id(rg2[1]))
# group_1 =  itertools.groupby(sorted_data, key=group_key)
# group_2 =  itertools.groupby(sorted_data, key=group_key)
# group_f = (item for item in group_1 if item[0][0] == 'Female')
# data_f = ((item[0][1], len(list(item[1]))) for item in group_f)
# for row in data_f:
#     print(row)



# group_m = (item for item in group_2 if item[0][0] == 'Male')
# data_m = ((item[0][0], len(list(item[1]))) for item in group_m)
# # data is exhausted list(item[1]))) from above condition, solution is to seperate group 1 and group2
# for row in data_m:
#     print(row)

# def group_key(item):
#     return item.vehicle_make


# data_1, data_2 = itertools.tee(data, 2)

# data_m = (row for row in data_1 if row.gender == 'Male')
# sorted_data_m = sorted(data_m, key=group_key)
# groups_m = itertools.groupby(sorted_data_m, key=group_key)
# for row in groups_m:
#     print(row[0], len(list(row[1])))

# data_f = (row for row in data_2 if row.gender == 'Female')
# sorted_data_f = sorted(data_f, key=group_key)
# groups_f = itertools.groupby(sorted_data_f, key=group_key)
# for row in groups_f:
#     print(row[0], len(list(row[1])))

cutoff_date = datetime(2017, 3, 1)
def filter_key(cutoff_date, gender, row):  #Partial function
    return row.last_updated >= cutoff_date and row.gender == gender

results = parse_utils.group_data(constants.fnames,constants.class_names, constants.parsers, constants.compress_fileds
                                                 , filter_key=partial(filter_key, cutoff_date, 'Female'),
                                                 group_key=lambda row: row.vehicle_make)
for row in results:
    print(row)








