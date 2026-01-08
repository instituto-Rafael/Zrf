"""
Mathematical Operations Library for RAFAELIA/ZRF
RAFCODE-Φ | Mathematical Framework with Derivatives, Antiderivatives, and Inverses

This module implements 69 mathematical operations including:
- Direct derivatives (1-23)
- Antiderivatives/Integrals (24-46)
- Inverse operations (47-69)
"""

import math
from typing import Callable, Union, List

# NumPy is optional - only needed for future vectorization features
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


# ============================================================================
# SECTION 1: DIRECT DERIVATIVES (Operations 1-23)
# ============================================================================

def derivative_polynomial(coefficients: List[float], x: float) -> float:
    """1. Derivative of polynomial function"""
    n = len(coefficients)
    if n <= 1:
        return 0.0
    result = sum(i * coefficients[i] * (x ** (i - 1)) for i in range(1, n))
    return result


def derivative_exponential(a: float, x: float) -> float:
    """2. Derivative of exponential function: d/dx(a^x) = a^x * ln(a)"""
    return (a ** x) * math.log(a)


def derivative_natural_exp(x: float) -> float:
    """3. Derivative of natural exponential: d/dx(e^x) = e^x"""
    return math.exp(x)


def derivative_logarithm(x: float, base: float = math.e) -> float:
    """4. Derivative of logarithm: d/dx(log_b(x)) = 1/(x*ln(b))"""
    if x <= 0:
        raise ValueError("Logarithm derivative undefined for x <= 0")
    return 1 / (x * math.log(base))


def derivative_natural_log(x: float) -> float:
    """5. Derivative of natural logarithm: d/dx(ln(x)) = 1/x"""
    if x <= 0:
        raise ValueError("Natural log derivative undefined for x <= 0")
    return 1 / x


def derivative_sine(x: float) -> float:
    """6. Derivative of sine: d/dx(sin(x)) = cos(x)"""
    return math.cos(x)


def derivative_cosine(x: float) -> float:
    """7. Derivative of cosine: d/dx(cos(x)) = -sin(x)"""
    return -math.sin(x)


def derivative_tangent(x: float) -> float:
    """8. Derivative of tangent: d/dx(tan(x)) = sec²(x) = 1/cos²(x)"""
    cos_x = math.cos(x)
    if abs(cos_x) < 1e-10:
        raise ValueError("Tangent derivative undefined at x = π/2 + nπ")
    return 1 / (cos_x ** 2)


def derivative_cotangent(x: float) -> float:
    """9. Derivative of cotangent: d/dx(cot(x)) = -csc²(x) = -1/sin²(x)"""
    sin_x = math.sin(x)
    if abs(sin_x) < 1e-10:
        raise ValueError("Cotangent derivative undefined at x = nπ")
    return -1 / (sin_x ** 2)


def derivative_secant(x: float) -> float:
    """10. Derivative of secant: d/dx(sec(x)) = sec(x)*tan(x)"""
    cos_x = math.cos(x)
    if abs(cos_x) < 1e-10:
        raise ValueError("Secant derivative undefined at x = π/2 + nπ")
    return (1 / cos_x) * math.tan(x)


def derivative_cosecant(x: float) -> float:
    """11. Derivative of cosecant: d/dx(csc(x)) = -csc(x)*cot(x)"""
    sin_x = math.sin(x)
    if abs(sin_x) < 1e-10:
        raise ValueError("Cosecant derivative undefined at x = nπ")
    return -(1 / sin_x) * (math.cos(x) / sin_x)


def derivative_arcsin(x: float) -> float:
    """12. Derivative of arcsine: d/dx(arcsin(x)) = 1/√(1-x²)"""
    if abs(x) >= 1:
        raise ValueError("Arcsine derivative undefined for |x| >= 1")
    return 1 / math.sqrt(1 - x ** 2)


def derivative_arccos(x: float) -> float:
    """13. Derivative of arccosine: d/dx(arccos(x)) = -1/√(1-x²)"""
    if abs(x) >= 1:
        raise ValueError("Arccosine derivative undefined for |x| >= 1")
    return -1 / math.sqrt(1 - x ** 2)


