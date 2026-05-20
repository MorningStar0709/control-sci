# 4.5 AN INTRODUCTION TO $H^{\infty}$ THEORY

As a followup to the preceding section, we present an introduction to $H^{\infty}$ theory. This theory originated in the work of Zames only a few years ago, and is having a significant impact on the development of control methodology. We shall use the theory to derive for a given plant the best (in some sense) $S(s)$ that satisfies the interpolation conditions. The result, which does not take into account the need to roll off $T(s)$ or to have a proper or strictly proper $F(s)$ , is not so much a design as a yardstick against which to evaluate a design. If a control system sensitivity were close to optimal in this sense at frequencies within the desired bandwidth, the design would have little room for improvement.

At its most basic level, $H^{\infty}$ theory addresses the following problem: given a stable, proper, rational weighting function $W(s)$ with all zeros in the open LHP, find the proper, stable sensitivity function $S(s)$ that (i) satisfies given interpolation constraints at some RHP points and (ii) minimizes

$$\mu = \sup _ {\omega} | S (j \omega) W (j \omega) |. \tag {4.55}$$

The interpolation constraints are precisely the ones discussed earlier. The optimization problem is of the “mini-max” or worst-case variety: we seek to minimize the supremum, over the whole frequency range, of the weighted sensitivity. The weighting function reflects the fact that low sensitivity is more important at some frequencies (normally low frequencies) than at other frequencies. Since it is the magnitude of the product that is minimized, the sensitivity tends to be small at frequencies where the weight is relatively great.

The solution, derived from functional analysis, is of the form

$$S (s) W (s) = k B (s) \tag {4.56}$$

where $k$ is a constant and $B(s)$ is a Blaschke product.

The Blaschke product $B(s)$ in Equation 4.56 will be chosen to satisfy interpolation constraints, if any. We saw that there are no interpolation constraints on $S(s)$ if the plant $P(s)$ is stable and minimum-phase; in that case, $B(s) = 1$ and $k$ may be any real number, as small as desired. If $P(s)$ has poles $p_1, p_2, \ldots, p_N$ in the closed RHP, then $S(p_i) = 0, i = 1, 2, \ldots, N$ . If $P(s)$ has zeros $z_1, z_2, \ldots, z_M$ in the closed RHP, then $S(z_i) = 1, i = 1, 2, \ldots, M$ .
