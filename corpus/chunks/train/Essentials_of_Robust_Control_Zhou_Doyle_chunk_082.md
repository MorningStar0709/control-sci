$$G (s) = \frac {\eta_ {1} s ^ {n - 1} + \eta_ {2} s ^ {n - 2} + \cdots + \eta_ {n - 1} s + \eta_ {n}}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}} + d, \eta_ {i} ^ {*} \in \mathbb {R} ^ {m}, d ^ {*} \in \mathbb {R} ^ {m}.$$

Then

$$
G (s) = \left[ \begin{array}{c c} A & B \\ \hline c & d \end{array} \right] = \left[ \begin{array}{c c c c c c} - a _ {1} & 1 & 0 & \dots & 0 & \eta_ {1} \\ - a _ {2} & 0 & 1 & \dots & 0 & \eta_ {2} \\ \vdots & \vdots & \vdots & & \vdots & \vdots \\ - a _ {n - 1} & 0 & 0 & \dots & 1 & \eta_ {n - 1} \\ - a _ {n} & 0 & 0 & \dots & 0 & \eta_ {n} \\ \hline 1 & 0 & 0 & \dots & 0 & d \end{array} \right]
$$

is an observable canonical form or observer canonical form.

For a MIMO system, the simplest and most straightforward way to obtain a realization is by realizing each element of the matrix $G ( s )$ and then combining all these individual realizations to form a realization for $G ( s )$ . To illustrate, let us consider a $2 \times 2$ (block) transfer matrix such as

$$
G (s) = \left[ \begin{array}{l l} G _ {1} (s) & G _ {2} (s) \\ G _ {3} (s) & G _ {4} (s) \end{array} \right]
$$

and assume that $G _ { i } ( s )$ has a state-space realization of the form

$$
G _ {i} (s) = \left[ \begin{array}{c c} A _ {i} & B _ {i} \\ \hline C _ {i} & D _ {i} \end{array} \right], i = 1, \ldots , 4.
$$

Then a realization for $G ( s )$ can be obtained as $( \mathbf { G } = \mathbf { a b v } ( \mathbf { s b s } ( \mathbf { G _ { 1 } } , \mathbf { G _ { 2 } } ) , \mathbf { s b s } ( \mathbf { G _ { 3 } } , \mathbf { G _ { 4 } } ) ) )$ :

$$
G (s) = \left[ \begin{array}{c c c c c c} A _ {1} & 0 & 0 & 0 & B _ {1} & 0 \\ 0 & A _ {2} & 0 & 0 & 0 & B _ {2} \\ 0 & 0 & A _ {3} & 0 & B _ {3} & 0 \\ 0 & 0 & 0 & A _ {4} & 0 & B _ {4} \\ \hline C _ {1} & C _ {2} & 0 & 0 & D _ {1} & D _ {2} \\ 0 & 0 & C _ {3} & C _ {4} & D _ {3} & D _ {4} \end{array} \right].
$$

Alternatively, if the transfer matrix $G ( s )$ can be factored into the product and/or the sum of several simply realized transfer matrices, then a realization for G can be obtained by using the cascade or addition formulas given in the preceding section.

A problem inherited with these kinds of realization procedures is that a realization thus obtained will generally not be minimal. To obtain a minimal realization, a Kalman controllability and observability decomposition has to be performed to eliminate the uncontrollable and/or unobservable states. (An alternative numerically reliable method to eliminate uncontrollable and/or unobservable states is the balanced realization method, which will be discussed later.)
