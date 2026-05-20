$$\mu_ {\Delta} (M) \leq \pi \left(\left[ \| M _ {i j} \| \right]\right) (= \rho \left(\left[ \| M _ {i j} \| \right]\right))$$

where $\pi ( \cdot )$ denotes the Perron eigenvalue.

Problem 10.7 Show

$$\inf _ {D \in \mathbb {C} ^ {n \times n}} \left\| D M D ^ {- 1} \right\| _ {p} = \rho (M)$$

where $\left\| \cdot \right\| _ { p }$ is the induced p-norm, $1 \leq p \leq \infty$ .

Problem 10.8 Let D be a nonsingular diagonal matrix $D = \operatorname { d i a g } ( d _ { 1 } , d _ { 2 } , \dotsc , d _ { n } )$ . Show

$$\inf _ {D} \left\| D M D ^ {- 1} \right\| _ {p} = \pi (M)$$

if either $M = [ | m _ { i } j | ]$ and $1 \leq p \leq \infty$ or $p = 1$ or ∞. Moreover, the optimal $D$ is given by

$$D = \mathrm{diag} (y _ {1} ^ {1 / p} / x _ {1} ^ {1 / q}, y _ {2} ^ {1 / p} / x _ {2} ^ {1 / q}, \ldots , y _ {n} ^ {1 / p} / x _ {n} ^ {1 / q})$$

where $1 / p + 1 / q = 1$ and

$$[ | m _ {i j} | ] x = \pi (M) x, y ^ {T} [ | m _ {i j} | ] = \pi (M) y ^ {T}.$$

Problem 10.9 Let $\Delta$ be a structured uncertainty defined in the book. Suppose $M =$ $x y ^ { * }$ with $x , y \in \mathbb { C } ^ { n }$ . Derive an exact expression for $\mu _ { \Delta } ( M )$ in terms of the components of x and $y .$ . [Note that $\Delta = \mathrm { d i a g } ( \delta _ { 1 } I , \delta _ { 2 } I , \ldots , \delta _ { m } I , \Delta _ { 1 } , \ldots , \Delta _ { F } )$ and $\mu _ { \Delta } ( M ) =$ $\begin{array} { r } { \operatorname* { m a x } _ { U \in \mathcal { U } } \rho ( M U ) = \operatorname* { m a x } _ { \Delta \in \mathbf { B } \Delta } \rho ( M \Delta ) . ] } \end{array}$

Problem 10.10 Let $\{ x _ { k } \} _ { k = 0 } ^ { \infty } , \{ z _ { k } \} _ { k = 0 } ^ { \infty }$ , and $\{ d _ { k } \} _ { k = 0 } ^ { \infty }$ be sequences satisfying

$$\left\| x _ {k + 1} \right\| ^ {2} + \left\| z _ {k} \right\| ^ {2} \leq \beta^ {2} (\left\| x _ {k} \right\| ^ {2} + \left\| d _ {k} \right\| ^ {2})$$

for some $\beta < 1$ and all $k \geq 0$ . If $d \in \ell _ { 2 }$ , show that both $x \in \ell _ { 2 }$ and $z \in \ell _ { 2 }$ and the norms are bounded by

$$\| z \| _ {2} ^ {2} + (1 - \beta^ {2}) \| x \| _ {2} ^ {2} \leq \beta^ {2} \| d \| _ {2} ^ {2} + \| x _ {0} \| ^ {2}$$

Give a system interpretation of this result.

Problem 10.11 Consider a SISO feedback system shown here with

$$P = P _ {0} (1 + W _ {1} \Delta_ {1}) + W _ {2} \Delta_ {2}, \Delta_ {i} \in \mathcal {R H} _ {\infty}, \| \Delta_ {i} \| _ {\infty} < 1, i = 1, 2.$$

Suppose $W _ { 1 }$ and $W _ { 2 }$ are stable, and $P$ and $P _ { 0 }$ have the same number of poles in $\mathrm { R e } \{ s \} > 0$ .

![](image/64dfd4ef151fac17e009d0c08604848ac6211de8017d0f9c2f0f90e4b2501e09.jpg)

<details>
<summary>flowchart</summary>
