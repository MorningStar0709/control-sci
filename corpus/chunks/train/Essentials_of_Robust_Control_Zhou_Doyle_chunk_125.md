$${e _ {1}} = {w _ {1} + \hat {K} e _ {2}}{e _ {2}} = {w _ {2} + P e _ {1}.}$$

Then an expression for $e _ { 1 }$ can be obtained as

$$(I - \hat {K} P) e _ {1} = w _ {1} + \hat {K} w _ {2}.$$

Thus well-posedness is equivalent to the condition that $( I - \hat { K } P ) ^ { - 1 }$ exists and is proper. But this is equivalent to the condition that the constant term of the transfer function $I - { \hat { K } } P$ is invertible. ✷

It is straightforward to show that equation (5.2) is equivalent to either one of the following two conditions:

$$
\left[ \begin{array}{c c} I & - \hat {K} (\infty) \\ - P (\infty) & I \end{array} \right] \text {   is   invertible; } \tag {5.3}
I - P (\infty) \hat {K} (\infty) \mathrm{isinvertible}.
$$

The well-posedness condition is simple to state in terms of state-space realizations. Introduce realizations of $P$ and $\hat { K }$ :

$$
P = \left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right], \quad \hat {K} = \left[ \begin{array}{c c} \hat {A} & \hat {B} \\ \hline \hat {C} & \hat {D} \end{array} \right].
$$

Then $P ( \infty ) = D , \hat { K } ( \infty ) = \hat { D }$ and the well-posedness condition in equation (5.3) is equivalent to the invertibility of $\left\lceil \begin{array} { c c } { I } & { - \hat { D } } \\ { - D } & { I } \end{array} \right\rceil$ Fortunately, in most practical cases we shall have $D = 0$ , and hence well-posedness for most practical control systems is guaranteed.
