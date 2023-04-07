
"""
B. Ловкость рук
Решение в контесте: https://contest.yandex.ru/contest/23390/run-report/85335273/
"""

def simulator_for_printing(number_of_clicks, matrix):
    simulator = []
    players = number_of_clicks * 2
    win_count = 0
    for i in range(1, 10):
        simulator_count = matrix.count(str(i))
        simulator.append(simulator_count)
    for i in simulator:
        if i == 0:
            continue
        elif i <= players:
            win_count += 1
    return win_count


if __name__ == "__main__":
    number_of_clicks = int(input())
    matrix = "".join([input().strip() for _ in range(4)])
    print(simulator_for_printing(number_of_clicks, matrix))
