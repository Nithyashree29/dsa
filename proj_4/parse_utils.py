from collections import namedtuple
import csv
import itertools
from datetime import datetime

def csv_parser(fname, *, delimiter=',', quotechar='"', include_header=False):
    with open(fname) as f:
        reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
        # print(not(include_header))
        if not include_header:
            next(f)
        yield from reader
        

def parse_date(value, *, fmt='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, fmt)

def extract_filed_names(fname):
    reader = csv_parser(fname, include_header=True)
    return next(reader)

def create_named_tuple_class(fname, class_name):
    fields = extract_filed_names(fname)
    return namedtuple(class_name, fields)
    
def iter_file(fname, class_name, parser):
    nt_class = create_named_tuple_class(fname, class_name)
    reader = csv_parser(fname)
    for row in reader:
        parsed_data = (parse_fn(value) for value, parse_fn in zip(row, parser))
        yield nt_class (*parsed_data)
        
def iter_combined_plain_tuple(fnames, class_name, parsers, compress_fields):
    compress_fields = tuple(itertools.chain.from_iterable(compress_fields))
    zipped_tuples = zip(*[iter_file(fname, class_name, parser) 
               for fname, class_name, parser in zip(fnames, class_name, parsers)])
    # print(next(zipped_tuples))
    merged_iter = (itertools.chain.from_iterable(zipped_tuple) for zipped_tuple in zipped_tuples)
    # yield from merged_iter
    for row in merged_iter:
        compressed_row = itertools.compress(row, compress_fields)
        yield tuple(compressed_row)
          
def create_combo_named_tuple_class(fnames, compress_fields):
    compress_fields = itertools.chain.from_iterable(compress_fields)
    field_names = itertools.chain.from_iterable(extract_filed_names(fname) for fname in fnames)
    compress_fields_names = itertools.compress(field_names, compress_fields)
    return namedtuple('Data', compress_fields_names)

def iter_combined(fnames, class_name, parsers, compress_fields):
    combo_nt = create_combo_named_tuple_class(fnames, compress_fields)
    compress_fields = tuple(itertools.chain.from_iterable(compress_fields))
    zipped_tuples = zip(*[iter_file(fname, class_name, parser) 
               for fname, class_name, parser in zip(fnames, class_name, parsers)])
    # print(next(zipped_tuples))
    merged_iter = (itertools.chain.from_iterable(zipped_tuple) for zipped_tuple in zipped_tuples)
    # yield from merged_iter
    for row in merged_iter:
        compressed_row = itertools.compress(row, compress_fields)
        yield combo_nt(*compressed_row)

def filter_iter_combined(fnames, class_names, parsers, compress_fields, *, key=None):
    iter_combo = iter_combined(fnames, class_names, parsers, compress_fields)
    yield from filter(key, iter_combo)
     
     
def group_data(fnames, class_names, parsers, compress_fields, filter_key, group_key,):
    data = filter_iter_combined(fnames,class_names, parsers, compress_fields
                                                 , key=filter_key)
    # data = (row for row in data if row.gender == gender)
    
    sorted_data = sorted(data, key=group_key)
    groups = itertools.groupby(sorted_data, key=group_key)
    group_counts = ((g[0], len(list(g[1]))) for g in groups)
    return sorted(group_counts, key=lambda row:row[1], reverse=True)


 


    
        
     
    