"""
A. Ближайший ноль
Решение в контесте: https://contest.yandex.ru/contest/23390/run-report/85327604/
"""
# решение ID 85327604
def get_data_unput():
    length_street = int(input())
    street = [int(num) for num in input().split()]
    return length_street, street


def calc(length_street, street):
    distance = [0] * length_street
    zero_position = None
    for i, elem in enumerate(street):
        if elem == 0:
            zero_position = i
            distance[i] = 0
            continue
        if elem != 0 and zero_position != None:
            distance[i] = i - zero_position
        else:
            distance[i] = length_street
    zero_position = None
    for i, elem in reversed(list(enumerate(street))):
        if elem == 0:
            zero_position = i
            continue
        if (
                elem != 0 and zero_position != None and distance[i] > zero_position - i
        ):
            distance[i] = zero_position - i
    return distance


if __name__ == '__main__':
    length_street, street = get_data_unput()
    print(*calc(length_street, street))
