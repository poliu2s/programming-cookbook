# Given two strings, write a method to decide if one is a permutation of another


def is_permutation(query_string, comparison_string):
    # Build hashtables for both and compare frequency
    qsHashMap = {}
    csHashMap = {}
    for c in query_string:
        if c in qsHashMap:
            print 'here'
            qsHashMap[c] += 1
        else:
            qsHashMap[c] = 1

    for c in comparison_string:
        if c in csHashMap:
            csHashMap[c] += 1
        else:
            csHashMap[c] = 1

    # Compare hashmaps of two strings
    if qsHashMap == csHashMap:
        print True
    else:
        print False


is_permutation("abc", "cab")
is_permutation("abc", "casdfa")