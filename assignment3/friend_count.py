import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    person = record[0]
    mr.emit_intermediate(person, 1)


def reducer(key, values):
    mr.emit((key, len(values)))


if __name__ == '__main__':
    data = open(sys.argv[1])
    mr.execute(data, mapper, reducer)
