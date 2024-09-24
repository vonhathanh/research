from utils import *


def estimate_y_amount(p, a, b, x):
    print(f"Example 1: how much of USDC I need when providing {x} ETH at this price and range?")
    sp = p ** 0.5
    sa = a ** 0.5
    sb = b ** 0.5
    L = get_liquidity_0(x, sp, sb)
    y = calculate_y(L, sp, sa, sb)
    print("amount of USDC y={:.2f}".format(y))


def estimate_x_and_y(X: str, Y: str, p: float, a: float, b: float, x: float, y: float, p1: float):
    """

    :param X: name of token X
    :param Y: name of token Y
    :param p: current price
    :param a: PA
    :param b: PB
    :param x: liquidity provided of X
    :param y: liquidity provided of Y
    :param p1: target price
    """
    print(f"Current position: "
          f"price: {p}, "
          f"lower_bound: {a}, "
          f"upper bound: "
          f"{b}, "
          f"initial x: {x}, "
          f"initial y: {y}, "
          f"target price: {p1}")
    print(f"Using the position above, what are asset balances at {p1} USDC per {X}?")
    sp = p ** 0.5
    sa = a ** 0.5
    sb = b ** 0.5
    # calculate the initial liquidity
    L = get_liquidity(x, y, sp, sa, sb)

    sp1 = p1 ** 0.5

    x1 = calculate_x(L, sp1, sa, sb)
    y1 = calculate_y(L, sp1, sa, sb)
    print("Amount of ARB x={:.2f} amount of USDC y={:.2f}".format(x1, y1))

    # alternative way, directly based on the whitepaper

    # this delta math only works if the price is in the range (including at its endpoints),
    # so limit the square roots of prices to the range first
    sp = max(min(sp, sb), sa)
    sp1 = max(min(sp1, sb), sa)

    delta_p = sp1 - sp
    delta_inv_p = 1 / sp1 - 1 / sp
    delta_x = delta_inv_p * L
    delta_y = delta_p * L
    x1 = x + delta_x
    y1 = y + delta_y
    pre_value = x*p + y
    post_value = x1*p1 + y1
    print("delta_x={:.2f} delta_y={:.2f}".format(delta_x, delta_y))
    print("Amount of ARB x={:.2f}, value: {:.2f} amount of {} y={:.2f}".format(x1, x1 * p1, Y, y1))
    print("pre value: {:.2f}, post value: {:.2f}, profit: {:.2f}".format(pre_value, post_value, post_value - pre_value))
    print("-----------------------------------------------------------------------------------------------------------")


def main():
    X = "ARB"
    Y = "USDC"
    # estimate_y_amount(1.1426, 0.2843, 1.9984, 1000)
    estimate_x_and_y(X, Y, 1.1426, 0.2843, 1.9984, 1000, 2348.34, 0.29)
    estimate_x_and_y(X, Y, 1.1426, 0.2843, 1.9984, 1000, 2348.34, 1.99)


main()
