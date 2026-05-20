Compare with Example 3.9. Summarizing, we find that the solution to the design problem is given by a linear state feedback with the gain

$$
L = \left( \begin{array}{l l l l} p _ {1} - a _ {1} & p _ {2} - a _ {2} & \dots & p _ {n} - a _ {n} \end{array} \right) \bar {W} _ {c} W _ {c} ^ {- 1} \tag {4.13}
$$

This equation can be expressed in a slightly different way by the following result.

THEOREM 4.1 POLE-PLACEMENT USING STATE FEEDBACK Consider the system of (4.2). Assume that there is only one input signal. If the system is reachable there exists a linear feedback that gives a closed-loop system with the characteristic $P(z)$ . The feedback is given by

$$u (k) = - L x (k)$$

with

$$
\begin{array}{l} L = \left( \begin{array}{l l l l} p _ {1} - a _ {1} & p _ {2} - a _ {2} & \dots & p _ {n} - a _ {n} \end{array} \right) \tilde {W} _ {c} W _ {c} ^ {- 1} \tag {4.14} \\ = \left(0 \dots 0 1\right) W _ {c} ^ {- 1} P (\Phi) \\ \end{array}
$$

where $W_{c}$ and $\tilde{W}_{c}$ are the reachability matrices of the systems (4.2) and (4.5), respectively.

Proof. To prove the result we first observe that

$$P (\tilde {\Phi}) = \tilde {\Phi} ^ {n} + p _ {1} \tilde {\Phi} ^ {n - 1} + \dots + p _ {n} I = (p _ {1} - a _ {1}) \tilde {\Phi} ^ {n - 1} + \dots + (p _ {n} - a _ {n}) I$$

where $\tilde{\Phi}$ is the system matrix of the transformed system (4.5). The second equality is obtained by using the Cayley-Hamilton theorem. Introduce $e^{i}$ as the row vector that has all elements equal to zero except the ith element, which is 1. We have

$$e ^ {i} \tilde {\Phi} = e ^ {i - 1}$$

It then follows from Eq. (4.7) that $\tilde{L} = e^n P(\tilde{\Phi})$ and we get

$$L = \hat {L} T = e ^ {n} P (T \Phi T ^ {- 1}) T = e ^ {n} T P (\Phi) = e ^ {n} \tilde {W} _ {c} W _ {c} ^ {- 1} P (\Phi)$$

It follows from (4.12) that $e^n \tilde{W}_r^{-1} = e^n$ and Eq. (4.14) is obtained.

Remark 1. Equation (4.14) is called Ackermann's formula.

Remark 2. Notice that the pole-placement problem can be formulated as the following abstract problem. Given matrices $\Phi$ and $\Gamma$ , find a matrix $L$ such that the matrix $\Phi - \Gamma L$ has prescribed eigenvalues.

Remark 3. Notice that it follows from (4.11) and (4.12) that

$$
T ^ {- 1} = \left( \begin{array}{l l l l} \Gamma & \Phi \Gamma + a _ {1} \Gamma & \dots & \Phi^ {n - 1} \Gamma + a _ {1} \Phi^ {n - 2} + \dots + a _ {n - 1} \Gamma \end{array} \right) \tag {4.15}
$$

The theorem is illustrated by an example.
