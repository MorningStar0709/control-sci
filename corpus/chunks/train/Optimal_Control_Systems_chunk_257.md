# 5.1 Variational Calculus for Discrete-Time Systems

\- Step 5: Boundary Conditions

Now consider these items in detail.

\- Step 1: Variations: We first let $x(k)$ and $x(k + 1)$ take on variations $\delta x(k)$ and $\delta x(k + 1)$ from their optimal values $x^{*}(k)$ and $x^{*}(k + 1)$ , respectively, such that

$$x (k) = x ^ {*} (k) + \delta x (k); \quad x (k + 1) = x ^ {*} (k + 1) + \delta x (k + 1). \tag {5.1.2}$$

Now with these variations, the performance index (5.1.1) becomes

$$
\begin{array}{l} J ^ {*} = J (x ^ {*} (k _ {0}), k _ {0}) \\ = \sum_ {k = k _ {0}} ^ {k _ {f} - 1} V (x ^ {*} (k), x ^ {*} (k + 1), k) \tag {5.1.3} \\ \end{array}

\begin{array}{l} J = J (x (k _ {0}), k _ {0}) \\ = \sum_ {k = k _ {0}} ^ {k _ {f} - 1} V (x ^ {*} (k) + \delta x (k), x ^ {*} (k + 1) + \delta x (k + 1), k). \tag {5.1.4} \\ \end{array}
$$

\- Step 2: Increment: The increment of the functionals defined by (5.1.2) and (5.1.3) is defined as

$$\Delta J = J - J ^ {*}. \tag {5.1.5}$$

\- Step 3: First Variation: The first variation $\delta J$ is the first order approximation of the increment $\Delta J$ . Thus, using the Taylor series expansion of (5.1.4) along with (5.1.3), we have

$$
\begin{array}{l} \delta J = \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left[ \frac {\partial V (x ^ {*} (k) , x ^ {*} (k + 1) , k)}{\partial x ^ {*} (k)} \delta x (k) \right. \\ \left. + \frac {\partial V (x ^ {*} (k) , x ^ {*} (k + 1) , k)}{\partial x ^ {*} (k + 1)} \delta x (k + 1) \right]. \tag {5.1.6} \\ \end{array}
$$

Now in order to express the coefficient $\delta x(k+1)$ also in terms of $\delta x(k)$ , consider the second expression in (5.1.6).
