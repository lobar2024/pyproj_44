def permutations(arr):
    if len(arr) <= 1: return [arr[:]]
    result = []
    for i in range(len(arr)):
        arr[0], arr[i] = arr[i], arr[0]
        for perm in permutations(arr[1:]):
            result.append([arr[0]] + perm)
        arr[0], arr[i] = arr[i], arr[0]
    return result

def combinations(arr, r):
    if r == 0: return [[]]
    if not arr: return []
    with_first    = [[arr[0]] + rest for rest in combinations(arr[1:], r-1)]
    without_first = combinations(arr[1:], r)
    return with_first + without_first

def subsets(arr):
    if not arr: return [[]]
    rest = subsets(arr[1:])
    return rest + [[arr[0]] + s for s in rest]

if __name__ == "__main__":
    print("Permutatsiyalar [1,2,3]:")
    for p in permutations([1,2,3]):
        print(" ", p)

    print("\nKombinatsiyalar C(4,2):")
    print(combinations([1,2,3,4], 2))

    print("\nBarcha to'plamlar {1,2,3}:")
    print(subsets([1,2,3]))
