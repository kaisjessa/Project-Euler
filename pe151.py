from random import randint


def num_split(n):
    if n == 1:
        return []
    if n == 2:
        return [1]
    if n == 4:
        return [2, 1]
    if n == 8:
        return [4, 2, 1]
    if n == 16:
        return [8, 4, 2, 1]
    return None


def count_possibilities(repeats=1):
    dc = {}
    dc[(16,)] = 1
    for i in range(repeats):
        next = {}
        for k in dc.keys():
            arr = list(k)
            for i in range(len(arr)):
                d = arr[i]
                el = arr[:i] + num_split(d) + arr[i + 1 :]
                el.sort()
                el = el[::-1]
                next[tuple(el)] = next.get(tuple(el), 0) + dc[k] / len(k)
        dc = next
    return dc


# def simulate_batch(repeats=1):
#     counts = [0 for i in range(16)]
#     for i in range(repeats):
#         arr = [16]
#         for i in range(1, 16):
#             if len(arr) == 1:
#                 counts[i] += 1
#             index = randint(0, len(arr) - 1)
#             page = arr.pop(index)
#             while page > 1:
#                 page //= 2
#                 arr.append(page)
#     return counts


if __name__ == "__main__":
    total = 0
    for n in (8, 4, 2):
        dc = count_possibilities(16 - n)
        a = dc[(n,)]
        total += a
    print(round(total, 6))
