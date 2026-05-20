# Example 5.1

Consider the minimization of a functional

$$J (x \left(k _ {0}\right), k _ {0}) = J = \sum_ {k = k _ {0}} ^ {k _ {f} - 1} [ x (k) x (k + 1) + x ^ {2} (k) ] \tag {5.1.23}$$

subject to the boundary conditions $\mathrm{x}(0) = 2$ , and $\mathrm{x}(10) = 5$ .

Solution: Let us identify in (5.1.23) that

$$V (x (k), x (k + 1)) = x (k) x (k + 1) + x ^ {2} (k) \tag {5.1.24}$$

and hence

$$V (x (k - 1), x (k)) = x (k - 1) x (k) + x ^ {2} (k - 1). \tag {5.1.25}$$

Then using the Euler-Lagrange equation (5.1.10), which is the same as the scalar version of (5.1.21), we get

$$x (k + 1) + 2 x (k) + x (k - 1) = 0 \tag {5.1.26}$$

or

$$x (k + 2) + 2 x (k + 1) + x (k) = 0 \tag {5.1.27}$$

which upon solving with the given boundary conditions $x(0) = 2$ and $x(10) = 5$ , becomes

$$x (k) = 2 (- 1) ^ {k} + 0. 3 k (- 1) ^ {k}. \tag {5.1.28}$$
