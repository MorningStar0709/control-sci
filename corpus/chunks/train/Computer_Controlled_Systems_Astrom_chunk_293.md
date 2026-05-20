# Euclid's Algorithm

Examples 5.3 and 5.4 essentially reveal the important issues about Eq. (5.9). It is now simply a matter of giving a formal analysis of the equation. We will first develop a classical result in algebra. This algorithm finds the greatest common divisor G of two polynomials A and B. The algorithm is recursive. If one of the polynomials is zero then the other polynomial is defined as the greatest common divisor G. If this is not the case the algorithm proceeds recursively as follows. Assume that the degree of A is greater or equal to the degree of B. Put $A_{0} = A$ and $B_{0} = B$ . Iterate the equations

$$
\begin{array}{l} A _ {n + 1} = B _ {n} \\ B _ {n + 1} = A _ {n} \bmod B _ {n} \\ \end{array}
$$

until $B_{n+1}=0$ . The greatest common divisor is then $G=B_{n}$ . Backtracking we find that G satisfies the equation

$$A X + B Y = G \tag {5.12}$$

where the polynomials X and Y can be found by keeping track of the quotients and the remainders in the iterations. The link between Euclid's algorithm and the Diophantine equation is thus established and we have the following result.

THEOREM 5.1 EXISTENCE OF SOLUTIONS TO THE DIOPHANTINE EQUATION Let A, B, and C be polynomials with real coefficients. Then Eq. (5.9) has a solution if and only if the greatest common factor of A and B divides C. If one solution $X_{0}$ , $Y_{0}$ exists there are $X = X_{0} + QB$ , and $Y = Y_{0} - QA$ , where Q is an arbitrary polynomial and is also a solution.

Proof. The proof follows directly from Euclid's algorithm. If $A$ and $B$ do not have a common factor we have $G = 1$ . Multiplying Eq. (5.12) by $C$ now gives (5.9).