def derivative_arctan(x: float) -> float:
    """14. Derivative of arctangent: d/dx(arctan(x)) = 1/(1+x²)"""
    return 1 / (1 + x ** 2)


def derivative_sinh(x: float) -> float:
    """15. Derivative of hyperbolic sine: d/dx(sinh(x)) = cosh(x)"""
    return math.cosh(x)


def derivative_cosh(x: float) -> float:
    """16. Derivative of hyperbolic cosine: d/dx(cosh(x)) = sinh(x)"""
    return math.sinh(x)


def derivative_tanh(x: float) -> float:
    """17. Derivative of hyperbolic tangent: d/dx(tanh(x)) = sech²(x) = 1/cosh²(x)"""
    cosh_x = math.cosh(x)
    return 1 / (cosh_x ** 2)


def derivative_power(x: float, n: float) -> float:
    """18. Derivative of power function: d/dx(x^n) = n*x^(n-1)"""
    if x == 0 and n < 1:
        raise ValueError("Power derivative undefined for x=0 when n<1")
    return n * (x ** (n - 1))


def derivative_sqrt(x: float) -> float:
    """19. Derivative of square root: d/dx(√x) = 1/(2√x)"""
    if x <= 0:
        raise ValueError("Square root derivative undefined for x <= 0")
    return 1 / (2 * math.sqrt(x))


def derivative_reciprocal(x: float) -> float:
    """20. Derivative of reciprocal: d/dx(1/x) = -1/x²"""
    if x == 0:
        raise ValueError("Reciprocal derivative undefined at x=0")
    return -1 / (x ** 2)


def derivative_abs(x: float) -> float:
    """21. Derivative of absolute value: d/dx(|x|) = x/|x| = sgn(x)"""
    if x == 0:
        raise ValueError("Absolute value derivative undefined at x=0")
    return 1 if x > 0 else -1


def derivative_gaussian(x: float, mu: float = 0, sigma: float = 1) -> float:
    """22. Derivative of Gaussian/Normal distribution"""
    return -(x - mu) / (sigma ** 2) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))


def derivative_sigmoid(x: float) -> float:
    """23. Derivative of sigmoid: d/dx(1/(1+e^(-x))) = sigmoid(x)*(1-sigmoid(x))"""
    sig = 1 / (1 + math.exp(-x))
    return sig * (1 - sig)


# ============================================================================
# SECTION 2: ANTIDERIVATIVES/INTEGRALS (Operations 24-46)
# ============================================================================

def antiderivative_constant(c: float, x: float) -> float:
    """24. Antiderivative of constant: ∫c dx = cx"""
    return c * x


def antiderivative_power(x: float, n: float) -> float:
    """25. Antiderivative of power: ∫x^n dx = x^(n+1)/(n+1) + C"""
    if n == -1:
        raise ValueError("Use antiderivative_reciprocal for n=-1")
    return (x ** (n + 1)) / (n + 1)


def antiderivative_reciprocal(x: float) -> float:
    """26. Antiderivative of reciprocal: ∫1/x dx = ln|x| + C"""
    if x == 0:
        raise ValueError("Antiderivative of 1/x undefined at x=0")
    return math.log(abs(x))


def antiderivative_exponential(x: float) -> float:
    """27. Antiderivative of exponential: ∫e^x dx = e^x + C"""
    return math.exp(x)


def antiderivative_sine(x: float) -> float:
    """28. Antiderivative of sine: ∫sin(x) dx = -cos(x) + C"""
    return -math.cos(x)


def antiderivative_cosine(x: float) -> float:
    """29. Antiderivative of cosine: ∫cos(x) dx = sin(x) + C"""
    return math.sin(x)


def antiderivative_secant_squared(x: float) -> float:
    """30. Antiderivative of sec²(x): ∫sec²(x) dx = tan(x) + C"""
    return math.tan(x)


