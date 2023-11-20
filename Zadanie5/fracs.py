import math


def add_frac(frac1, frac2):
    lcm = math.lcm(frac1[1], frac2[1])

    frac1_num = frac1[0] * (lcm // frac1[1])
    frac2_num = frac2[0] * (lcm // frac2[1])

    result_num = frac1_num + frac2_num
    result_denom = lcm

    gcd = math.gcd(result_num, result_denom)
    result = [result_num // gcd, result_denom // gcd]

    return result


def sub_frac(frac1, frac2):  # frac1 - frac2
    lcm = math.lcm(frac1[1], frac2[1])

    frac1_num = frac1[0] * (lcm // frac1[1])
    frac2_num = frac2[0] * (lcm // frac2[1])

    result_num = frac1_num - frac2_num
    result_denom = lcm

    gcd = math.gcd(result_num, result_denom)
    result = [result_num // gcd, result_denom // gcd]

    return result


def mul_frac(frac1, frac2):  # frac1 * frac2
    result_num = frac1[0] * frac2[0]
    result_denom = frac1[1] * frac2[1]

    gcd = math.gcd(result_num, result_denom)
    result = [result_num // gcd, result_denom // gcd]

    return result


def div_frac(frac1, frac2):  # frac1 / frac2
    if is_zero(frac2):
        raise ValueError('Denominator cannot be zero.')
    result_num = frac1[0] * frac2[1]
    result_denom = frac1[1] * frac2[0]

    gcd = math.gcd(result_num, result_denom)
    result = [result_num // gcd, result_denom // gcd]

    return result


def is_positive(frac):  # bool, czy dodatni
    return frac[0] * frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):  # -1 | 0 | +1
    lcm = math.lcm(frac1[1], frac2[1])

    frac1_num = frac1[0] * (lcm // frac1[1])
    frac2_num = frac2[0] * (lcm // frac2[1])

    if frac1_num == frac2_num:
        return 0
    elif frac1_num > frac2_num:
        return 1
    else:
        return -1


def frac2float(frac):
    if frac[1] == 0:
        return float(0)
    return frac[0] / frac[1]
