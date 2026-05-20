# EXAMPLE 6.4 Parametric excitation

Consider the system in Example 6.3. Let the command signal be $u_{c}(t) = \sin \omega t$ . After a transient the model output becomes

$$y _ {m} (t) = \frac {1}{\sqrt {1 + \omega^ {2}}} \sin (\omega t - \arctan (\omega))$$

To determine the stability of Eq. (6.16), we compute W by integrating Eq. (6.18) over one period, that is, $\tau = 2\pi/\omega$ , with the initial condition $\Phi(0) = I$ . Then from Eq. (6.19) we get $W = \Phi(\tau)$ . Choosing $\omega = 2$ and integrating to $\tau = \pi$ give

$$
\Phi (\tau) = \left( \begin{array}{l l} 0. 4 3 7 3 & 0. 7 2 8 3 \\ 0. 2 3 8 9 & 0. 4 9 6 7 \end{array} \right)
$$

with eigenvalues 0.049 and 0.885 for $\gamma = 10$ and

$$
\Phi (\tau) = \left( \begin{array}{l l} 0. 5 6 0 9 & 0. 9 9 6 0 \\ 0. 2 6 4 2 & 0. 5 4 6 3 \end{array} \right)
$$

with eigenvalues 0.041 and 1.067 for $\gamma = 11$ . It can thus be concluded that the adaptive system will be stable for $\gamma = 10$ but unstable for $\gamma = 11$ .

This calculation can be repeated for many frequencies and many values of the adaptation gain to determine the values of $\omega$ and $\gamma$ for which the system is stable. The result of such a calculation is shown in Fig. 6.6. Notice in particular that Fig. 6.6 explains the behavior observed in the numerical experiment in Example 6.3, in which the system goes through a region of instability as the frequency of the input signal increases. Notice, however, that the system is stable for low adaptation gains.

Example 6.3 indicates that even very simple adaptive systems can exhibit complex behavior. The mechanism of periodic excitation can also give rise to instabilities in more complex adaptive systems. The analysis can be made in the same way as for the simple example, but the details are much more complicated. The behavior is typically associated with periodic excitation and comparatively high adaptation gains. The phenomenon illustrated in Fig. 6.5 is an example of parametric excitation, that is, a system can be made unstable by changing its parameters periodically. A classical example is the Mathieu equation:

![](image/d214d110ece70b3de5313999e4fceb605cb79b1ef4ab9ff78d84ca43a864bfb5.jpg)

<details>
<summary>line</summary>
