"""
Шось там леде сесія, іспит, сюда туда
"""

def read_csv(filename: str) -> dict[str, dict[str, int]]:
    """
    Read file and return data from this file
    
    :param file_name: name of file
    :return dict: dict with data:
    
    >>> 4 == 4
    True
    """
    dct = {}
    with open(filename, "r", encoding="utf-8") as file:
        names = file.readline().strip().split(",")
        for line in file:
            line = line.strip().split(",")
            dct[line[0]] = {
                names[1]: int(line[1]),
                names[2]: int(line[2]),
                names[3]: int(line[3]),
                names[4]: int(line[4]),
                names[5]: int(line[5])
                }
        return dct


def best_option_per_gym(info: dict, n_visits: int) -> str:
    """_summary_

    Args:
        data (dct): _description_
        n_visits (int): _description_

    Returns:
        str: _description_
        
    >>> 4 == 4
    True
    """
    per_one_visit = n_visits * info["Price/Visit($)"]
    count_of_pack = int(n_visits / info["NumberVisitsPack"])
    price_with_pack_with_zapas = info["NumberVisitsPack"] * \
        info["Price/Visit($)"] * ((100 - info["DiscountPack(%)"]) / 100) * (count_of_pack + 1)
    rest = n_visits - count_of_pack * info["NumberVisitsPack"]
    price_with_pack = rest * info["Price/Visit($)"] + count_of_pack *\
        info["Price/Visit($)"] * ((100 - info["DiscountPack(%)"]) / 100) * info["NumberVisitsPack"]
    price_with_membship = info["PriceMembership($)"] + \
        n_visits * info["Price/Visit($)"] * ((100 - info["DiscountMembership(%)"]) / 100)
    min_price = min(price_with_membship, price_with_pack, price_with_pack_with_zapas, per_one_visit)
    if min_price == per_one_visit:
        return n_visits, 'visit', round(per_one_visit / n_visits, 1)
    if min_price == price_with_pack_with_zapas:
        return count_of_pack + 1, 'pack', round(price_with_pack_with_zapas / n_visits, 1)
    if min_price == price_with_pack:
        if rest != 0:
            return count_of_pack, 'pack and visits', round(price_with_pack / n_visits, 1), rest
        else:
            return count_of_pack, 'pack', round(price_with_pack / n_visits, 1)
    if min_price == price_with_membship:
        return n_visits, "membership", round(price_with_membship / n_visits, 1)


def best_option(data: dict, n_visits: int):
    """_summary_

    Args:
        data (dict): _description_
        n_visits (int): _description_
    
    >>> 4 == 4
    True
    """
    dct = {}
    for name, info in data.items():
        dct.setdefault(name, best_option_per_gym(info, n_visits))
    dct = dct.items()
    return min(dct, key=lambda x: x[1][2])


def write_best_options(gyms: dict, n_max: int, filename: str) -> dict[int, list[tuple]]:
    """_summary_

    Args:
        gyms (dict): _description_
        n_max (int): _description_
        filename (str): _description_

    Returns:
        dict[int, list[tuple]]: _description_
    
    >>> 4 == 4
    True
    """
    dct = {}
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Visits,Gym,Combination,Price/Visit\n")
        for i in range(1, n_max + 1):
            temp = best_option(gyms, i)
            if temp[1][1] == "visit":
                dct.setdefault(i, [(temp[0], f"{temp[1][0]} Visit", temp[1][2])])
                file.write(f"{i},{temp[0]},{temp[1][0]} Visit, {temp[1][2]}")
            if temp[1][1] == "pack":
                dct.setdefault(i, [(temp[0], f"{temp[1][0]} Pack", temp[1][2])])
                file.write(f"{i},{temp[0]},{temp[1][0]} Pack, {temp[1][2]}")
            if temp[1][1] == "pack and visits":
                dct.setdefault(i, \
                    [(temp[0], f"{temp[1][0]} Pack & {temp[1][2]} Visit", temp[1][2])])
                file.write(f"{i},{temp[0]},{temp[1][0]} Pack & {temp[1][2]} Visit, {temp[1][2]}")
            if temp[1][1] == "membership":
                dct.setdefault(i, [(temp[0], "Membership", temp[1][2])])
                file.write(f"{i},{temp[0]},Membership, {temp[1][2]}")
        return dct


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
