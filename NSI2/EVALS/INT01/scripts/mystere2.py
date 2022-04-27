def mystery2(lst: list) -> int:
    """lst est une liste d'int "éventuellement vide"""
    if lst != []:
        return lst[0] + mystery2(lst[1:])
        # on rappelle que lst[1:] désigne la liste
        # composée de lst[1],lst[2], etc jusqu'au dernier élément de lst
    else:
        return 0

