# MATLAB Program 10–11

% Obtaining the state feedback gain matrix K

$$A = [ 0 \quad 1 \quad 0; 0 \quad 0 \quad 1; 0 \quad - 2 4 \quad - 1 0 ];\mathrm{B} = [ 0; 1 0; - 8 0 ];C = [ 1 \quad 0 \quad 0 ];J = \left[ - 1 + j ^ {*} 2 - 1 - j ^ {*} 2 - 5 \right];K = \operatorname{acker} (A, B, J)K =$$

1.2500 1.2500 0.19375

% Obtaining the observer gain matrix Ke

$$\mathrm{Aaa} = 0; \mathrm{Aab} = [ 1 0 ]; \mathrm{Aba} = [ 0; 0 ]; \mathrm{Abb} = [ 0 1; - 2 4 - 1 0 ]; \mathrm{Ba} = 0; \mathrm{Bb} = [ 1 0; - 8 0 ];L = [ - 1 0 \quad - 1 0 ];\mathrm{Ke} = \text { acker } (\mathrm{Abb} ^ {\prime}, \mathrm{Aab} ^ {\prime}, \mathrm{L}) ^ {\prime}\mathrm{Ke} =$$

10

-24

In the program, matrices J and L represent the desired closed-loop poles for pole placement and the desired poles for the observer, respectively. The matrices K and $\mathbf { K } _ { e }$ are obtained as

$$
\mathbf {K} = \left[ \begin{array}{c c c} 1. 2 5 & 1. 2 5 & 0. 1 9 3 7 5 \end{array} \right]

\mathbf {K} _ {e} = \left[ \begin{array}{c} 1 0 \\ - 2 4 \end{array} \right]
$$

Design step 4: We shall determine the transfer function of the observer controller. Referring to Equation (10–108), the transfer function of the observer controller can be given by

$$G _ {c} (s) = \frac {U (s)}{- Y (s)} = \frac {\text { num }}{\text { den }} = - \left[ \widetilde {\mathbf {C}} (s \mathbf {I} - \widetilde {\mathbf {A}}) ^ {- 1} \widetilde {\mathbf {B}} + \widetilde {D} \right]$$

We shall use MATLAB to calculate the transfer function of the observer controller. MATLAB Program 10–12 produces this transfer function. The result is

$$
\begin{array}{l} G _ {c} (s) = \frac {9 . 1 s ^ {2} + 7 3 . 5 s + 1 2 5}{s ^ {2} + 1 7 s - 3 0} \\ = \frac {9 . 1 (s + 5 . 6 4 2 5) (s + 2 . 4 3 4 4)}{(s + 1 8 . 6 1 1 9) (s - 1 . 6 1 1 9)} \\ \end{array}
$$

Define the system with this observer controller as System 1. Figure 10–20 shows the block diagram of System 1.

MATLAB Program 10–12   
% Determination of transfer function of observer controller
A = [0 1 0;0 0 1;0 -24 -10];
B = [0;10;-80];
Aaa = 0; Aab = [1 0]; Aba = [0;0]; Abb = [0 1;-24 -10];
Ba = 0; Bb = [10;-80];
Ka = 1.25; Kb = [1.25 0.19375];
Ke = [10;-24];
Ahat = Abb - Ke*Aab;
Bhat = Ahat*Ke + Aba - Ke*Aaa;
Fhat = Bb - Ke*Ba;
Atilde = Ahat - Fhat*Kb;
Btilde = Bhat - Fhat*(Ka + Kb*Ke);
Ctilde = -Kb;
Dtilde = -(Ka + Kb*Ke);
[num,den] = ss2tf(Atilde, Btilde, -Ctilde, -Dtilde)
num =
9.1000 73.5000 125.0000
den =
1.0000 17.0000 -30.0000

Figure 10–20 Block diagram of System 1.   
![](image/377d7146e4da98b38fb1d072de93322db47f4288ec9bc6d4a64845b2fba0e882.jpg)
