$$\left| s \mathbf {I} - \mathbf {A} + \mathbf {B K} \right| = (s - \mu_ {1}) (s - \mu_ {2}) (s - \mu_ {3})$$

Since both sides of this characteristic equation are polynomials in s, by equating the coefficients of the like powers of s on both sides, it is possible to determine the values of $k _ { 1 } , k _ { 2 }$ , and $k _ { 3 }$ . This approach is convenient if n=2 or 3. (For $n = 4 , 5 , 6 , \ldots$ , this approach may become very tedious.)

Note that if the system is not completely controllable, matrix K cannot be determined. (No solution exists.)

Determination of Matrix K Using Ackermann’s Formula. There is a well-known formula, known as Ackermann’s formula, for the determination of the state feedback gain matrix K. We shall present this formula in what follows.

Consider the system

$$\dot {\mathbf {x}} = \mathbf {A x} + \mathbf {B u}$$

where we use the state feedback control u=–Kx. We assume that the system is completely state controllable. We also assume that the desired closed-loop poles are at $s = \mu _ { 1 } , s = \mu _ { 2 } , \ldots , s = \mu _ { n } .$ .

Use of the state feedback control

$$u = - \mathbf {K x}$$

modifies the system equation to

$$\dot {\mathbf {x}} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} \tag {10-14}$$

Let us define

$$\widetilde {\mathbf {A}} = \mathbf {A} - \mathbf {B K}$$

The desired characteristic equation is

$$
\begin{array}{l} \left| s \mathbf {I} - \mathbf {A} + \mathbf {B K} \right| = \left| s \mathbf {I} - \widetilde {\mathbf {A}} \right| = (s - \mu_ {1}) (s - \mu_ {2}) \dots (s - \mu_ {n}) \\ = s ^ {n} + \alpha_ {1} s ^ {n - 1} + \dots + \alpha_ {n - 1} s + \alpha_ {n} = 0 \\ \end{array}
$$

Since the Cayley–Hamilton theorem states that $\widetilde { \mathbf { A } }$ satisfies its own characteristic equation, we have

$$\phi (\widetilde {\mathbf {A}}) = \widetilde {\mathbf {A}} ^ {n} + \alpha_ {1} \widetilde {\mathbf {A}} ^ {n - 1} + \dots + \alpha_ {n - 1} \widetilde {\mathbf {A}} + \alpha_ {n} \mathbf {I} = \mathbf {0} \tag {10-15}$$

We shall utilize Equation (10–15) to derive Ackermann’s formula. To simplify the derivation, we consider the case where n=3. (For any other positive integer n, the following derivation can be easily extended.)

Consider the following identities:
