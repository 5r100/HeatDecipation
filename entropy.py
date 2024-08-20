import itertools
import numpy as np

def main(num_ones_a,num_ones_b):
    total_positions = 16

    if num_ones_a + num_ones_b > total_positions:
        print("total count of phonons exceeds the atoms")
        return

    num_ones = num_ones_a+num_ones_b

    combinations = []
    for num_ones_a in range(num_ones+1):
        num_ones_b = num_ones - num_ones_a
        positions_a = list(itertools.combinations(range(total_positions), num_ones_a))
        positions_b = list(itertools.combinations(range(total_positions), num_ones_b))

        for pos_a in positions_a:
            for pos_b in positions_b:
                matrix_a = np.zeros((4,4),dtype=int)
                matrix_b = np.zeros((4,4),dtype=int)

                for p in pos_a:
                    matrix_a[p//4][p%4]=1
                for p in pos_b:
                    matrix_b[p//4][p%4]=1

                combinations.append((num_ones_a,num_ones_b))
    
    percents = {}
    for combination in combinations:
        try:
            percents[combination] += 1
        except KeyError:
            percents[combination] = 1

    result = {}
    for percent in percents:
        result[percent] = (percents[percent]/len(combinations))*100
    print(result)


if __name__ == "__main__":
    main(6,4)