def antiderivative_cosecant_squared(x: float) -> float:
    """31. Antiderivative of csc²(x): ∫csc²(x) dx = -cot(x) + C"""
    sin_x = math.sin(x)
    if abs(sin_x) < 1e-10:
        raise ValueError("Cotangent undefined at x = nπ")
    return -math.cos(x) / sin_x


def antiderivative_secant_tangent(x: float) -> float:
    """32. Antiderivative of sec(x)tan(x): ∫sec(x)tan(x) dx = sec(x) + C"""
    cos_x = math.cos(x)
    if abs(cos_x) < 1e-10:
        raise ValueError("Secant undefined at x = π/2 + nπ")
    return 1 / cos_x


def antiderivative_cosecant_cotangent(x: float) -> float:
    """33. Antiderivative of csc(x)cot(x): ∫csc(x)cot(x) dx = -csc(x) + C"""
    sin_x = math.sin(x)
    if abs(sin_x) < 1e-10:
        raise ValueError("Cosecant undefined at x = nπ")
    return -1 / sin_x


def antiderivative_sqrt_complement(x: float) -> float:
    """34. Antiderivative pattern: ∫1/√(1-x²) dx = arcsin(x) + C"""
    if abs(x) >= 1:
        raise ValueError("Arcsin undefined for |x| >= 1")
    return math.asin(x)


def antiderivative_arctan_pattern(x: float) -> float:
    """35. Antiderivative pattern: ∫1/(1+x²) dx = arctan(x) + C"""
    return math.atan(x)


def antiderivative_sinh(x: float) -> float:
    """36. Antiderivative of sinh: ∫sinh(x) dx = cosh(x) + C"""
    return math.cosh(x)


def antiderivative_cosh(x: float) -> float:
    """37. Antiderivative of cosh: ∫cosh(x) dx = sinh(x) + C"""
    return math.sinh(x)


def antiderivative_sech_squared(x: float) -> float:
    """38. Antiderivative of sech²(x): ∫sech²(x) dx = tanh(x) + C"""
    return math.tanh(x)


def antiderivative_polynomial(coefficients: List[float], x: float) -> float:
    """39. Antiderivative of polynomial"""
    n = len(coefficients)
    result = sum(coefficients[i] * (x ** (i + 1)) / (i + 1) for i in range(n))
    return result


def antiderivative_rational_arctan(x: float, a: float = 1) -> float:
    """40. ∫1/(a²+x²) dx = (1/a)arctan(x/a) + C"""
    return (1 / a) * math.atan(x / a)


def antiderivative_exp_scaled(x: float, k: float = 1) -> float:
    """41. ∫e^(kx) dx = (1/k)e^(kx) + C"""
    if k == 0:
        return x
    return (1 / k) * math.exp(k * x)


def antiderivative_sin_scaled(x: float, k: float = 1) -> float:
    """42. ∫sin(kx) dx = -(1/k)cos(kx) + C"""
    if k == 0:
        return 0
    return -(1 / k) * math.cos(k * x)


def antiderivative_cos_scaled(x: float, k: float = 1) -> float:
    """43. ∫cos(kx) dx = (1/k)sin(kx) + C"""
    if k == 0:
        return 0
    return (1 / k) * math.sin(k * x)


def antiderivative_sqrt_x(x: float) -> float:
    """44. ∫√x dx = (2/3)x^(3/2) + C"""
    if x < 0:
        raise ValueError("Square root undefined for x < 0")
    return (2 / 3) * (x ** 1.5)


def antiderivative_reciprocal_sqrt(x: float) -> float:
    """45. ∫1/√x dx = 2√x + C"""
    if x <= 0:
        raise ValueError("1/√x undefined for x <= 0")
    return 2 * math.sqrt(x)


def antiderivative_ln(x: float) -> float:
    """46. ∫ln(x) dx = x*ln(x) - x + C (integration by parts)"""
    if x <= 0:
        raise ValueError("ln(x) undefined for x <= 0")
    return x * math.log(x) - x


# ============================================================================
# SECTION 3: INVERSE OPERATIONS (Operations 47-69)
# ============================================================================

