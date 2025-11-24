items = []
n = 0
i = 1
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = i - 1

def step():
    global items, n, i, j

    if n <= 1 or i >= n:
        return {"done": True}

    a = j
    b = j + 1
    swap = False

    if items[b] < items[a]:
        items[a], items[b] = items[b], items[a]
        swap = True
        j -= 1

        if j < 0:
            i += 1
            j = i - 1

        return {"a": a, "b": b, "swap": swap, "done": False}


    i += 1
    j = i - 1

    return {"a": a, "b": b, "swap": False, "done": False}