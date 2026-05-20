# Exercise A.27: Reachability Gramian in continuous time

Consider the symmetric, $n \times n$ matrix W defined by

$$W (t) = \int_ {0} ^ {t} e ^ {(t - \tau) A} B B ^ {\prime} e ^ {(t - \tau) A ^ {\prime}} d \tau$$

The matrix W is known as the reachability Gramian of the linear, time-invariant system. The reachability Gramian proves useful in analyzing controllability and reachability. Prove the following important properties of the reachability Gramian.

(a) The reachability Gramian satisfies the following matrix differential equation

$$\frac {d W}{d t} = B B ^ {\prime} + A W + W A ^ {\prime}W (0) = 0$$

which provides one useful way to calculate its values.

(b) The reachability Gramian W (t) is full rank for all $t > 0$ if and only if the system is controllable.
