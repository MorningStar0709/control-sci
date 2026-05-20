The previous analysis can be easily extended to the vector function $\mathbf{x}(k)$ of nth order. Thus, consider a functional which is the vector version of the scalar functional (5.1.1) as

$$J (\mathbf {x} (k _ {0}), k _ {0}) = J = \sum_ {k = k _ {0}} ^ {k _ {f} - 1} V (\mathbf {x} (k), \mathbf {x} (k + 1), k). \tag {5.1.13}$$

We will only give the corresponding final Euler-Lagrange equation and the transversality condition, respectively, as

$$\frac {\partial V \left(\mathbf {x} ^ {*} (k) , \mathbf {x} ^ {*} (k + 1) , k\right)}{\partial \mathbf {x} ^ {*} (k)} + \frac {\partial V \left(\mathbf {x} ^ {*} (k - 1) , \mathbf {x} ^ {*} (k) , k - 1\right)}{\partial \mathbf {x} ^ {*} (k)} = 0 \tag {5.1.14}$$

and

$$\left. \left[ \frac {\partial V (\mathbf {x} ^ {*} (k - 1) , \mathbf {x} ^ {*} (k) , k - 1)}{\partial \mathbf {x} ^ {*} (k)} \right] \right| _ {k = k _ {f}} = 0. \tag {5.1.15}$$

Note in the Euler-Lagrange equation (5.1.10) or (5.1.14),

1. the first term involves taking the partial derivative of the given function $V(\mathbf{x}^{*}(k), \mathbf{x}^{*}(k + 1), k)$ w.r.t. $\mathbf{x}(k)$ and   
2. the second term considers taking the partial derivative of $V(\mathbf{x}^*(k - 1), \mathbf{x}^*(k), k - 1)$ (one step behind) w.r.t. the same function $\mathbf{x}(k)$ .

The second function $V(\mathbf{x}^{*}(k-1),\mathbf{x}^{*}(k),k-1)$ can be easily obtained from the given function $V(\mathbf{x}^{*}(k),\mathbf{x}^{*}(k+1),k)$ just by replacing k by k-1. Also, compare the previous results with the corresponding results for continuous-time systems in Chapter 2.
