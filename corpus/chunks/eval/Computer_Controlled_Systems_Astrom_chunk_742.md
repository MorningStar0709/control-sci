The problem is more complicated when there is no delay in the controller. The transfer function of the optimal controller in this case was given by Eq. (12.44) with $\deg R(z) = \deg S(z) = n$ , and and $\deg S^{*}(z) < n$ . These conditions are more conveniently expressed using another version of the Diophantine equation (12.47). Assuming $\deg R(z) = \deg S(z) = n$ , writing (12.47) with argument $z^{-1}$ and multiplying it by $z^{2n}$ we find that

$$A ^ {*} (z) R ^ {*} (z) + z ^ {d} B ^ {*} (z) S ^ {*} (z) = P ^ {*} (z) C ^ {*} (z) \tag {12.48}$$

where

$$d = \deg A (z) - \deg B (z)$$

If $\deg A^{*}(z)=n$ the optimal controller is then the unique solution to (12.48) with $\deg S^{*}(z)<\deg A^{*}(z)$ . Notice, however, that this does not give the optimal solution when $\deg A^{*}(z)<n$ , i.e. when $A(0)=0$ . This case will be discussed in the next section where we give a direct solution of the LQG problem with polynomial calculations.
