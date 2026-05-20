# 5.1.2 Functional with Terminal Cost

Let us formulate the cost functional with terminal cost (in addition to summation cost) as

$$
\begin{array}{l} J = J (\mathbf {x} (k _ {0}), k _ {0}) \\ = S \left(\mathbf {x} \left(k _ {f}\right), k _ {f}\right) + \sum_ {k = k _ {0}} ^ {k _ {f} - 1} V (\mathbf {x} (k), \mathbf {x} (k + 1), k) \tag {5.1.16} \\ \end{array}
$$

given the initial condition $\mathbf{x}(k_{0})$ and the final time $k_{f}$ as fixed, and the final state $\mathbf{x}(k_{f})$ as free. First, assume optimal (\*) condition and then consider the variations as

$$\mathbf {x} (k) = \mathbf {x} ^ {*} (k) + \delta \mathbf {x} (k)\mathbf {x} (k + 1) = \mathbf {x} ^ {*} (k + 1) + \delta \mathbf {x} (k + 1). \tag {5.1.17}$$

Then, the corresponding functionals $J$ and $J^{*}$ become

$$
J ^ {*} = S \left(\mathbf {x} ^ {*} \left(k _ {f}\right), k _ {f}\right) + \sum_ {k = k _ {0}} ^ {k _ {f} - 1} V \left(\mathbf {x} ^ {*} (k), \mathbf {x} ^ {*} (k + 1), k\right), \tag {5.1.18}
\begin{array}{l} J = S \left(\mathbf {x} ^ {*} \left(k _ {f}\right) + \delta \mathbf {x} \left(k _ {f}\right), k _ {f}\right) \\ + \sum_ {k = k _ {0}} ^ {k _ {f} - 1} V (\mathbf {x} ^ {*} (k) + \delta \mathbf {x} (k), \mathbf {x} ^ {*} (k + 1) + \delta \mathbf {x} (k + 1), k). \tag {5.1.19} \\ \end{array}
$$

Following the same procedure as given previously for a functional without terminal cost, we get the first variation as

$$
\begin{array}{l} \delta J = \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left[ \frac {\partial V (\mathbf {x} ^ {*} (k) , \mathbf {x} ^ {*} (k + 1) , k)}{\partial \mathbf {x} ^ {*} (k)} + \frac {\partial V [ \mathbf {x} ^ {*} (k - 1) , \mathbf {x} ^ {*} (k) , k - 1)}{\partial \mathbf {x} ^ {*} (k)} \right] ^ {\prime} \delta \mathbf {x} (k) \\ + \left. \left[ \frac {\partial V (\mathbf {x} ^ {*} (k - 1) , \mathbf {x} ^ {*} (k) , k - 1)}{\partial \mathbf {x} ^ {*} (k)} \delta \mathbf {x} (k) \right] \right| _ {k = k _ {0}} ^ {k = k _ {f}} \\ + \frac {\partial S (\mathbf {x} ^ {*} (k _ {f}) , k _ {f})}{\partial \mathbf {x} ^ {*} (k _ {f})} \delta \mathbf {x} (k _ {f}). \tag {5.1.20} \\ \end{array}
$$

For extremization, the first variation $\delta J$ must be zero. Hence, from (5.1.20) the Euler-Lagrange equation becomes

$$\boxed {\frac {\partial V \left(\mathbf {x} ^ {*} (k) , \mathbf {x} ^ {*} (k + 1) , k\right)}{\partial \mathbf {x} ^ {*} (k)} + \frac {\partial V \left(\mathbf {x} ^ {*} (k - 1) , \mathbf {x} ^ {*} (k) , k - 1\right)}{\partial \mathbf {x} ^ {*} (k)} = 0.} \tag {5.1.21}$$

and the transversality condition for the free-final point becomes

$$\boxed {\left. \left[ \frac {\partial V (\mathbf {x} ^ {*} (k - 1) , \mathbf {x} ^ {*} (k) , k - 1)}{\partial \mathbf {x} ^ {*} (k)} + \frac {\partial S (\mathbf {x} ^ {*} (k _ {f}) , k _ {f})}{\partial \mathbf {x} ^ {*} (k _ {f})} \right] \right| _ {k = k _ {f}} = 0.} \tag {5.1.22}$$

Let us now illustrate the application of the Euler-Lagrange equation for discrete-time functionals.
