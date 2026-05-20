# 5.6.3 Parametric Uncertainties: The Kharitonov Polynomials

As was pointed out in Chapter 2, Section 2.7, some of the uncertainty is parametric, i.e., is expressed in terms of a set of parameters. All examples in Chapter 2 contained physical parameters, so the plant models were, in fact, functions of those parameters.

A relatively new tool for the study of systems with parametric uncertainties is Kharitonov's theorem [8]. Kharitonov's work has sparked a new line of inquiry in this general area (see, for example, Barmish [9]). The theorem addresses the stability of a polynomial

$$p (s, \mathbf {a}) = a _ {0} + a _ {1} s + \dots + a _ {m} s ^ {n}$$

whose coefficients can vary over given ranges, or

$$a _ {i} ^ {-} \leq a _ {i} \leq a _ {i} ^ {+}.$$

This is known as an interval polynomial family. It is of invariant degree if $a_{n}$ always nonzero.

We define the form Kharitonov polynomials:

$$k _ {1} (s) = a _ {0} ^ {-} + a _ {1} ^ {-} s + a _ {2} ^ {+} s ^ {2} + a _ {3} ^ {+} s ^ {3} + a _ {4} ^ {-} s ^ {4} + a _ {5} ^ {-} s ^ {5} + a _ {6} ^ {+} s ^ {6} + \dotsk _ {2} (s) = a _ {0} ^ {+} + a _ {1} ^ {+} s + a _ {2} ^ {-} s ^ {2} + a _ {3} ^ {-} s ^ {3} + a _ {4} ^ {+} s ^ {4} + a _ {5} ^ {+} s ^ {5} + a _ {6} ^ {-} s ^ {6} + \dotsk _ {3} (s) = a _ {0} ^ {+} + a _ {1} ^ {-} s + a _ {2} ^ {-} s ^ {2} + a _ {3} ^ {+} s ^ {3} + a _ {4} ^ {+} s ^ {4} + a _ {5} ^ {-} s ^ {5} + a _ {6} ^ {-} s ^ {6} + \dotsk _ {4} (s) = a _ {0} ^ {-} + a _ {1} ^ {+} s + a _ {2} ^ {+} s + a _ {3} ^ {-} s ^ {3} + a _ {4} ^ {-} s ^ {4} + a _ {5} ^ {+} s ^ {5} + a _ {6} ^ {+} s ^ {6} + \dots \tag {5.24}$$

Now we can state the theorem.

■ Theorem 5.1 Kharitonov's Theorem An interval polynomial family P with invariant degree is robustly stable if, and only if, its four Kharitonov polynomials are stable. ■

The reader is referred to Barmish for a proof. The proof is not difficult but is too long to be included here.

Example 5.17 Assess the robust stability of the third-order interval polynomial family with $1 \leq a_0 \leq 2$ , $0.5 \leq a_1 \leq 1$ , $2 \leq a_2 \leq 3$ , and $a_3 = 1$ .

Solution The Kharitonov polynomials are

$$k _ {1} (s) = 1 +. 5 s + 3 s ^ {2} + s ^ {3}k _ {2} (s) = 2 + s + 2 s ^ {2} + s ^ {3}k _ {3} (s) = 2 +. 5 s + 2 s ^ {2} + s ^ {3}k _ {4} (s) = 1 + s + 3 s ^ {2} + s ^ {3}$$

By the Routh criterion, $k_{2}$ and $k_{4}$ are unstable, so the family is not robustly stable. In fact, $k_{2}$ and $k_{4}$ are two unstable members of $\mathcal{P}$ .

In general, the coefficients of the characteristic polynomial are not the model parameters, but functions of those parameters. We may apply Kharitonov's theorem in such cases, but the result is only sufficient. The Kharitonov test may be used, but with the caveat that the results may be conservative.
