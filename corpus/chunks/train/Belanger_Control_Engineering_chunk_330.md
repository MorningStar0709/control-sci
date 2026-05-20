# Lag Compensation in the Frequency Domain

The value of gain that is used in gain compensation is usually dictated by stability considerations. It is often the case that this gain value is not high enough to satisfy a given steady-state specification. The pure-gain design must be modified so as to achieve the steady-state specification and maintain the required degree of stability (i.e., the stability margins, peak frequency response, or pole damping).

We assume that a design is available (e.g., a pure-gain design) that provides satisfactory stability but not enough dc gain to give acceptable position or velocity constants. Because stability depends on the frequency behavior in the neighborhood of crossover, it is best to leave the design essentially undisturbed in that frequency range. We modify the design at and near zero frequency, because the steady-state behavior depends on the behavior of the loop gain near $\omega = 0$ .

Figure 6.18 shows the structure of the lag compensator. The controller transfer function is

$$\frac {u}{e} = G _ {c} (s) = \left(1 + \frac {k _ {1}}{T s + 1}\right). \tag {6.27}$$

An equivalent expression is

$$
\begin{array}{l} G _ {c} (s) = \frac {T s + 1 + k _ {1}}{T s + 1} \\ = (1 + k _ {1}) \frac {[ T / (1 + k _ {1}) ] s + 1}{T s + 1}. \tag {6.28} \\ \end{array}
$$

This form is the one seen most often in control texts.

At dc, $G_{c}(0) = (1 + k_{1})$ . From Equation 6.27, we see that at high frequencies, where $|k_{1} / (j\omega T + 1)| \ll 1$ , $G_{c} \approx 1$ . The basic idea is to choose $k_{1}$ such that $G_{c}(0) = (1 + k_{1})$ yields a satisfactory position or velocity constant, and to choose $T$ such that $G_{c} \approx 1$ in the critical frequencies region where the stability margins are determined. This ensures satisfactory dc gain without disturbing the stability.

Suppose the dc specification is $G_{c}(0) = k_{0}$ . Then $k_{1}$ is chosen as follows:

$$(1 + k _ {1}) = k _ {0}$$

or

$$k _ {1} = (k _ {0} - 1). \tag {6.29}$$

It is assumed that $k_0 > 1$ , so $k_1 > 0$ ; otherwise, the pure-gain control yields satisfactory dc performance.

Let $\omega_{c}$ be some frequency in the critical region. We shall take $\omega_{c}$ to be the crossover frequency, but it could also be, for example, the frequency at which the phase is $180^{\circ}$ .

![](image/52746c8105896b7c119af0efac747a83d1f8375312fa7647a06678b5fa624fc1.jpg)

<details>
<summary>flowchart</summary>
