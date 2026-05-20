# ■ Theorem 3.1

An LTI system is observable [for short, the pair $(C, A)$ is observable] if, and only if, it has no unobservable states.

Proof: To show necessity ("only if"), we show that the existence of an unobservable state is enough to destroy observability. Let $\mathbf{x}^*$ be an unobservable state and let $\mathbf{x}_1$ be some $n$ -vector. For $\mathbf{x}(0) = \mathbf{x}_1$ , the output response is

$$\mathbf {y} _ {1} (t) = C e ^ {A t} \mathbf {x} _ {1}.$$

By zero-input linearity, the response for $\mathbf{x}(0) = \mathbf{x}_1 + \alpha \mathbf{x}^*$ is

$$\mathbf {y} _ {2} (t) = C e ^ {A t} \mathbf {x} _ {1} + \alpha C e ^ {A t} \mathbf {x} ^ {*} = C e ^ {A t} \mathbf {x} _ {1} = \mathbf {y} _ {1} (t)$$

because $Ce^{At} \mathbf{x}^* = \mathbf{0}$ .

Since $\mathbf{y}_{2}(t)=\mathbf{y}_{1}(t)$ , different initial states produce identical outputs. It is thus impossible to determine uniquely the initial state by observing the output; i.e., the system is not observable.

To show sufficiency (“if”), we show that the absence of unobservable states implies observability. Let $\mathbf{x}(0) = \mathbf{x}_{0} \neq \mathbf{0}$ and write

$$\mathbf {y} (t) = C e ^ {A t} \mathbf {x} _ {0}. \tag {3.36}$$

Premultiply both sides by $(Ce^{At})^T$ to get

$$(C e ^ {A t}) ^ {T} \mathbf {y} (t) = (C e ^ {A t}) ^ {T} C e ^ {A t} \mathbf {x} _ {0}.$$

Now integrate:

$$\int_ {0} ^ {T} (C e ^ {A t}) ^ {T} \mathbf {y} (t) d t = M (T) \mathbf {x} _ {0} \tag {3.37}$$

where

$$M (T) = \int_ {0} ^ {T} (C e ^ {A t}) ^ {T} C e ^ {A t} d t.$$

Note that $M(T)$ is symmetric, since the integrand is a product of a matrix and its transpose.

We now show that $M(T)$ is positive definite for every $T > 0$ . Write

$$
\begin{array}{l} \mathbf {x} _ {0} ^ {T} M (T) \mathbf {x} _ {0} = \int_ {0} ^ {T} \mathbf {x} _ {0} ^ {T} \left(C e ^ {A t}\right) ^ {T} C e ^ {A t} \mathbf {x} _ {0} d t \\ = \int_ {0} ^ {T} \left(C e ^ {A t} \mathbf {x} _ {0}\right) ^ {T} \left(C e ^ {A t} \mathbf {x} _ {0}\right) d t \\ = \int_ {0} ^ {T} \| C e ^ {A t} \mathbf {x} _ {0} \| ^ {2} d t \\ \end{array}
$$

where $\| \mathbf{v}\|$ is the Euclidean norm, i.e., the length of the vector $\mathbf{v}$ .
