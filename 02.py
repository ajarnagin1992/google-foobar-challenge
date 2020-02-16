def solution(h, q):
    parentof = {} # dictionary to save time from future lookups if parentof seen before
    def helper(num, parent, height, current):
        if current not in parentof:
            parentof[current] = parent
        if (num == current):
            return(parent)
        elif (current-2**height) >= num:  # left of node
            return(helper(num, current, height-1, current-2**height))
        else:  # right of node
            return(helper(num, current, height-1, current-1))

    output = []
    for num in q:
        if num in parentof:
            output.append(parentof[num])
        else:
            output.append(helper(num, -1, h-1, 2**h-1))

    return(output)