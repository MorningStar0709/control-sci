# Solution

(a) The sum of two quadratics is also quadratic, so we parameterize the sum as

$$V (x) = (1 / 2) (x - v) ^ {\prime} H (x - v) + d$$

and solve for v, H, and d. Comparing zeroth, first and second derivatives gives

$$V (\boldsymbol {v}) = d \quad = V _ {1} (\boldsymbol {v}) + V _ {2} (\boldsymbol {v})V _ {x} (x) = H (x - v) = A (x - a) + B (x - b)V _ {x x} = H \quad = A + B$$

Solving these gives

$$H = A + B\nu = H ^ {- 1} (A a + B b)d = V _ {1} (\nu) + V _ {2} (\nu) \tag {1.8}$$

Notice that H is positive definite since A and B are positive definite. Substituting the values of a, A, b, and B, and setting d = 0 gives

$$
V (x) = (1 / 2) (x - v) ^ {\prime} H (x - v)
H = \left[ \begin{array}{c c} 2. 7 5 & 0. 2 5 \\ 0. 2 5 & 2. 7 5 \end{array} \right] \qquad \nu = \left[ \begin{array}{c} - 0. 1 \\ 0. 1 \end{array} \right]
$$

V (x) = 1/4 is plotted for the choice of constant d = 0.

(b) Comparing zeroth, first and second derivatives gives

$$V (\boldsymbol {v}) = d \quad = V _ {1} (\boldsymbol {v}) + V _ {2} (\boldsymbol {v})V _ {x} (x) = H (x - v) = A (x - a) + C ^ {\prime} B (C x - b)V _ {x x} = H \quad = A + C ^ {\prime} B C$$

Solving these gives

$$H = A + C ^ {\prime} B C\nu = H ^ {- 1} (A a + C ^ {\prime} B b)d = V _ {1} (\nu) + V _ {2} (\nu)$$

Notice that H is positive definite since A is positive definite and $C ^ { \prime } B C$ is positive semidefinite for any C.

(c) Define ${ \overline { { x } } } = x - a$ and ${ \overline { { b } } } = b - C a$ , and express the problem as

$$V (\overline {{x}}) = (1 / 2) \overline {{x}} ^ {\prime} A \overline {{x}} + (1 / 2) (C (\overline {{x}} + a) - b) ^ {\prime} B (C (\overline {{x}} + a) - b)= (1 / 2) \overline {{{x}}} ^ {\prime} A \overline {{{x}}} + (1 / 2) (C \overline {{{x}}} - \overline {{{b}}}) ^ {\prime} B (C \overline {{{x}}} - \overline {{{b}}})$$

Apply the solution of the previous part and set the constant to zero to obtain

$$V (\overline {{x}}) = (1 / 2) (\overline {{x}} - \overline {{v}}) ^ {\prime} H (\overline {{x}} - \overline {{v}})H = A + C ^ {\prime} B C\overline {{v}} = H ^ {- 1} C ^ {\prime} B \overline {{b}}$$

Use the matrix inversion lemma’s (1.55) on H and (1.56) on $\overline { { \nu } }$ to obtain

$$\tilde {H} = A ^ {- 1} - A ^ {- 1} C ^ {\prime} (C A ^ {- 1} C ^ {\prime} + B ^ {- 1}) ^ {- 1} C A ^ {- 1}\overline {{v}} = A ^ {- 1} C ^ {\prime} (C A ^ {- 1} C ^ {\prime} + B ^ {- 1}) ^ {- 1} \overline {{b}}$$

The function V is then given by

$$V = (1 / 2) (\overline {{x}} - \overline {{v}}) ^ {\prime} \tilde {H} ^ {- 1} (\overline {{x}} - \overline {{v}})V = (1 / 2) (x - (a + \overline {{v}})) ^ {\prime} \tilde {H} ^ {- 1} (x - (a + \overline {{v}}))V = (1 / 2) (x - \nu) ^ {\prime} \tilde {H} ^ {- 1} (x - \nu)$$

in which

$$\nu = a + A ^ {- 1} C ^ {\prime} \left(C A ^ {- 1} C ^ {\prime} + B ^ {- 1}\right) ^ {- 1} (b - C a)$$

\-
