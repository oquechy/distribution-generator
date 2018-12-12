import numpy as np


# a >= 0
def inverse_function_method(a):
    if a < 0:
        raise Exception('negative arg')
    c = 0.5 / (a + np.exp(-a))
    y = np.random.uniform(0, 1) / c
    if y < np.exp(-a):
        return np.log(y)
    if y <= np.exp(a) + 2 * a:
        return y - np.exp(-a) - a
    return -np.log(2 * (np.exp(-a) + a) - y)


def discrete_decomposition_method(a):
    y = np.random.uniform(0, 1)
    c = 0.5 / (a + np.exp(-a))
    if c * np.exp(-a) < y < c * np.exp(a) + 2 * c * a:
        return np.random.uniform(-a, a)
    x = np.random.exponential()
    while x < a:
        x = np.random.exponential()
    return -x if y <= c * np.exp(-a) else x


if __name__ == "__main__":
    inv_gen = [inverse_function_method(1) for _ in range(10)]
    dec_gen = [discrete_decomposition_method(1) for _ in range(10)]
    inv_gen.sort()
    dec_gen.sort()
    for p in zip(inv_gen, dec_gen):
        print(p)
