# THEOREM 6.2 Solution of periodic systems

The solution to the matrix differential equation (6.18) has the form

$$\Phi (t) = D (t) e ^ {C t}$$

where C is a constant matrix and D is periodic with period $\tau$ .

Proof: Since the matrix $W$ in Eq. (6.19) is nonsingular, there exists a matrix $C$ such that

$$W = e ^ {C \tau} \tag {6.20}$$

Introduce the matrix function $D(t)$ defined by

$$D (t) = \Phi (t) e ^ {- C t}$$

Then

$$D (t + \tau) = \Phi (t + \tau) e ^ {- C (t + \tau)} = \Phi (t) W e ^ {- C \tau} e ^ {C t} = D (t)$$

and the theorem is proven.

Remark. From Eq. (6.20) we see that the differential equation (6.18) is stable if the matrix C has all its eigenvalues in the left half-plane, which means that the matrix W should have all its eigenvalues inside the unit disc. Stability can thus be determined by numerical integration over one period. □

We now show how the results can be used to investigate the stability of the system in Example 6.3.
