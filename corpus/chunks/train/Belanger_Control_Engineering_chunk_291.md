# Problems

5.1 Let $P(s) = (s - 1) / [(s + 1)(s + 2)]$ and $F(s) = k / (s - 1)$ .

a. Obtain minimal realizations for $P$ and $F$ .   
b. Combine the realizations obtained in part (a) to derive a third-order realization for the 1-DOF system.   
c. Show that the 1-DOF closed-loop system has an unobservable mode at $s = 1$ , independent of $k$ .

5.2 Repeat Problem 5.1 for $P(s) = 1 / [(s - 1)(s + 1)]$ and $F(s) = k[(s - 1) / (s + 2)]$ , replacing the word "unobservable" in part (c) with the word "uncontrollable."

5.3 Given $F(s)P(s) = [k(s - 2)] / (s^2 + 1.6s + .8)$ :

a. Find the closed-loop characteristic polynomial, and use the Routh array to calculate the range of $k$ for which its roots are stable.   
b. With $k$ at its upper limit for stability, calculate the two imaginary roots by solving for the roots of the auxiliary polynomial.

5.4 Repeat Problem 5.3 for $F(s)P(s) = k / [(s + 1)^2 (s + .5)]$ .   
5.5 For $F(s)P(s) = k[(s + 1) / (s^2 + 1)(s + 4)]$ , show that the closed-loop characteristic polynomial is stable for all $k > 0$ .   
5.6 Show that, if the loop gain is $F(s)P(s) = k / [(s + 1)^2 (s - .5)]$ , the closed-loop system is unstable for all values of $k$ .   
5.7 Repeat Problem 5.6 for $F(s)P(s) = [k(s - 1)] / [(s + 2)(s - 2)].$   
5.8 In Problem 4.28 (Chapter 4), an $H^{\infty}$ design was carried out for the plant $P(s) = [2(-s + 1)] / [(s + 3)(s + 6)]$ , with the weight function $W(s) = (s + 1) / (10s + 1)$ . The compensator $F(s)$ was not proper, and we wish to design a new one, $F'(s) = [F(s)] / (Ts + 1)^2$ , that attenuates high frequencies. Over what range of values of $T$ is the closed-loop system stable?   
5.9 In Problem 4.29 (Chapter 4), an $H^{\infty}$ design was carried out for $P(s) = [2(-s + 1)] / [(s + 3)(-s + 6)]$ , with the weight function $(0.1s + 1) / (s + 1)$ . Repeat the redesign exercise of Problem 5.8.   
5.10 Sketch (by hand; do not compute) the Root Locus for the system of Problem 5.3, with $k > 0$ .   
5.11 Repeat Problem 5.10 for the system of Problem 5.4.   
5.12 Sketch the Root Locus for the system of Problem 5.5. Corroborate the truth of the assertion made there.   
5.13 Repeat Problem 5.12 for the system of Problem 5.6.   
5.14 Repeat Problem 5.12 for the system of Problem 5.7.

5.15 dc servo, simplified model For the dc servo of Problem 2.4 (Chapter 2) (with $L = 0$ ), obtain the Root Locus for pure-gain feedback. Calculate the feedback gain $k$ for a damping factor $\zeta = 0.707$ .

![](image/b084883179c8709796bd1f4de9247b09d8c0aba1ae59d219afc25081941ba17a.jpg)
