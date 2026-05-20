# 7.3 POLE PLACEMENT

A look back at Example 7.1 will show that the two gains $k_{1}$ and $k_{2}$ can be chosen to achieve any desired closed-loop characteristic polynomial and, hence, any real or complex conjugate eigenvalue pair. The reason is that $k_{1}$ and $k_{2}$ allow independent adjustment of the coefficients of the first and zero powers of $s$ . That is true in general for controllable systems.

We need the following result:

Lemma 7.1 Let $(A, \mathbf{b})$ be a controllable single-input, single-output (SISO) system of order $n$ . There exists a nonsingular $n \times n$ matrix $T$ such that, with $A_c = T^{-1}AT$ and $\mathbf{b}_c = T^{-1}\mathbf{b}$ , $(A_c, \mathbf{b}_c)$ is the controllable canonical form.

Proof: Consider the system

$$\dot {\mathbf {x}} = A \mathbf {x} + \mathbf {b} u\mathbf {y} = I \mathbf {x} \tag {7.12}$$

where $I$ is the $n \times n$ identity matrix. This realization is minimal because (i) $(A, \mathbf{b})$ is controllable and (ii) $(I, A)$ is obviously observable since all state variables are measured. That being the case, the vector transfer function $\mathbf{h}(s) = \mathbf{y}(s) / u(s)$ is of order $n$ . In particular, a controllable canonical form can be written for each element of $\mathbf{h}(s)$ . The $A$ matrix is common to all, because the modes are common, and the rows of the C matrix are written directly from the numerator polynomials of $\mathbf{h}(s)$ . We write

$$\dot {\mathbf {z}} = A _ {c} \mathbf {z} + \mathbf {b} _ {c} u\mathbf {y} = T \mathbf {z} \tag {7.13}$$

as the desired realization.

Since Equations 7.12 and 7.13 are realizations of the same transfer function, the corresponding impulse responses are the same. Thus,

$$e ^ {A t} \mathbf {b} = T e ^ {A _ {c} t} \mathbf {b} _ {c}, \quad \text { for all } t.$$

Taking time derivatives and evaluating at $t = 0$ yields

$$\mathbf {b} = T \mathbf {b} _ {c}\mathbf {A} \mathbf {b} = T A _ {c} \mathbf {b} _ {s}A ^ {2} \mathbf {b} = T A _ {c} ^ {2} \mathbf {b} _ {c}\vdots = \quad \vdotsA ^ {n - 1} \mathbf {b} = T A _ {c} ^ {n - 1} \mathbf {b} _ {c}$$

or

$$[ \mathbf {b} \quad A \mathbf {b} \quad \dots \quad A ^ {n - 1} \mathbf {b} ] = T [ \mathbf {b} _ {c} \quad A _ {c} \mathbf {b} _ {c} \quad \dots \quad A _ {c} ^ {n - 1} \mathbf {b} _ {c} ].$$

We identify the two controllability matrices as C and $C_{c}$ , and write

$$T = \mathcal {C C} _ {c} ^ {- 1} \tag {7.14}$$
