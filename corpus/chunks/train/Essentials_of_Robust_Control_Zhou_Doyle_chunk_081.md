# 3.5 State-Space Realizations for Transfer Matrices

In some cases, the natural or convenient description for a dynamical system is in terms of matrix transfer function. This occurs, for example, in some highly complex systems for which the analytic differential equations are too hard or too complex to write down. Hence certain engineering approximation or identification has to be carried out; for example, input and output frequency responses are obtained from experiments so that some transfer matrix approximating the system dynamics can be obtained. Since the state-space computation is most convenient to implement on the computer, some appropriate state-space representation for the resulting transfer matrix is necessary.

In general, assume that $G ( s )$ is a real rational transfer matrix that is proper. Then we call a state-space model $( A , B , C , D )$ such that

$$
G (s) = \left[ \begin{array}{c c} A & B \\ \hline C & D \end{array} \right]
$$

a realization of $G ( s )$ .

Definition 3.9 A state-space realization $( A , B , C , D )$ of $G ( s )$ is said to be a minimal realization of $G ( s )$ if A has the smallest possible dimension.

Theorem 3.6 A state-space realization $( A , B , C , D )$ of $G ( s )$ is minimal if and only if $( A , B )$ is controllable and $( C , A )$ is observable.

We now describe several ways to obtain a state-space realization for a given multipleinput and multiple-output transfer matrix $G ( s )$ . We shall first consider SIMO (singleinput and multiple-output) and MISO (multiple-input and single-output) systems.

Let $G ( s )$ be a column vector of transfer function with p outputs:

$$G (s) = \frac {\beta_ {1} s ^ {n - 1} + \beta_ {2} s ^ {n - 2} + \cdots + \beta_ {n - 1} s + \beta_ {n}}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}} + d, \beta_ {i} \in \mathbb {R} ^ {p}, d \in \mathbb {R} ^ {p}.$$

Then $G ( s ) = \left[ { \frac { A \left. b \right. } { C \left. d \right. } } \right]$ with

$$
A := \left[ \begin{array}{c c c c c} - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} & - a _ {n} \\ 1 & 0 & \dots & 0 & 0 \\ 0 & 1 & \dots & 0 & 0 \\ \vdots & \vdots & & \vdots & \vdots \\ 0 & 0 & \dots & 1 & 0 \end{array} \right] \quad b := \left[ \begin{array}{c} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{array} \right]

C = \left[ \begin{array}{l l l l l} \beta_ {1} & \beta_ {2} & \dots & \beta_ {n - 1} & \beta_ {n} \end{array} \right]
$$

is a so-called controllable canonical form or controller canonical form.

Dually, consider a multiple-input and single-output system
