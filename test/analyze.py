import matplotlib.pyplot as plt


#calculates the carbon equivalent CE-IIW
def carbon_eq(c, mn, cr, mo, ni, v, cu):
    ceq = c+mn/6+(cr+mo+v)/5+(cu+ni)/15
    return ceq


#lower critical temperature (F)
def lower_critical(mn, si, cr, ni):
    ae1 = 1333-25*mn+40*si+42*cr-26*ni
    return ae1


def plot_data(x,y):
    c.execute('SELECT * stressrelief2 WHERE')
    x = []
    y = []
    for row in x:
        #x.append
