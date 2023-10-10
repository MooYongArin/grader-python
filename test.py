def total(pocket):
    total = 0
    for item in pocket:
        total += item*pocket[item]
    return total
def take(pocket, money_in):
    for item in money_in:
        if item in pocket:
            pocket[item] += money_in[item]
        else:
            pocket[item] = money_in[item]
    return pocket
def pay(pocket, amt):
    pay = {}
    copy_pocket = pocket.copy()
    if total(pocket) < amt:
        return {}
    for item in pocket:
        if amt/item>1:
            x = amt//item
            amt -= x*item
            pay[item] = x
            pocket[item] -= x
        if pocket[item]<0:
            # make pocket the same
            for item in pocket:
                pocket[item] = copy_pocket[item]
            return {}
    return pay
exec(input().strip())