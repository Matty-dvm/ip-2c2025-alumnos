items = []
n = 0
i = 0
j = 0
min_idx = 0
phase = "scan"   # "scan" para buscar mínimo, "swap" para hacer el intercambio final

def init(vals):
    global items, n, i, j, min_idx, phase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    phase = "scan"

def step():
    global items, n, i, j, min_idx, phase

    if n <= 1 or i >= n - 1:
        return {"done": True}

    # -------------------------
    # Fase 1: búsqueda del mínimo
    # -------------------------
    if phase == "scan":
        a = min_idx
        b = j
        swap = False

        if items[b] < items[min_idx]:
            min_idx = b

        j += 1

        # Terminó la búsqueda en esta pasada
        if j >= n:
            phase = "swap"
        return {"a": a, "b": b, "swap": swap, "done": False}

    # -------------------------
    # Fase 2: hacer el swap i <-> min_idx
    # -------------------------
    if phase == "swap":
        a = i
        b = min_idx
        swap = False

        if min_idx != i:
            items[a], items[b] = items[b], items[a]
            swap = True

        # Preparar siguiente pasada
        i += 1
        if i >= n - 1:
            return {"a": a, "b": b, "swap": swap, "done": False}

        j = i + 1
        min_idx = i
        phase = "scan"

        return {"a": a, "b": b, "swap": swap, "done": False}
