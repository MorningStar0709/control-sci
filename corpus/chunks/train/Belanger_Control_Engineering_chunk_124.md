# ■ Theorem 3.4

An LTI system is controllable [for short, the pair $(A, B)$ is controllable] if, and only if, it has no uncontrollable states.

Proof: To show necessity ("only if"), we show that the existence of a single uncontrollable state precludes controllability. This follows immediately from the definition of an uncontrollable state: no state $\mathbf{x}(T)$ that is not orthogonal to $\mathbf{x}^*$ is reachable.

To show sufficiency (“if”), we show that controllability follows if there is no uncontrollable state. We try a control function $\mathbf{u}(T-\tau)=B^{T}e^{A^{T}\tau}\mathbf{v}$ , where v is an n-vector to be chosen. We have

$$
\begin{array}{l} \mathbf {x} (T) = \int_ {0} ^ {T} e ^ {A \tau} B \mathbf {u} (T - \tau) d \tau \\ = \left[ \int_ {0} ^ {T} e ^ {A \tau} B B ^ {T} e ^ {A ^ {T} \tau} d \tau \right] \mathbf {v} \\ = N (T) \mathbf {v}. \tag {3.49} \\ \end{array}
$$

To exploit a result already derived for observability, $N(T)$ is written as

$$N (T) = \int_ {0} ^ {T} (B ^ {T} e ^ {A ^ {T} \tau}) ^ {T} B ^ {T} e ^ {A ^ {T} \tau} d \tau .$$

By the same reasoning as in Theorem 3.2, $N(T)$ is shown to be positive definite if there exists no uncontrollable state. This means that $N(T)$ can be inverted and Equation 3.49 can be solved uniquely for $\mathbf{v}$ , for arbitrary $\mathbf{x}(T)$ , and proves that a control of the form specified (among others) can take the state from the origin to any desired $\mathbf{x}(T)$ .
