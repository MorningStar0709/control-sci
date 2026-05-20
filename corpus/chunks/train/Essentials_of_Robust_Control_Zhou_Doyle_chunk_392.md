Problem 14.2 Make the same assumptions as in Chapter 13 for $\mathcal { H } _ { 2 }$ control and derive the $\mathcal { H } _ { \infty }$ controller parameterization by using the normalization procedure and Theorem 14.7.

Problem 14.3 Consider the feedback system in Figure 6.3 and suppose

$$P = \frac {s - 1 0}{(s + 1) (s + 1 0)}, W _ {e} = \frac {1}{s + 0 . 0 0 1}, W _ {u} = \frac {s + 2}{s + 1 0}.$$

Design a controller that minimizes

$$
\left\| \left[ \begin{array}{c} W _ {e} S _ {o} \\ W _ {u} K S _ {o} \end{array} \right] \right\| _ {\infty}.
$$

Simulate the time response of the system when r is a step.

Problem 14.4 Repeat Problem 14.3 when $W _ { e } = 1 / s$ .

Problem 14.5 Consider again Problem 13.5 and design a controller that minimizes the $\mathcal { H } _ { \infty }$ norm of the transfer matrix from r to $( e , u _ { w } )$ .

Problem 14.6 Repeat Problem 14.5 with $W = \epsilon$ for $\epsilon = 0 . 0 1$ and 0.0001. Study the behavior of the controller when $\epsilon  0$ .

Problem 14.7 Repeat Problem 14.5 and Problem 14.6 with

$$P = \frac {1 0 (2 - s)}{(s + 1) ^ {3}}.$$

Problem 14.8 Let $N \in \mathcal { R } \mathcal { H } _ { \infty } ^ { - }$ . The Nehari problem is the following approximation problem:

$$\inf _ {Q \in \mathcal {R H} _ {\infty}} \| N - Q \| _ {\infty}.$$

Formulate the Nehari problem as a standard $\mathcal { H } _ { \infty }$ control problem.

Problem 14.9 Consider a generalized plant

$$
P = \left[ \begin{array}{c c c c} - 4 & 2 5 & 0. 8 & - 1 \\ - 1 0 & 2 9 & 0. 9 & - 1 \\ \hline 1 0 & - 2 5 & 0 & 1 \\ 1 3 & 2 5 & 1 & 0 \end{array} \right]
$$

with an SISO controller K. Find the optimal $\mathcal { H } _ { \infty }$ performance $\gamma _ { \mathrm { o p t } }$ . Calculate the central controller for each $\gamma \in ( \gamma _ { \mathrm { o p t } } , 2 )$ and the corresponding $\mathcal { H } _ { \infty }$ performance, $\gamma _ { \infty } .$ Plot $\gamma _ { \infty }$ versus $\gamma .$ Is $\gamma _ { \infty }$ monotonic with respect to $\gamma \smash { ? }$ (See Ushida and Kimura [1996] for a detailed discussion.)

Problem 14.10 Let a satellite model be given by $P _ { o } ( s ) = \left[ { \frac { A \ { \Big | } \ B } { C \ { \Big | } \ 0 \ { \Big ] } } } \right]$ , where

$$
A = \left[ \begin{array}{c c c c} {0} & {1} & {0} & {0} \\ {0} & {0} & {0} & {0} \\ {0} & {0} & {0} & {1} \\ {0} & {0} & {- 1. 5 3 9 ^ {2}} & {- 2 \times 0. 0 0 3 \times 1. 5 3 9} \end{array} \right], \quad B = \left[ \begin{array}{c} {0} \\ {1. 7 3 1 9 \times 1 0 ^ {- 5}} \\ {0} \\ {3. 7 8 5 9 \times 1 0 ^ {- 4}} \end{array} \right],

C = \left[ \begin{array}{l l l l} 1 & 0 & 1 & 0 \end{array} \right], \quad D = 0.
$$
