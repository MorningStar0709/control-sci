$$(X _ {n - 1} - X) A _ {n} + A _ {n} ^ {*} (X _ {n - 1} - X) = - \mathcal {Q} (X) + \hat {F} _ {n} ^ {*} \hat {F} _ {n} + (F _ {n} - F _ {n - 1}) ^ {*} (F _ {n} - F _ {n - 1}) > 0, \tag {14.9}$$

which implies that $A _ { n }$ is antistable by Lyapunov theorem since $X _ { n - 1 } - X > 0$

Now we introduce $X _ { n }$ as the unique solution of the Lyapunov equation:

$$X _ {n} A _ {n} + A _ {n} ^ {*} X _ {n} = F _ {n} ^ {*} F _ {n} - Q. \tag {14.10}$$

Then $X _ { n }$ is Hermitian. Next, we have

$$(X _ {n} - X) A _ {n} + A _ {n} ^ {*} (X _ {n} - X) = - \mathcal {Q} (X) + \hat {F} _ {n} ^ {*} \hat {F} _ {n} > 0,$$

and, by using equation (14.8),

$$(X _ {n - 1} - X _ {n}) A _ {n} + A _ {n} ^ {*} (X _ {n - 1} - X _ {n}) = \left(F _ {n} - F _ {n - 1}\right) ^ {*} \left(F _ {n} - F _ {n - 1}\right) \geq 0.$$

Since $A _ { n }$ is antistable, we have

$$X _ {n - 1} \geq X _ {n} > X.$$

We have a nonincreasing sequence $\{ X _ { i } \}$ , and the sequence is bounded below by $X _ { i } > X$ . Hence the limit

$$X _ {+} := \lim _ {n \to \infty} X _ {n}$$

exists and is Hermitian, and we have $X _ { + } \geq X$ . Passing the limit $n \to \infty$ in equation (14.10), we get $\mathcal { Q } ( X _ { + } ) = 0$ . So $X _ { + }$ is a solution of equation (14.6).

Note that $X _ { + } - X \ge 0$ and

$$(X _ {+} - X) A _ {+} + A _ {+} ^ {*} (X _ {+} - X) = - \mathcal {Q} (X) + (X _ {+} - X) R (X _ {+} - X) > 0. \tag {14.11}$$

Hence, $X _ { + } - X > 0$ and ${ \cal A } _ { + } = { \cal A } + R { \cal X } _ { + }$ is antistable.

Lemma 14.5 There exists an admissible controller such that $\| T _ { z w } \| _ { \infty } < \gamma$ only if the following three conditions hold:

(i) There exists a stabilizing solution $X _ { \infty } > 0$ to

$$X _ {\infty} A + A ^ {*} X _ {\infty} + X _ {\infty} (B _ {1} B _ {1} ^ {*} / \gamma^ {2} - B _ {2} B _ {2} ^ {*}) X _ {\infty} + C _ {1} ^ {*} C _ {1} = 0. \tag {14.12}$$

(ii) There exists a stabilizing solution $Y _ { \infty } > 0$ to

$$A Y _ {\infty} + Y _ {\infty} A ^ {*} + Y _ {\infty} (C _ {1} ^ {*} C _ {1} / \gamma^ {2} - C _ {2} ^ {*} C _ {2}) Y _ {\infty} + B _ {1} B _ {1} ^ {*} = 0. \tag {14.13}$$

$( i i i ) \left[ \begin{array} { c c } { { \gamma Y _ { \infty } ^ { - 1 } } } & { { I _ { n } } } \\ { { I _ { n } } } & { { \gamma X _ { \infty } ^ { - 1 } } } \end{array} \right] > 0 \mathrm { o r } \rho ( X _ { \infty } Y _ { \infty } ) < \gamma ^ { 2 } .$

Proof. Applying Theorem 14.4 to part (i) of Lemma 14.3, we conclude that there exists a $Y > Y _ { 1 } > 0$ such that

$$A Y + Y A ^ {*} + Y C _ {1} ^ {*} C _ {1} Y / \gamma^ {2} + B _ {1} B _ {1} ^ {*} - \gamma^ {2} B _ {2} B _ {2} ^ {*} = 0$$

and $A + C _ { 1 } ^ { * } C _ { 1 } Y / \gamma ^ { 2 }$ is antistable. Let $X _ { \infty } : = \gamma ^ { 2 } Y ^ { - 1 }$ ; we have
