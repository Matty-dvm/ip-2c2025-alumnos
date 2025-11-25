items = []
n = 0
i = 0
j = 0
done = False
#
def step():
    global i, j, n, items, done

    if done:
        return {"done": True}

    if j < n - 1 - i:
        a, b = j, j + 1
        j += 1

        if items[a] > items[b]:
            items[a], items[b] = items[b], items[a]
            return {"a": a, "b": b, "swap": True, "done": False}

        return {"a": a, "b": b, "swap": False, "done": False}

    else:
        i += 1
        j = 0

        if i >= n - 1:
            done = True
            return {"done": True}

        return step()