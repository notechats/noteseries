import math
import random


# 判断是否为素数
def is_prime(n, d=2):
    if math.sqrt(n) < d:
        return True  # 为素数时返回True
    if n % d == 0:
        return False  # 不为素数时返回False
    else:
        return is_prime(n, d + 1)


def is_prime2(n, trials=10):
    assert n >= 2
    # 2是素数~
    if n == 2:
        return True
    # 先判断n是否为偶数，用n&1==0的话效率更高
    if n % 2 == 0:
        return False
    # 把n-1写成(2^s)*d的形式
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert (2 ** s * d == n - 1)

    # 测试以a为底时，n是否为合数
    def try_composite(a):
        if pow(a, d, n) == 1:  # 相当于(a^d)%n
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:  # 相当于(a^((2^i)*d))%n
                return False
        return True  # 以上条件都不满足时，n一定是合数

    # trials为测试次数，默认测试5次
    # 每次的底a是不一样的，只要有一次未通过测试，则判定为合数
    for i in range(trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True  # 通过所有测试，n很大可能为素数

# 生成素数数组
def prime_generate(max_size=10, max_value=None):
    result = []
    max_value = max_value or 100000000000
    for i in range(2, max_value):  # 生成前100中的素数，从2开始因为2是最小的素数
        x = is_prime(i)  # i为素数是返回True，则将x加入result数组中;2为测试值
        if x:
            result.append(i)
            if len(result) >= max_size:
                break
    return result
