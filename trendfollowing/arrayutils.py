def maskarray(x, n):
    maskedarray = np.ma.array(x, mask=False)
    maskedarray.mask[:n] = True
    return maskedarray
