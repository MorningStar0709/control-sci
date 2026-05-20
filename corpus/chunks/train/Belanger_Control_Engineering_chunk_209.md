# Proof:

Controllability: We must show that, starting from the zero state at $t = 0$ , it is possible to take the composite state vector $\left[ \mathbf{x}_F^* \right]$ to $\left[ \mathbf{x}_{\mathbf{P}^*}^* \right]$ at $t = T$ , where $T > 0$ and $\mathbf{x}_F^*$ and $\mathbf{x}_P^*$ are arbitrary. Since $F$ and $P$ are controllable, there exist functions $e^*(t)$ and $u^*(t)$ that, respectively, take $\mathbf{x}_F(t)$ to $\mathbf{x}_F^*$ and $\mathbf{x}_P(t)$ to $\mathbf{x}_P^*$ , at time $T$ . The zero-state outputs resulting from the application of $e^*(t)$ and $u^*(t)$ are $z^*(t)$ and $y^*(t)$ , respectively.

Choose the system inputs $y_{d}^{*}(t)$ and $w^{*}(t)$ as follows:

$$
\begin{array}{l} y _ {d} ^ {*} (t) = y ^ {*} (t) + e ^ {*} (t) \\ w ^ {*} (t) = u ^ {*} (t) - z ^ {*} (t) \\ \end{array}
$$

Then it is easy to see that all relationships between the signals are satisfied with $e(t) = e^{*}(t)$ and $u(t) = u^{*}(t)$ , so that the state at time T is indeed the desired one. Thus, the system is controllable.

Observability: Let the inputs $y_{d}(t) = w(t) = 0$ ; let $z(t)$ and $y(t)$ be observed. Since $e(t) = -y(t)$ , the input and the output of F are accessible; since F is observable, the initial state $\mathbf{x}_{F}(0)$ can be uniquely deduced. Since $u(t) = z(t)$ , the input and output of P are also given, so, by the same reasoning, $\mathbf{x}_{P}(0)$ can be obtained and the composite system is observable.

Since the system is controllable and observable, internal stability is guaranteed by input-output stability, leading to the following theorem.