def inverse_linear(y: float, a: float, b: float) -> float:
    """47. Inverse of linear function y = ax + b"""
    if a == 0:
        raise ValueError("Linear function not invertible when a=0")
    return (y - b) / a


def inverse_quadratic_positive(y: float, a: float = 1, b: float = 0, c: float = 0) -> float:
    """48. Inverse of quadratic (positive branch): y = ax² + bx + c"""
    if a == 0:
        raise ValueError("Not a quadratic function")
    # Using quadratic formula for positive root
    discriminant = b ** 2 - 4 * a * (c - y)
    if discriminant < 0:
        raise ValueError("No real inverse for this y value")
    return (-b + math.sqrt(discriminant)) / (2 * a)


def inverse_quadratic_negative(y: float, a: float = 1, b: float = 0, c: float = 0) -> float:
    """49. Inverse of quadratic (negative branch)"""
    if a == 0:
        raise ValueError("Not a quadratic function")
    discriminant = b ** 2 - 4 * a * (c - y)
    if discriminant < 0:
        raise ValueError("No real inverse for this y value")
    return (-b - math.sqrt(discriminant)) / (2 * a)


def inverse_exponential(y: float, base: float = math.e) -> float:
    """50. Inverse of exponential: if y = b^x, then x = log_b(y)"""
    if y <= 0:
        raise ValueError("Exponential inverse undefined for y <= 0")
    if base <= 0 or base == 1:
        raise ValueError("Invalid base for exponential")
    return math.log(y) / math.log(base)


def inverse_logarithm(y: float, base: float = math.e) -> float:
    """51. Inverse of logarithm: if y = log_b(x), then x = b^y"""
    if base <= 0 or base == 1:
        raise ValueError("Invalid base for logarithm")
    return base ** y


def inverse_sine(y: float) -> float:
    """52. Inverse sine (arcsin)"""
    if abs(y) > 1:
        raise ValueError("Arcsin domain is [-1, 1]")
    return math.asin(y)


def inverse_cosine(y: float) -> float:
    """53. Inverse cosine (arccos)"""
    if abs(y) > 1:
        raise ValueError("Arccos domain is [-1, 1]")
    return math.acos(y)


def inverse_tangent(y: float) -> float:
    """54. Inverse tangent (arctan)"""
    return math.atan(y)


def inverse_cotangent(y: float) -> float:
    """55. Inverse cotangent (arccot)"""
    return math.pi / 2 - math.atan(y)


def inverse_secant(y: float) -> float:
    """56. Inverse secant (arcsec)"""
    if abs(y) < 1:
        raise ValueError("Arcsec domain is (-∞,-1] ∪ [1,∞)")
    return math.acos(1 / y)


def inverse_cosecant(y: float) -> float:
    """57. Inverse cosecant (arccsc)"""
    if abs(y) < 1:
        raise ValueError("Arccsc domain is (-∞,-1] ∪ [1,∞)")
    return math.asin(1 / y)


def inverse_sinh(y: float) -> float:
    """58. Inverse hyperbolic sine (arcsinh)"""
    return math.asinh(y)


def inverse_cosh(y: float) -> float:
    """59. Inverse hyperbolic cosine (arccosh)"""
    if y < 1:
        raise ValueError("Arccosh domain is [1, ∞)")
    return math.acosh(y)


def inverse_tanh(y: float) -> float:
    """60. Inverse hyperbolic tangent (arctanh)"""
    if abs(y) >= 1:
        raise ValueError("Arctanh domain is (-1, 1)")
    return math.atanh(y)


def inverse_power(y: float, n: float) -> float:
    """61. Inverse of power function: if y = x^n, then x = y^(1/n)"""
    if n == 0:
        raise ValueError("Cannot invert x^0")
    if y < 0 and (1 / n) != int(1 / n):
        raise ValueError("Even root of negative number")
    return y ** (1 / n)


def inverse_sqrt(y: float) -> float:
    """62. Inverse of square root: if y = √x, then x = y²"""
    return y ** 2


