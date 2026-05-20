implies $a_{1}=a_{2}=\cdots=a_{n}=0$ , i.e., is satisfied only if all coefficients are zero. For example, the functions 1, t, $t^{2}$ are linearly independent over any interval of nonzero duration. A linear combination $a_{1}+a_{2}t+a_{3}t^{2}$ may be zero at isolated points (two at most), but not over the whole interval, unless $a_{1}=a_{2}=a_{3}=0$ .

■ Theorem 3.3

The system $(C, A)$ is unobservable if, and only if, there exists an eigenvector v of the matrix A, such that Cv = 0.

Proof: To show sufficiency (“if”), let $v_{1}, v_{2}, \ldots, v_{k}$ be eigenvectors of A. We show that, if $Cv_{i} = 0$ for some i, the system is not observable. To show this, let $\mathbf{x}(0) = \mathbf{v}_{i}$ and assume $Cv_{i} = 0$ . Then, by Equation 3.13,

$$\mathbf {x} (t) = e ^ {s _ {i} t} \mathbf {v} _ {i}$$

where $s_{i}$ is the eigenvalue corresponding to $v_{i}$ . It follows that

$$C \mathbf {x} (t) = e ^ {s _ {i} t} C \mathbf {v} _ {i} = \mathbf {0}, \quad \text { for all } t$$

and that $v_{i}$ is therefore an unobservable state and the system is not observable.

We show necessity (“only if”) by proving that there can be no unobservable states if $Cv_{i} \neq 0$ for all i. The result will be proved for the special case where A has n distinct eigenvalues, but it is true in general.

If the eigenvalues of $A$ are distinct, it is known that its eigenvectors are linearly independent. This implies that the eigenvectors $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ span the whole state space, so that any $n$ -vector can be expressed as a unique linear combination of $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ . Let $\mathbf{x}(0)$ be so expressed; i.e., let

$$\mathbf {x} (0) = a _ {1} \mathbf {v} _ {1} + a _ {2} \mathbf {v} _ {2} + \dots + a _ {n} \mathbf {v} _ {n}$$

where the $a_{i}$ are constants. Then, by zero-input linearity and Equation 3.13,

$$\mathbf {x} (t) = a _ {1} e ^ {s _ {1} t} \mathbf {v} _ {1} + a _ {2} e ^ {s _ {2} t} \mathbf {v} _ {2} + \dots + a _ {n} e ^ {s _ {n} t} \mathbf {v} _ {n}$$

and

$$\mathbf {y} (t) = C \mathbf {x} (t) = a _ {1} C \mathbf {v} _ {1} e ^ {s _ {1} t} + a _ {2} C \mathbf {v} _ {2} e ^ {s _ {2} t} + \dots + a _ {n} C \mathbf {v} _ {n} e ^ {s _ {n} t}.$$
