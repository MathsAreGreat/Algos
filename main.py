from random import randint, shuffle


def knapsack_01(items, W):
    items = sorted(items, key=lambda e: e[-1])
    datas = {k: v for k, v in items}
    items = [
        (k, v)
        for k, v in datas.items()
        for _ in range(len(datas))
    ]
    w, v = unzip(items)
    weights, values = list(w), list(v)
    n = len(weights)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Fill the dp table
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                               [w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Maximum value that can be obtained
    max_value = dp[n][W]

    # To find which items to include, backtrack
    w = W
    included_weights = []
    included_values = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            included_weights.append(weights[i - 1])
            included_values.append(values[i - 1])
            w -= weights[i - 1]
    return max_value, [(k, v) for k, v in zip(included_weights, included_values)]


# items = [(randint(5, 20), randint(20, 40)) for _ in range(10)]
# # items = [(12, 25), (12, 23)]

# W = 30
# max_value, included_weights = knapsack_01(
#     items,
#     W
# )

# print(f"Maximum value: {max_value}")
# print(f"Included weights: {included_weights}")


def aff(arr, sep, l=None):
    arr = [f"{l}_{i} = {n}" if l else f"{n}" for i,
           n in enumerate(arr, start=1)]
    return f" {sep} ".join(arr)


def cal_inv(n, h, k, f=0):
    for i in range(1000):
        j = i+1
        nb = h*j
        if nb % n == 1:
            if f == 1:
                print(f"> {j} * h_{k} = 1 [{n}]")
            elif f < 1:
                print(f"{j}\\times\\hat n_{k}",
                      "\\equiv 1 \\pmod {", n, "} \\\\")
            return j*h


def rest_chinois(ns, rs):
    sm = " * ".join(str(e) for e in ns)
    nt = eval(sm)
    hs = [int(nt/nb) for nb in ns]
    es = []
    for i, (n, h) in enumerate(zip(ns, hs), start=1):
        e = cal_inv(n, h, i, 2)
        es.append(e)
    mul = [e*r for e, r in zip(es, rs)]
    tt = sum(mul)
    print(f"x = {tt%nt} [{nt}]")
    print()
    print("Testings :")
    for n in ns:
        print(f":: {tt} % {n} = {tt%n}")


def demo(ns, rs):
    sm = " * ".join(str(e) for e in ns)
    nt = eval(sm)
    hs = [int(nt/nb) for nb in ns]
    print("First datas :")
    for n, r in zip(ns, rs):
        print(f" > x = {r} [{n}]")
    print()
    print(f"Et on considère : n = {sm} = {nt}")
    print()
    print("New Datas :")
    sn = aff(ns, ";", l="n")
    print(">", sn)
    sn = aff(hs, ";", l="hn")
    print(">", sn)
    print()
    print("On obtient par calcul d'inverse alors :")
    es = []
    for i, (n, h) in enumerate(zip(ns, hs), start=1):
        e = cal_inv(n, h, i, 1)
        es.append(e)
    print()
    sn = aff(es, '\\\\', "e")
    print(">", sn)
    mul = [e*r for e, r in zip(es, rs)]
    sul = [f"{e} * {r}" for e, r in zip(es, rs)]
    tt = sum(mul)
    print()
    print(
        f"Une solution pour $x$ est alors : x = {aff(sul, '+')} = {tt}")
    print(
        f"Les solutions sont tous les entiers congrus à {tt} modulo {nt}")
    print(f"C'est-à-dire à {tt%nt} modulo {nt}")


def html_demo(ns, rs):
    nt = eval(" * ".join(str(e) for e in ns))
    hs = [int(nt/nb) for nb in ns]
    print()
    print("""<div class="math">""")
    print("$\\begin{cases}")
    for n, r in zip(ns, rs):
        print(f"x \\equiv {r} \\pmod", "{" + str(n) + "} \\\\")
    print("\\end{cases} $</div>")

    print()
    sm = aff(ns, '\\times')
    print(f"<p>on obtient alors : $\\; n = {sm} = {nt} $ </p>")
    print()
    sn = aff(ns, '\\\\', "n")
    hn = aff(hs, '\\\\', "\\hat n")

    print("""<p> et :</p> <div class="math">""")
    print(
        "$ \\begin{cases}", sn,
        "\\end{cases}\\so\\begin{cases}", hn,
        "\\end{cases} $</div> <p>on obtient par calcul d'inverse alors :</p>",
        """<div class="math">"""
    )
    es = []
    print("$ \\begin{cases}")
    for i, (n, h) in enumerate(zip(ns, hs), start=1):
        e = cal_inv(n, h, i)
        es.append(e)
    sn = aff(es, '\\\\', "e")
    print("\\end{cases} \\so \\begin{cases}", sn, "\\end{cases} $</div>")
    print()
    mul = [e*r for e, r in zip(es, rs)]
    sul = [f"{e} \\times {r}" for e, r in zip(es, rs)]
    tt = sum(mul)
    print()
    print(
        f"<p>Une solution pour $x$ est alors $\; x = {aff(sul, '+')} = {tt}$</p>")
    print(
        f"<p>Les solutions sont tous les entiers congrus à ${tt}$ modulo ${nt}$</p>")
    print(f"<p>C'est-à-dire à ${tt%nt}$ modulo ${nt}$</p>")


ns = [3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
rs = [randint(1, n-1) for n in ns]
print(rs)
rest_chinois(ns, rs)
