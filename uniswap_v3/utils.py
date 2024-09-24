def get_liquidity_0(x, sa, sb):
    return x * sa * sb / (sb - sa)


def get_liquidity_1(y, sa, sb):
    return y / (sb - sa)


def get_liquidity(x, y, sp, sa, sb):
    if sp <= sa:
        liquidity = get_liquidity_0(x, sa, sb)
    elif sp < sb:
        liquidity0 = get_liquidity_0(x, sp, sb)
        liquidity1 = get_liquidity_1(y, sa, sp)
        liquidity = min(liquidity0, liquidity1)
    else:
        liquidity = get_liquidity_1(y, sa, sb)
    return liquidity


#
# Calculate x and y given liquidity and price range
#
def calculate_x(L, sp, sa, sb):
    sp = max(min(sp, sb), sa)  # if the price is outside the range, use the range endpoints instead
    return L * (sb - sp) / (sp * sb)


def calculate_y(L, sp, sa, sb):
    sp = max(min(sp, sb), sa)  # if the price is outside the range, use the range endpoints instead
    return L * (sp - sa)


#
# Two different ways how to calculate p_a. calculate_a1() uses liquidity as an input, calculate_a2() does not.
#
def calculate_a1(L, sp, sb, x, y):
    # https://www.wolframalpha.com/input/?i=solve+L+%3D+y+%2F+%28sqrt%28P%29+-+a%29+for+a
    # sqrt(a) = sqrt(P) - y / L
    return (sp - y / L) ** 2


def calculate_a2(sp, sb, x, y):
    # https://www.wolframalpha.com/input/?i=solve+++x+sqrt%28P%29+sqrt%28b%29+%2F+%28sqrt%28b%29++-+sqrt%28P%29%29+%3D+y+%2F+%28sqrt%28P%29+-+a%29%2C+for+a
    # sqrt(a) = (y/sqrt(b) + sqrt(P) x - y/sqrt(P))/x
    #    simplify:
    # sqrt(a) = y/(sqrt(b) x) + sqrt(P) - y/(sqrt(P) x)
    sa = y / (sb * x) + sp - y / (sp * x)
    return sa ** 2


#
# Two different ways how to calculate p_b. calculate_b1() uses liquidity as an input, calculate_b2() does not.
#
def calculate_b1(L, sp, sa, x, y):
    # https://www.wolframalpha.com/input/?i=solve+L+%3D+x+sqrt%28P%29+sqrt%28b%29+%2F+%28sqrt%28b%29+-+sqrt%28P%29%29+for+b
    # sqrt(b) = (L sqrt(P)) / (L - sqrt(P) x)
    return ((L * sp) / (L - sp * x)) ** 2


def calculate_b2(sp, sa, x, y):
    # find the square root of b:
    # https://www.wolframalpha.com/input/?i=solve+++x+sqrt%28P%29+b+%2F+%28b++-+sqrt%28P%29%29+%3D+y+%2F+%28sqrt%28P%29+-+sqrt%28a%29%29%2C+for+b
    # sqrt(b) = (sqrt(P) y)/(sqrt(a) sqrt(P) x - P x + y)
    P = sp ** 2
    return (sp * y / ((sa * sp - P) * x + y)) ** 2


#
# Calculating c and d
#
def calculate_c(p, d, x, y):
    return y / ((d - 1) * p * x + y)


def calculate_d(p, c, x, y):
    return 1 + y * (1 - c) / (c * p * x)