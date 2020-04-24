import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    order_id = record[1]
    mr.emit_intermediate(order_id, record)


def reducer(_key, list_of_values):
    orders = []
    line_items = []
    for record in list_of_values:
        destination = orders if record[0] == 'order' else line_items
        destination.append(record)
    for order in orders:
        for line_item in line_items:
            mr.emit((order + line_item))


if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
