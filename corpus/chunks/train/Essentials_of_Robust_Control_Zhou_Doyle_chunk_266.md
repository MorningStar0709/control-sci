$$\gg \left[ \mathbf {D} _ {\ell}, \mathbf {D} _ {\mathbf {r}} \right] = \text { unwrapd(rowd,blk) }$$

where $D _ { \ell }$ and $D _ { r }$ denote the left and right scaling matrices used in computing the upper-bound inf $\overline { { \sigma } } \left( D _ { \ell } M D _ { r } ^ { - 1 } \right)$ when some full blocks are not necessarily square and they are equal if all full blocks are square.

Example 10.2 Let

$$
M = \left[ \begin{array}{c c c c c c c} j & 2 & 2 j & 0 & - 1 & - 1 + 3 j & 2 + 3 j \\ 3 + j & 2 - j & - 1 + j & 2 + j & - 1 + j & 1 & - 1 + j \\ 3 + j & j & 2 + 2 j & - 1 + 2 j & 3 - j & 3 j & - 1 + j \\ - 1 + j & - 1 - j & j & 0 & 1 - j & 2 - j & 2 + 2 j \\ 3 & j & 1 + j & 3 j & 1 + j & 3 j & - j \\ 1 & 3 + 2 j & 2 + 2 j & 3 j & 1 + 2 j & 2 + j & - 1 + 2 j \\ 2 + j & - 1 - j & - 1 & 3 + 3 j & 2 + 3 j & 2 j & 1 - j \end{array} \right]
$$

and

$$
\boldsymbol {\Delta} = \left\{\Delta = \left[ \begin{array}{c c c c} \delta_ {1} I _ {2} & & & \\ & \delta_ {2} & & \\ & & \Delta_ {3} & \\ & & & \Delta_ {4} \end{array} \right]: \delta_ {1}, \delta_ {2} \in \mathbb {C}, \Delta_ {3} \in \mathbb {C} ^ {2 \times 3}, \Delta_ {4} \in \mathbb {C} ^ {2 \times 1} \right\}.
$$

${ \begin{array} { r l } & { { \mathrm { T h e n ~ b l k } } = { \left[ \begin{array} { l l } { 2 } & { 0 } \\ { 1 } & { 1 } \\ { 2 } & { 3 } \\ { 2 } & { 1 } \end{array} \right] } { \mathrm { ~ a n d ~ t h e ~ M A T L A B ~ p r o g r a m ~ g i v e s ~ b o u n d s } } = { \left[ \begin{array} { l l } { 1 0 . 5 9 5 5 } & { 1 0 . 5 5 1 8 } \end{array} \right] } } \\ & { { \mathrm { a n d } } } \end{array} }$

and

$$
D _ {\ell} = \left[ \begin{array}{c c c c} {D _ {1}} & & & \\ & {0. 7 6 3 8} & & \\ & & {0. 8 8 0 9 I _ {3}} & \\ & & & {1. 0 2 9 3} \end{array} \right]

D _ {r} = \left[ \begin{array}{c c c c} D _ {1} & & & \\ & 0. 7 6 3 8 & & \\ & & 0. 8 8 0 9 I _ {2} & \\ & & & 1. 0 2 9 3 I _ {2} \end{array} \right]
$$

where

$$
D _ {1} = \left[ \begin{array}{c c} 1. 0 2 6 0 - 0. 0 6 5 7 j & 0. 2 1 7 4 - 0. 3 4 7 1 j \\ - 0. 0 7 0 1 + 0. 3 8 7 1 j & - 0. 4 4 8 7 - 0. 6 9 5 3 j \end{array} \right].
$$

In fact, $D _ { \ell }$ and $D _ { r }$ can be replaced by Hermitian matrices without changing the upperbound by replacing $D _ { 1 }$ with

$$
\hat {D} _ {1} = \left[ \begin{array}{c c} 1. 0 9 9 2 & 0. 0 0 4 1 - 0. 0 5 9 1 j \\ 0. 0 0 4 1 + 0. 0 5 9 1 j & 0. 9 2 1 5 \end{array} \right]
$$

since $D _ { 1 } = U _ { 1 } \hat { D } _ { 1 }$ and

$$
U _ {1} = \left[ \begin{array}{c c} 0. 9 1 5 5 - 0. 0 7 1 3 j & 0. 2 3 6 5 - 0. 3 1 7 7 j \\ - 0. 1 0 2 9 + 0. 3 8 2 4 j & - 0. 5 1 1 1 - 0. 7 6 2 9 j \end{array} \right]
$$

is a unitary matrix.
