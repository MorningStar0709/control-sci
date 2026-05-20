# 4.2.1 State Estimation as Optimal Control of Estimate Error

Given the many structural similarities between estimation and regulation, the reader may wonder why the stability analysis of the full information estimator presented in the previous section looks rather different than the zero-state regulator stability analysis presented in Chapter 2. To provide some insight into essential differences, as well as similarities, between estimation and regulation, consider again the estimation problem in the simplest possible setting with a linear time invariant model and Gaussian noise

$$
\begin{array}{l} x ^ {+} = A x + G w \quad w \sim N (0, Q) \\ y = C x + v \quad v \sim N (0, R) \tag {4.8} \\ \end{array}
$$

and random initial state $x ( 0 ) \sim N ( \overline { { x } } ( 0 ) , P ^ { - } ( 0 ) )$ . In full information estimation, we define the objective function

$$V _ {T} (\chi (0), \boldsymbol {\omega}) = \frac {1}{2} \left(| \chi (0) - \overline {{\chi}} (0) | _ {(P ^ {-} (0)) ^ {- 1}} ^ {2} + \sum_ {i = 0} ^ {T - 1} | \boldsymbol {\omega} (i) | _ {Q ^ {- 1}} ^ {2} + | \nu (i) | _ {R ^ {- 1}} ^ {2}\right)$$

subject to $\chi ^ { + } ~ = ~ A \chi + G \omega , ~ \gamma ~ = ~ C \chi + \nu$ . Denote the solution to this optimization as

$$(\hat {x} (0 | T), \hat {\mathbf {w}} _ {T}) = \arg \min _ {\chi (0), \boldsymbol {\omega}} V _ {T} (\chi (0), \boldsymbol {\omega})$$

and the trajectory of state estimates comes from the model ${ \hat { x } } ( i { + } 1 | T ) =$ $A \hat { x } ( i | T ) + G \hat { w } ( i | T )$ . We define estimate error as $\tilde { x } ( i | T ) = x ( i ) - \hat { x } ( i | T )$ for $0 \leq i \leq T - 1 , T \geq 1$ .

Because the system is linear, the estimator is stable if and only if it is stable with zero process and measurement disturbances. So analyzing stability is equivalent to the following simpler question. If noise-free data are provided to the estimator, $( \boldsymbol { w } ( i ) , \boldsymbol { \nu } ( i ) ) ~ = ~ 0$ for all $i \geq 0$ in (4.8), is the estimate error asymptotically stable as $T \to \infty$ for all $x _ { 0 } ?$ We next make this statement precise. First we note that the noise-free measurement satisfies $y ( i ) - C \hat { x } ( i | T ) = C \widetilde { x } ( i | T ) , 0 \leq i \leq T$ and the initial condition term can be written in estimate error as ${ \hat { x } } ( 0 ) - { \overline { { x } } } ( 0 ) =$ $- ( \tilde { x } ( 0 ) - a )$ in which $a = x ( 0 ) - { \overline { { x } } } ( 0 )$ . For the noise-free measurement we can therefore rewrite the cost function as
