"""
module info goes here
"""
def count(sequence, item):
    """
    function info goes here
    """
    item_count = 0
    for number in sequence:
        if number == item:
            item_count += 1
    return item_count

help(count)
