def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return " and ".join(items)
    else:
        new_list = items[:-1]
        end_item = items[-1]
        return ", ".join(new_list) + ", and " + end_item




            


print(oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits"]))
