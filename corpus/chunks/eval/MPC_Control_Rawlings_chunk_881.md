# Solution

From the definition of joint density we have

$$p (a | b, c) = \frac {p (a , b , c)}{p (b , c)}$$

Multiplying the top and bottom of the fraction by $p ( c )$ yields

$$p (a | b, c) = \frac {p (a , b , c)}{p (c)} \frac {p (c)}{p (b , c)}$$

or

$$p (a | b, c) = \frac {p (a , b | c)}{p (b | c)}$$

Substituting the distribution given in (A.39) and using the result in Example A.38 to evaluate $p ( b | c )$ yields

$$
p (a | b, c) = \frac {N \left(\left[ \begin{array}{c} m _ {a} \\ m _ {b} \end{array} \right] , \left[ \begin{array}{c c} P _ {a} & P _ {a b} \\ P _ {b a} & P _ {b} \end{array} \right]\right)}{N (m _ {b} , P _ {b})}
$$

And now applying the methods of Example A.44 this ratio of normal distributions reduces to the desired expression. -

Adjoint operator. Given a linear operator $\mathcal { G } : \mathbb { U } \to \mathbb { V }$ and inner products for the spaces U and V, the adjoint of $\mathscr { G } .$ , denoted by $G ^ { * }$ is the linear operator $\mathcal { G } ^ { * } : \mathbb { V } \to \mathbb { U }$ such that

$$\langle u, \mathcal {G} ^ {*} v \rangle = \langle \mathcal {G} u, v \rangle , \quad \forall u \in \mathbb {U}, v \in \mathbb {V} \tag {A.40}$$

Dual dynamic system (Callier and Desoer, 1991). The dynamic system

$$x (k + 1) = A x (k) + B u (k), \quad k = 0, \dots , N - 1y (k) = C x (k) + D u (k)$$

maps an initial condition and input sequence $( x ( 0 ) , u ( 0 ) , \ldots , u ( N - 1 ) )$ into a final condition and an output sequence $( x ( N ) , y ( 0 ) , \ldots , y ( N -$ 1)). Call this linear operator $\mathcal { G }$

$$
\left[ \begin{array}{c} x (N) \\ y (0) \\ \vdots \\ y (N - 1) \end{array} \right] = G \left[ \begin{array}{c} x (0) \\ u (0) \\ \vdots \\ u (N - 1) \end{array} \right]
$$

The dual dynamic system represents the adjoint operator $G ^ { * }$

$$
\left[ \begin{array}{c} \overline {{x}} (0) \\ \overline {{y}} (1) \\ \vdots \\ \overline {{y}} (N) \end{array} \right] = \mathcal {G} ^ {*} \left[ \begin{array}{c} \overline {{x}} (N) \\ \overline {{u}} (1) \\ \vdots \\ \overline {{u}} (N) \end{array} \right]
$$

We define the usual inner product, $\langle a , b \rangle = a ^ { \prime } b$ , and substitute into (A.40) to obtain

$$\underbrace {x (0) ^ {\prime} \overline {{x}} (0) + u (0) ^ {\prime} \overline {{y}} (1) + \cdot \cdot \cdot + u (N - 1) ^ {\prime} \overline {{y}} (N)} _ {\langle u, G ^ {*} v \rangle} -\underbrace {x (N) ^ {\prime} \overline {{x}} (N) + y (0) ^ {\prime} \overline {{u}} (1) + \cdots + y (N - 1) ^ {\prime} \overline {{u}} (N)} _ {\langle G u, v \rangle} = 0$$
