
from operator import itemgetter

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def _read(csv_data):
    data = {}
    for line in csv_data.split('\n'):
        name, age = line.split(';')
        data[name] = age
    return data


def _sort(data):
    return sorted(data.items(), key=itemgetter(1))


def _filter(data):
    result_data = []
    for person in data:
        if int(person[1]) < 10:
            continue
        else:
            result_data.append(person)
    return result_data


def get_users_list():
    data = _read(csv)
    sorted_data = _sort(data)
    print(sorted_data)
    return _filter(sorted_data)


if __name__ == '__main__':
    print(get_users_list())
