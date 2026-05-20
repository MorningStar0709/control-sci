If Inequality (10–181) holds true, then it is evident that Inequality (10–180) also holds true. So this is the condition to guarantee the robust stability of the designed system. In Figure 10–57(e), $\Delta _ { a }$ in Figure 10–57(d) was replaced by $W _ { a } I .$ .

To summarize, if we make the $H _ { \infty }$ norm of the transfer function from w to z to be less than 1, the controller K that satisfies Inequality (10–181) can be determined.

Figure $1 0 { - } 5 7 ( \mathrm { e } )$ can be redrawn as that shown in Figure 10–57(f), which is the generalized plant diagram for the system considered.

Note that for this problem the matrix that relates the controlled variable z and the exoge-£ nous disturbance w is given by

$$z = \Phi (s) w = (W _ {a} T _ {a}) w = [ W _ {a} K (I + G K) ^ {- 1} ] w$$

Noting that $u ( s ) = K ( s ) y ( s )$ and referring to Equation (10–128), $\Phi ( s )$ is given by the elements of the P matrix as follows:

$$\Phi (s) = P _ {1 1} + P _ {1 2} K (I - P _ {2 2} K) ^ {- 1} P _ {2 1}$$

To make this $\Phi ( s )$ equal to $W _ { a } K ( I + G K ) ^ { - 1 }$ we may choose, $P _ { 1 1 } = 0 , P _ { 1 2 } = W _ { a } , P _ { 2 1 } = I$ , and $P _ { 2 2 } = - G$ . Then, the P matrix for this problem can be obtained as

$$
P = \left[ \begin{array}{c c} 0 & W _ {a} \\ I & - G \end{array} \right]
$$
