def mystery3(lst: list) -> bool:
    """lst est une liste d'int non vide"""
    if len(lst) > 1:
        if lst[0] > lst[1]:
            return False
        else:
            return mystery3(lst[1:])
            # on rappelle que lst[1:] désigne la liste composée
            # de lst[1],lst[2], etc jusqu'au dernier élément de lst
    else:
        return True
