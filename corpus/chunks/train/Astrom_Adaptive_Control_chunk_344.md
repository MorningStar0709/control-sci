# The Error Model

Having obtained a suitable controller structure, we now proceed to derive an error model. It follows from Eq. (5.67) that

$$A _ {o} A _ {m} y = A R _ {1} y + b _ {0} S y = R _ {1} b _ {0} B u + b _ {0} S y \tag {5.69}$$

where the first equality follows from Eq. (5.67) and the second from Eq. (5.64). Introduce the error

$$e = y - y _ {m}$$

It follows from Eqs. (5.69) and (5.68) that

$$A _ {o} A _ {m} e = A _ {o} A _ {m} (y - y _ {m}) = b _ {0} (R u + S y - T u _ {c})$$

OT

$$e = \frac {b _ {0}}{A _ {o} A _ {m}} (R u + S y - T u _ {c})$$

This expression is not yet a suitable error model, because the transfer function $b_{0}/(A_{o}A_{m})$ is not SPR. Therefore introduce the filtered error

$$e _ {f} = \frac {Q}{P} e = \frac {Q}{P} (y - y _ {m})$$

where Q is a polynomial whose degree is not greater than $\deg A_{o}A_{m}$ such that

$$\frac {b _ {0} Q}{A _ {o} A _ {m}} \tag {5.70}$$

is SPR. The filtered error can be written as

$$e _ {f} = \frac {b _ {0} Q}{A _ {n} A _ {m}} \left(\frac {R}{P} u + \frac {S}{P} y - \frac {T}{P} u _ {c}\right)$$

Let $P = P_{1}P_{2}$ , where $P_{2}$ is a stable monic polynomial of the same degree as R. Rewrite R/P as

$$\frac {R}{P} = \frac {R - P _ {2} + P _ {2}}{P _ {1} P _ {2}} = \frac {1}{P _ {1}} + \frac {R - P _ {2}}{P}$$

The filtered error then becomes

$$e _ {f} = \frac {b _ {0} Q}{A _ {o} A _ {m}} \left(\frac {1}{P _ {1}} u + \frac {R - P _ {2}}{P} u + \frac {S}{P} y - \frac {T}{P} u _ {c}\right)$$

Let k, l, and m be the degrees of the polynomials R, S, and T, respectively. Introduce a vector of true controller parameters

$$\theta^ {0} = \left(r _ {1} ^ {\prime} \dots r _ {k} ^ {\prime} s _ {0} \dots s _ {l} t _ {0} \dots t _ {m}\right) ^ {T} \tag {5.71}$$

where $r_{i}^{\prime}$ are the coefficients of the polynomial $R - P_{2}$ . Also introduce a vector of filtered input, output, and command signals

$$\varphi^ {T} = \left(\frac {p ^ {k - 1}}{P (p)} u \dots \frac {1}{P (p)} u \quad \frac {p ^ {\ell}}{P (p)} y \dots \frac {1}{P (p)} y \quad - \frac {p ^ {m}}{P (p)} u _ {c} \dots - \frac {1}{P (p)} u _ {c}\right) \tag {5.72}$$

The filtered error can then be written as

$$e _ {f} = \frac {b _ {0} Q}{A _ {o} A _ {m}} \left(\frac {1}{P _ {1}} u + \varphi^ {T} \theta^ {0}\right) \tag {5.73}$$

To obtain an error model, we must introduce a parameterization of the controller. In the nominal case in which the parameters are known, the control law can be expressed as
