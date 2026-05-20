#
def RowVector(x):  # vectors in numpy have to be 2-dimensional(!)
    x = np.array(x)
    return np.atleast_2d(x)

def ColVector(x):
    return RowVector(x).T