def inverse_cube_root(y: float) -> float:
    """63. Inverse of cube root: if y = ³√x, then x = y³"""
    return y ** 3


def inverse_reciprocal(y: float) -> float:
    """64. Inverse of reciprocal: if y = 1/x, then x = 1/y"""
    if y == 0:
        raise ValueError("Cannot invert reciprocal at y=0")
    return 1 / y


def inverse_sigmoid(y: float) -> float:
    """65. Inverse of sigmoid (logit function)"""
    if y <= 0 or y >= 1:
        raise ValueError("Sigmoid inverse domain is (0, 1)")
    return math.log(y / (1 - y))


def inverse_softplus(y: float) -> float:
    """66. Inverse of softplus: if y = ln(1 + e^x), then x = ln(e^y - 1)"""
    if y <= 0:
        raise ValueError("Softplus inverse undefined for y <= 0")
    return math.log(math.exp(y) - 1)


def inverse_abs_positive(y: float) -> float:
    """67. Inverse of absolute value (positive branch)"""
    if y < 0:
        raise ValueError("Absolute value output is non-negative")
    return y


def inverse_abs_negative(y: float) -> float:
    """68. Inverse of absolute value (negative branch)"""
    if y < 0:
        raise ValueError("Absolute value output is non-negative")
    return -y


def inverse_polynomial_newton(y: float, coefficients: List[float], 
                               initial_guess: float = 0, 
                               max_iterations: int = 100,
                               tolerance: float = 1e-10) -> float:
    """69. Inverse of polynomial using Newton-Raphson method"""
    x = initial_guess
    for _ in range(max_iterations):
        # Evaluate polynomial and its derivative
        p = sum(c * (x ** i) for i, c in enumerate(coefficients))
        dp = sum(i * c * (x ** (i - 1)) for i, c in enumerate(coefficients) if i > 0)
        
        if abs(dp) < 1e-15:
            raise ValueError("Derivative too small, Newton-Raphson failed")
        
        x_new = x - (p - y) / dp
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    
    raise ValueError("Newton-Raphson did not converge")


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_all_operations() -> dict:
    """Returns a dictionary of all 69 mathematical operations"""
    operations = {
        # Derivatives (1-23)
        1: ("derivative_polynomial", derivative_polynomial),
        2: ("derivative_exponential", derivative_exponential),
        3: ("derivative_natural_exp", derivative_natural_exp),
        4: ("derivative_logarithm", derivative_logarithm),
        5: ("derivative_natural_log", derivative_natural_log),
        6: ("derivative_sine", derivative_sine),
        7: ("derivative_cosine", derivative_cosine),
        8: ("derivative_tangent", derivative_tangent),
        9: ("derivative_cotangent", derivative_cotangent),
        10: ("derivative_secant", derivative_secant),
        11: ("derivative_cosecant", derivative_cosecant),
        12: ("derivative_arcsin", derivative_arcsin),
        13: ("derivative_arccos", derivative_arccos),
        14: ("derivative_arctan", derivative_arctan),
        15: ("derivative_sinh", derivative_sinh),
        16: ("derivative_cosh", derivative_cosh),
        17: ("derivative_tanh", derivative_tanh),
        18: ("derivative_power", derivative_power),
        19: ("derivative_sqrt", derivative_sqrt),
        20: ("derivative_reciprocal", derivative_reciprocal),
        21: ("derivative_abs", derivative_abs),
        22: ("derivative_gaussian", derivative_gaussian),
        23: ("derivative_sigmoid", derivative_sigmoid),
        
        # Antiderivatives (24-46)
        24: ("antiderivative_constant", antiderivative_constant),
        25: ("antiderivative_power", antiderivative_power),
        26: ("antiderivative_reciprocal", antiderivative_reciprocal),
        27: ("antiderivative_exponential", antiderivative_exponential),
        28: ("antiderivative_sine", antiderivative_sine),
        29: ("antiderivative_cosine", antiderivative_cosine),
        30: ("antiderivative_secant_squared", antiderivative_secant_squared),
        31: ("antiderivative_cosecant_squared", antiderivative_cosecant_squared),
        32: ("antiderivative_secant_tangent", antiderivative_secant_tangent),
        33: ("antiderivative_cosecant_cotangent", antiderivative_cosecant_cotangent),
        34: ("antiderivative_sqrt_complement", antiderivative_sqrt_complement),
        35: ("antiderivative_arctan_pattern", antiderivative_arctan_pattern),
        36: ("antiderivative_sinh", antiderivative_sinh),
        37: ("antiderivative_cosh", antiderivative_cosh),
        38: ("antiderivative_sech_squared", antiderivative_sech_squared),
        39: ("antiderivative_polynomial", antiderivative_polynomial),
        40: ("antiderivative_rational_arctan", antiderivative_rational_arctan),
        41: ("antiderivative_exp_scaled", antiderivative_exp_scaled),
        42: ("antiderivative_sin_scaled", antiderivative_sin_scaled),
        43: ("antiderivative_cos_scaled", antiderivative_cos_scaled),
        44: ("antiderivative_sqrt_x", antiderivative_sqrt_x),
        45: ("antiderivative_reciprocal_sqrt", antiderivative_reciprocal_sqrt),
        46: ("antiderivative_ln", antiderivative_ln),
        
        # Inverses (47-69)
        47: ("inverse_linear", inverse_linear),
        48: ("inverse_quadratic_positive", inverse_quadratic_positive),
        49: ("inverse_quadratic_negative", inverse_quadratic_negative),
        50: ("inverse_exponential", inverse_exponential),
        51: ("inverse_logarithm", inverse_logarithm),
        52: ("inverse_sine", inverse_sine),
        53: ("inverse_cosine", inverse_cosine),
        54: ("inverse_tangent", inverse_tangent),
        55: ("inverse_cotangent", inverse_cotangent),
        56: ("inverse_secant", inverse_secant),
        57: ("inverse_cosecant", inverse_cosecant),
        58: ("inverse_sinh", inverse_sinh),
        59: ("inverse_cosh", inverse_cosh),
        60: ("inverse_tanh", inverse_tanh),
        61: ("inverse_power", inverse_power),
        62: ("inverse_sqrt", inverse_sqrt),
        63: ("inverse_cube_root", inverse_cube_root),
        64: ("inverse_reciprocal", inverse_reciprocal),
        65: ("inverse_sigmoid", inverse_sigmoid),
        66: ("inverse_softplus", inverse_softplus),
        67: ("inverse_abs_positive", inverse_abs_positive),
        68: ("inverse_abs_negative", inverse_abs_negative),
        69: ("inverse_polynomial_newton", inverse_polynomial_newton),
    }
    return operations


