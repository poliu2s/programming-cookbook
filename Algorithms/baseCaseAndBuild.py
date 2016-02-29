# Design an algorithm to print all permutations of a string. For simplicity,
# assume all characters are unique

input = 'abcd'


def findPermutations( stringInput ):
    if len(stringInput) == 1:
        return stringInput
    elif len(stringInput) == 2:
        return [( stringInput[0] + stringInput[1]),
                stringInput[1] + stringInput[0]]
    else:
        output = []
        p = findPermutations(stringInput[:-1])
        for i in range(0, len(p)):
            for j in range(0, len(p[i]) + 1):
                output.append(p[i][0:j] + stringInput[-1] + p[i][j:])

        return output

permutations = findPermutations(input)

for permutation in permutations:
    print permutation