import itertools
import numpy as np

def probabilty(num_ones):
    total_positions = 16

    if num_ones > total_positions:
        print("total count of phonons exceeds the atoms")
        return

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

    ordered_result = {}
    for (key1, key2), value in result.items():
        sorted_key = tuple(sorted((key1, key2)))
        if sorted_key in ordered_result:
            ordered_result[sorted_key] += value
        else:
            ordered_result[sorted_key] = value
    return ordered_result


if __name__ == "__main__":
    for phonons in range(12,16):
        result = probabilty(phonons)

        max_pos = max(result,key=result.get)
        min_pos = min(result,key=result.get)

        print(f"|{phonons}|{max_pos}|{result[max_pos]}|{min_pos}|{result[min_pos]}|")
