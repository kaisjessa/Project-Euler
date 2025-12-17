`math` — Mathematical functions[¶](#module-math "Link to this heading")
=======================================================================

* * *

This module provides access to common mathematical functions and constants, including those defined by the C standard.

These functions cannot be used with complex numbers; use the functions of the same name from the [`cmath`](cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.") module if you require support for complex numbers. The distinction between functions which support complex numbers and those which don’t is made since most users do not want to learn quite as much mathematics as required to understand complex numbers. Receiving an exception instead of a complex result allows earlier detection of the unexpected complex number used as a parameter, so that the programmer can determine how and why it was generated in the first place.

The following functions are provided by this module. Except when explicitly noted otherwise, all return values are floats.

**Number-theoretic functions**

[`comb(n, k)`](#math.comb "math.comb")

Number of ways to choose _k_ items from _n_ items without repetition and without order

[`factorial(n)`](#math.factorial "math.factorial")

_n_ factorial

[`gcd(*integers)`](#math.gcd "math.gcd")

Greatest common divisor of the integer arguments

[`isqrt(n)`](#math.isqrt "math.isqrt")

Integer square root of a nonnegative integer _n_

[`lcm(*integers)`](#math.lcm "math.lcm")

Least common multiple of the integer arguments

[`perm(n, k)`](#math.perm "math.perm")

Number of ways to choose _k_ items from _n_ items without repetition and with order

**Floating point arithmetic**

[`ceil(x)`](#math.ceil "math.ceil")

Ceiling of _x_, the smallest integer greater than or equal to _x_

[`fabs(x)`](#math.fabs "math.fabs")

Absolute value of _x_

[`floor(x)`](#math.floor "math.floor")

Floor of _x_, the largest integer less than or equal to _x_

[`fma(x, y, z)`](#math.fma "math.fma")

Fused multiply-add operation: `(x * y) + z`

[`fmod(x, y)`](#math.fmod "math.fmod")

Remainder of division `x / y`

[`modf(x)`](#math.modf "math.modf")

Fractional and integer parts of _x_

[`remainder(x, y)`](#math.remainder "math.remainder")

Remainder of _x_ with respect to _y_

[`trunc(x)`](#math.trunc "math.trunc")

Integer part of _x_

**Floating point manipulation functions**

[`copysign(x, y)`](#math.copysign "math.copysign")

Magnitude (absolute value) of _x_ with the sign of _y_

[`frexp(x)`](#math.frexp "math.frexp")

Mantissa and exponent of _x_

[`isclose(a, b, rel_tol, abs_tol)`](#math.isclose "math.isclose")

Check if the values _a_ and _b_ are close to each other

[`isfinite(x)`](#math.isfinite "math.isfinite")

Check if _x_ is neither an infinity nor a NaN

[`isinf(x)`](#math.isinf "math.isinf")

Check if _x_ is a positive or negative infinity

[`isnan(x)`](#math.isnan "math.isnan")

Check if _x_ is a NaN (not a number)

[`ldexp(x, i)`](#math.ldexp "math.ldexp")

`x * (2**i)`, inverse of function [`frexp()`](#math.frexp "math.frexp")

[`nextafter(x, y, steps)`](#math.nextafter "math.nextafter")

Floating-point value _steps_ steps after _x_ towards _y_

[`ulp(x)`](#math.ulp "math.ulp")

Value of the least significant bit of _x_

**Power, exponential and logarithmic functions**

[`cbrt(x)`](#math.cbrt "math.cbrt")

Cube root of _x_

[`exp(x)`](#math.exp "math.exp")

_e_ raised to the power _x_

[`exp2(x)`](#math.exp2 "math.exp2")

_2_ raised to the power _x_

[`expm1(x)`](#math.expm1 "math.expm1")

_e_ raised to the power _x_, minus 1

[`log(x, base)`](#math.log "math.log")

Logarithm of _x_ to the given base (_e_ by default)

[`log1p(x)`](#math.log1p "math.log1p")

Natural logarithm of _1+x_ (base _e_)

[`log2(x)`](#math.log2 "math.log2")

Base-2 logarithm of _x_

[`log10(x)`](#math.log10 "math.log10")

Base-10 logarithm of _x_

[`pow(x, y)`](#math.pow "math.pow")

_x_ raised to the power _y_

[`sqrt(x)`](#math.sqrt "math.sqrt")

Square root of _x_

**Summation and product functions**

[`dist(p, q)`](#math.dist "math.dist")

Euclidean distance between two points _p_ and _q_ given as an iterable of coordinates

[`fsum(iterable)`](#math.fsum "math.fsum")

Sum of values in the input _iterable_

[`hypot(*coordinates)`](#math.hypot "math.hypot")

Euclidean norm of an iterable of coordinates

[`prod(iterable, start)`](#math.prod "math.prod")

Product of elements in the input _iterable_ with a _start_ value

[`sumprod(p, q)`](#math.sumprod "math.sumprod")

Sum of products from two iterables _p_ and _q_

**Angular conversion**

[`degrees(x)`](#math.degrees "math.degrees")

Convert angle _x_ from radians to degrees

[`radians(x)`](#math.radians "math.radians")

Convert angle _x_ from degrees to radians

**Trigonometric functions**

[`acos(x)`](#math.acos "math.acos")

Arc cosine of _x_

[`asin(x)`](#math.asin "math.asin")

Arc sine of _x_

[`atan(x)`](#math.atan "math.atan")

Arc tangent of _x_

[`atan2(y, x)`](#math.atan2 "math.atan2")

`atan(y / x)`

[`cos(x)`](#math.cos "math.cos")

Cosine of _x_

[`sin(x)`](#math.sin "math.sin")

Sine of _x_

[`tan(x)`](#math.tan "math.tan")

Tangent of _x_

**Hyperbolic functions**

[`acosh(x)`](#math.acosh "math.acosh")

Inverse hyperbolic cosine of _x_

[`asinh(x)`](#math.asinh "math.asinh")

Inverse hyperbolic sine of _x_

[`atanh(x)`](#math.atanh "math.atanh")

Inverse hyperbolic tangent of _x_

[`cosh(x)`](#math.cosh "math.cosh")

Hyperbolic cosine of _x_

[`sinh(x)`](#math.sinh "math.sinh")

Hyperbolic sine of _x_

[`tanh(x)`](#math.tanh "math.tanh")

Hyperbolic tangent of _x_

**Special functions**

[`erf(x)`](#math.erf "math.erf")

[Error function](https://en.wikipedia.org/wiki/Error_function) at _x_

[`erfc(x)`](#math.erfc "math.erfc")

[Complementary error function](https://en.wikipedia.org/wiki/Error_function) at _x_

[`gamma(x)`](#math.gamma "math.gamma")

[Gamma function](https://en.wikipedia.org/wiki/Gamma_function) at _x_

[`lgamma(x)`](#math.lgamma "math.lgamma")

Natural logarithm of the absolute value of the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function) at _x_

**Constants**

[`pi`](#math.pi "math.pi")

_π_ = 3.141592…

[`e`](#math.e "math.e")

_e_ = 2.718281…

[`tau`](#math.tau "math.tau")

_τ_ = 2_π_ = 6.283185…

[`inf`](#math.inf "math.inf")

Positive infinity

[`nan`](#math.nan "math.nan")

“Not a number” (NaN)