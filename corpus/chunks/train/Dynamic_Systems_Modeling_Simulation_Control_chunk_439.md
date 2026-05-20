# Example 8.7

Compute the inverse Laplace transform of

$$Y (s) = \frac {2 s + 5}{s ^ {2} + 8 s + 1 2} = \frac {2 s + 5}{(s + 2) (s + 6)}$$

Clearly, the two poles $( s = - 2 , s = - 6 )$ are distinct. Therefore, the partial-fraction expansion is

$$Y (s) = \frac {2 s + 5}{(s + 2) (s + 6)} = \frac {a _ {1}}{s + 2} + \frac {a _ {2}}{s + 6}$$

Using Eq. (8.16), the first residue is

$$a _ {1} = (s + 2) Y (s) | _ {s = - 2} = \left. \frac {2 s + 5}{s + 6} \right| _ {s = - 2} = \frac {1}{4} = 0. 2 5$$

The second residue is

$$a _ {2} = (s + 6) Y (s) | _ {s = - 6} = \left. \frac {2 s + 5}{s + 2} \right| _ {s = - 6} = \frac {- 7}{- 4} = 1. 7 5$$

We can verify the residue calculation using the MATLAB commands:

$$
\begin{array}{l} > > \text {numY} = [ 2 5 ]; \quad \% Y (s) \text {numerator coefficients in descending powers of} s \\ > > \text { denY } = [ 1 8 1 2 ]; \quad \% Y (s) \text { denominator coefficients; descending powers of } s \\ > > [ a, p, k ] = \text { residue } (\text { numY }, \text { denY }) \\ \end{array}
$$

The result is a = [1.75 0.25](residues), p = [-6 -2](poles), and k = [] (null, no direct terms). Note that $\mathsf { a } ( \mathsf { \Omega } _ { 1 } ) \mathsf { \Omega } = \mathsf { \Omega } _ { 1 } \mathsf { \Omega } _ { \cdot } 7 5 \mathsf { \Omega } ( = a _ { 2 } )$ is the residue for pole $\begin{array} { c c c c } { { \mathrm {  ~ \ p ( 1 ) ~ } } } & { { = } } & { { - 6 \mathrm {  ~ a n d } \mathrm {  ~ a } ( 2 ) } } & { { = } } & { { 0 . 2 5 ( = a _ { 1 } ) } } \end{array}$ is the residue for pole $\begin{array} { r } { \begin{array} { r c l } { \mathtt { p } ( 2 ) } & { = } & { - 2 . } \end{array} } \end{array}$ .

Using the residues, the partial-fraction expansion is

$$Y (s) = \frac {0 . 2 5}{s + 2} + \frac {1 . 7 5}{s + 6}$$

The inverse Laplace transforms of both partial-fraction terms are exponential functions (see number 6 in Table 8.1). Therefore, the inverse Laplace transform of $Y ( s )$ is

$$y (t) = 0. 2 5 e ^ {- 2 t} + 1. 7 5 e ^ {- 6 t}$$