def list_operations() -> None:
    """Prints a list of all 69 operations"""
    ops = get_all_operations()
    print("=" * 80)
    print("RAFAELIA Mathematical Operations Library - 69 Functions")
    print("=" * 80)
    print("\nDIRECT DERIVATIVES (1-23):")
    for i in range(1, 24):
        print(f"  {i:2d}. {ops[i][0]}")
    print("\nANTIDERIVATIVES/INTEGRALS (24-46):")
    for i in range(24, 47):
        print(f"  {i:2d}. {ops[i][0]}")
    print("\nINVERSE OPERATIONS (47-69):")
    for i in range(47, 70):
        print(f"  {i:2d}. {ops[i][0]}")
    print("=" * 80)


if __name__ == "__main__":
    # Demonstration
    list_operations()
    
    # Example usage
    print("\n\nExample Usage:")
    print("-" * 80)
    print(f"1. Derivative of x² at x=3: {derivative_power(3, 2)}")
    print(f"2. Antiderivative of x² at x=3: {antiderivative_power(3, 2)}")
    print(f"3. Inverse of y=2x+1 when y=7: {inverse_linear(7, 2, 1)}")
    print(f"4. Derivative of sin(π/4): {derivative_sine(math.pi/4)}")
    print(f"5. Inverse of e^x when y=10: {inverse_exponential(10)}")
