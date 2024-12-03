def getRow(index):

    if index<3:
        return [1]*index
    else:
        out = [1]*index
        j = len(out) - 1
        while j >= 1:
            for i in range(1, j):
                out[i] = out[i] + out[i - 1]
            j -= 1
        return out        




print(getRow(9))