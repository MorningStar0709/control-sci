$$
\left[ \begin{array}{c c} X _ {1} / \gamma & I _ {n} \\ I _ {n} & Y _ {1} / \gamma \end{array} \right] \geq 0 \qquad \text { rank } \left[ \begin{array}{c c} X _ {1} / \gamma & I _ {n} \\ I _ {n} & Y _ {1} / \gamma \end{array} \right] \leq n + r.
$$

![](image/a4870673d4ee6c81a1b68928d50bd692defdc33e7d1ed9b40adfdbb9ae0d7f3d.jpg)

To show that the inequalities in the preceding lemma imply the existence of the stabilizing solutions to the Riccati equations of $X _ { \infty }$ and $Y _ { \infty } .$ , we need the following theorem.

Theorem 14.4 Let $R \geq 0$ and suppose $( A , R )$ is controllable and there is an $X = X ^ { * }$ such that

$$\mathcal {Q} (X) := X A + A ^ {*} X + X R X + Q < 0. \tag {14.5}$$

Then there exists a solution $X _ { + } > X$ to the Riccati equation

$$X _ {+} A + A ^ {*} X _ {+} + X _ {+} R X _ {+} + Q = 0 \tag {14.6}$$

such that $A + R X _ { + }$ is antistable.

Proof. Let $R = B B ^ { * }$ for some B. Note the fact that $( A , R )$ is controllable iff (A, B) is. Let X be such that $\mathcal { Q } ( X ) < 0$ . Since $( A , B )$ is controllable, there is an $F _ { 0 }$ such that

$$A _ {0} := A - B F _ {0}$$

is antistable. Now let $X _ { 0 } = X _ { 0 } ^ { * }$ be the unique solution to the Lyapunov equation

$$X _ {0} A _ {0} + A _ {0} ^ {*} X _ {0} - F _ {0} ^ {*} F _ {0} + Q = 0.$$

Define

$$\hat {F} _ {0} := F _ {0} + B ^ {*} X,$$

and we have the following equation:

$$(X _ {0} - X) A _ {0} + A _ {0} ^ {*} (X _ {0} - X) = \hat {F} _ {0} ^ {*} \hat {F} _ {0} - \mathcal {Q} (X) > 0.$$

The antistability of $A _ { 0 }$ implies that

$$X _ {0} > X.$$

Starting with $X _ { 0 } .$ , we shall define a nonincreasing sequence of Hermitian matrices $\{ X _ { i } \}$ . Associated with $\{ X _ { i } \}$ , we shall also define a sequence of antistable matrices $\{ A _ { i } \}$ and a sequence of matrices $\{ F _ { i } \}$ . Assume inductively that we have already defined matrices $\{ X _ { i } \} , \{ A _ { i } \}$ , and $\{ F _ { i } \}$ for i up to $n - 1$ such that $X _ { i }$ is Hermitian and

$$X _ {0} \geq X _ {1} \geq \dots \geq X _ {n - 1} > X,A _ {i} = A - B F _ {i} \text { is antistable, } i = 0, \dots , n - 1;F _ {i} = - B ^ {*} X _ {i - 1}, i = 1, \dots , n - 1;X _ {i} A _ {i} + A _ {i} ^ {*} X _ {i} = F _ {i} ^ {*} F _ {i} - Q, i = 0, 1, \dots , n - 1. \tag {14.7}$$

Next, introduce

$$F _ {n} = - B ^ {*} X _ {n - 1},A _ {n} = A - B F _ {n}.$$

First we show that $A _ { n }$ is antistable. Using equation (14.7), with $i = n - 1$ , we $\mathrm { g e t }$

$$X _ {n - 1} A _ {n} + A _ {n} ^ {*} X _ {n - 1} + Q - F _ {n} ^ {*} F _ {n} - (F _ {n} - F _ {n - 1}) ^ {*} (F _ {n} - F _ {n - 1}) = 0. \tag {14.8}$$

Let

$$\hat {F} _ {n} := F _ {n} + B ^ {*} X;$$

then
