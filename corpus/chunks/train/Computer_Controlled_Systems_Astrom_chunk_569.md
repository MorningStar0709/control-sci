# Direct- and Companion-Form Realizations

The most straightforward way to realize (9.16) is to write it in the direct form

$$y (k) = \sum_ {i = 0} ^ {m} b _ {i} u (k - i) - \sum_ {i = 1} ^ {m} a _ {i} y (k - i)$$

It is then necessary to store $y(k-1)$ , $y(k-2)$ , $\ldots$ , $y(k-n)$ , and $u(k-1)$ , $\ldots$ , $u(k-m)$ , that is, $n+m$ variables. The direct realization has $n+m$ states and thus is not a minimal realization. The controllable or observable canonical forms, see Sec. 3.4, have n states. The direct form has the advantage that the state variables are simply delayed versions of the input and output signals. This means that the state does not have to be recomputed when the parameters are changed. Both the direct form and the companion form have the disadvantage that the coefficients in the characteristic polynomial are the coefficients in the realizations. This makes the realizations extremely sensitive to computational errors if the system is of high order and if the poles or zeros are close to one as discussed before.
