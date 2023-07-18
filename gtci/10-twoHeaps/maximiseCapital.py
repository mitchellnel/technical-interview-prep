from heapq import *


def maximise_capital(capital, profits, n_projects, initial_capital):
    min_capital_heap = []
    max_profits_heap = []

    # insert all project capitals into a min heap
    for proj_num, proj_capital in enumerate(capital):
        heappush(min_capital_heap, (proj_capital, proj_num))

    # try to find a total of n_projects best projects
    available_capital = initial_capital
    for _ in range(n_projects):
        # find all projects that can be selected with the current available
        #   capital, and insert their profits to a min heap
        while len(min_capital_heap) > 0 and min_capital_heap[0][0] <= available_capital:
            capital, proj_num = heappop(min_capital_heap)
            heappush(max_profits_heap, (-profits[proj_num], proj_num))

        # terminate early if we are not able to find any projects can that be
        #   completed with our available capital
        if len(max_profits_heap) == 0:
            break

        # select the project with the highest profit
        available_capital += -heappop(max_profits_heap)[0]

    return available_capital


def main():
    print("Maximum capital: " + str(maximise_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " + str(maximise_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
