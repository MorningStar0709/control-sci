Chapter 14 first considers an $\mathcal { H } _ { \infty }$ control problem with the generalized plant $G ( s )$ as given in Chapter 13 but with some additional simplifications: $R _ { 1 } = I , R _ { 2 } = I $ , $D _ { 1 2 } ^ { * } C _ { 1 } = 0$ , and $B _ { 1 } D _ { 2 1 } ^ { * } = 0$ . We show that there exists an admissible controller such that $\| T _ { z w } \| _ { \infty } < \gamma$ if and only if the following three conditions hold:

(i) $H _ { \infty } \in$ dom(Ric) and $X _ { \infty } : = \operatorname { R i c } ( H _ { \infty } ) > 0$ , where

$$
H _ {\infty} := \left[ \begin{array}{c c} A & \gamma^ {- 2} B _ {1} B _ {1} ^ {*} - B _ {2} B _ {2} ^ {*} \\ - C _ {1} ^ {*} C _ {1} & - A ^ {*} \end{array} \right];
$$

(ii) $J _ { \infty } \in \mathrm { d o m } ( \mathrm { R i c } )$ and $Y _ { \infty } : = \operatorname { R i c } ( J _ { \infty } ) > 0$ , where

$$
J _ {\infty} := \left[ \begin{array}{c c} A ^ {*} & \gamma^ {- 2} C _ {1} ^ {*} C _ {1} - C _ {2} ^ {*} C _ {2} \\ - B _ {1} B _ {1} ^ {*} & - A \end{array} \right];
$$

(iii) $\rho ( X _ { \infty } Y _ { \infty } ) < \gamma ^ { 2 }$ .

Moreover, an admissible controller such that $\| T _ { z w } \| _ { \infty } < \gamma$ is given by

$$
K _ {\mathrm{sub}} = \left[ \begin{array}{c c} \hat {A} _ {\infty} & - Z _ {\infty} L _ {\infty} \\ \hline F _ {\infty} & 0 \end{array} \right]
$$

where

$$\hat {A} _ {\infty} := A + \gamma^ {- 2} B _ {1} B _ {1} ^ {*} X _ {\infty} + B _ {2} F _ {\infty} + Z _ {\infty} L _ {\infty} C _ {2}F _ {\infty} := - B _ {2} ^ {*} X _ {\infty}, \quad L _ {\infty} := - Y _ {\infty} C _ {2} ^ {*}, \quad Z _ {\infty} := (I - \gamma^ {- 2} Y _ {\infty} X _ {\infty}) ^ {- 1}.$$

We then consider further the general $\mathcal { H } _ { \infty }$ control problem. We indicate how various assumptions can be relaxed to accommodate other more complicated problems, such as singular control problems. We also consider the integral control in the $\mathcal { H } _ { 2 }$ and $\mathcal { H } _ { \infty }$ theory and show how the general $\mathcal { H } _ { \infty }$ solution can be used to solve the $\mathcal { H } _ { \infty }$ filtering problem.

Chapter 15 considers the design of reduced-order controllers by means of controller reduction. Special attention is paid to the controller reduction methods that preserve the closed-loop stability and performance. Methods are presented that give sufficient conditions in terms of frequency-weighted model reduction.

Chapter 16 first solves a special $\mathcal { H } _ { \infty }$ minimization problem. Let $P = \tilde { M } ^ { - 1 } \tilde { N }$ be a normalized left coprime factorization. Then we show that
