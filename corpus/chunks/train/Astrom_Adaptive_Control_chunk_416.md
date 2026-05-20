# EXAMPLE 6.6 Singularities for pole placement design

Consider the model of Eq. (6.34) with

$$A (q) = q ^ {2} + a _ {1} q + a _ {2}B (q) = b _ {0} q + b _ {1}$$

In Example 3.2 a controller was designed for

$$A _ {m} (q) = q ^ {2} + a _ {m 1} q + a _ {m 2}A _ {o} (q) = q + a _ {o}$$

In this case the controller and process parameters are

$$
\vartheta = \left( \begin{array}{l l l} r _ {1} & s _ {0} & s _ {1} \end{array} \right) \quad \theta = \left( \begin{array}{l l l l} a _ {1} & a _ {2} & b _ {0} & b _ {1} \end{array} \right)
$$

and the map $\chi : R^4 \to R^3$ is given by

$$
\begin{array}{l} r _ {1} = \frac {a _ {0} a _ {m 2} b _ {0} ^ {2} + (a _ {2} - a _ {m 2} - a _ {0} a _ {m 1}) b _ {0} b _ {1} + (a _ {0} + a _ {m 1} - a _ {1}) b _ {1} ^ {2}}{b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \\ s _ {0} = \frac {b _ {1} \left(a _ {o} a _ {m 1} - a _ {2} \cdot a _ {m 1} a _ {1} + a _ {1} ^ {2} + a _ {m 2} - a _ {1} a _ {o}\right)}{b _ {1} ^ {2} \cdot a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \\ + \frac {b _ {0} \left(a _ {m 1} a _ {2} - a _ {1} a _ {2} - a _ {0} a _ {m 2} + a _ {0} a _ {2}\right)}{b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \tag {6.36} \\ s _ {1} = \frac {b _ {1} \left(a _ {1} a _ {2} - a _ {m 1} a _ {2} + a _ {o} a _ {m 2} - a _ {o} a _ {2}\right)}{b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \\ + \frac {b _ {0} \left(a _ {2} a _ {m 2} - a _ {2} ^ {2} - a _ {0} a _ {m 2} a _ {1} + a _ {0} a _ {2} a _ {m 1}\right)}{b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \\ \end{array}
$$

The map $\chi$ is singular when the denominator in Eqs. (6.36) vanishes, that is, when

$$b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2} = 0$$

Singularities of the type in Example 6.6 will appear for practically all design methods. Since the singularities are algebraic surfaces, the parameter estimates must pass them if the algorithms are not initialized properly. There are several ways to avoid the difficulties. One possibility is to test for common factors and to cancel them if they appear, but such a procedure will require test quantities. It will also make $\chi$ discontinuous, which creates difficulties in the analysis. Another and better solution is to find design techniques such that the mapping $\chi$ is smooth. This is an open research problem, which so far has received little' attention.

The following example illustrates what happens if no precautions are taken with cancellations.
