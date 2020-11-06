for _ in grades:
    if _ > 38:
        if _%5 >= 3:
            l.append(_ + (5 - _%5))
        else:
            l.append(_)
    else:
        l.append(_)