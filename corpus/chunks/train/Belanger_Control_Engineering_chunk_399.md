# Example 7.6 (dc Servo)

The dc servo of Example 2.1 (Chapter 2), with $T_{L} = 0$ , is to be regulated to the dc steady state $\theta = \theta_{d}$ , $\omega = i = v = 0$ . We wish to design the optimal LQ control for the performance index of the form

$$J = \int_ {0} ^ {\infty} [ Q _ {1 1} (\theta - \theta_ {d}) ^ {2} + Q _ {2 2} \omega^ {2} + v ^ {2} ] d t.$$

(a) With $Q_{22} = 0$ , choose $Q_{11}$ so that, with the initial state $\theta = \omega = i = 0$ and $\theta_d = 1$ rad, $v(t)$ does not exceed $3\mathrm{V}$ during the transient response.

(b) Experiment with different values of $Q_{22}$ to assess its effect on the response.

Solution The state part of the integrand of $J$ is

$$
Q _ {1 1} \Delta \theta^ {2} + Q _ {2 2} \dot {\omega} ^ {2} = [ \Delta \theta \quad \omega \quad i ] \left[ \begin{array}{c c c} Q _ {1 1} & 0 & 0 \\ 0 & Q _ {2 2} & 0 \\ 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \Delta \theta \\ \omega \\ i \end{array} \right].
$$

The A and B matrices are as in Equation 2.19 (with $T_{L}=0$ ). The Riccati equation and the gain are solved using the computer (MATLAB lqr). The gain is $k^{T}$ , a $1\times3$ matrix. The control v is generated from

$$
v = v ^ {*} - \mathbf {k} ^ {T} (\mathbf {x} - \mathbf {x} ^ {*}) = 0 - \left[ k _ {1} \quad k _ {2} \quad k _ {3} \right] \left(\left[ \begin{array}{l} \theta \\ \omega \\ i \end{array} \right] - \left[ \begin{array}{l} \theta_ {d} \\ 0 \\ 0 \end{array} \right]\right)
= k _ {1} \left(\theta_ {d} - \theta\right) - k _ {2} \omega - k _ {3} i.
$$

Transients are obtained, applying Equation 7.8 with $\Delta\theta(0)=0-1=-1$ and $\Delta\omega(0)=\Delta i(0)=0$ . Figure 7.8 shows results for $Q_{22}=0$ and $Q_{11}=4,9,20$ ; $Q_{11}=4$ yields the responses with the least overshoot and smallest input, and $Q_{11}=20$ gives the most overshoot and the largest input (because it weighs state errors correspondingly more than input effort). Curves with $Q_{11}=4$ and 9 both meet the input requirement $\nu\leq3\mathrm{~V}$ , but $Q_{11}=9$ is selected because it gives a faster angular response. For that value of $Q_{11}$ , the gain vector is $\mathbf{k}^{T}=[3\quad0.8796\quad0.1529]$ .

Figure 7.9 shows a few transients for $\Delta\theta(t)$ and $\omega(t)$ , with $Q_{11}=9$ and with two values of $Q_{22}$ . As $Q_{22}$ is increased, the angular velocity $\omega$ is seen to decrease,

![](image/da778ab2022b645f9e0ea6a1b9a65707a7a9d2ae28981d354501c400b18f87b1.jpg)
