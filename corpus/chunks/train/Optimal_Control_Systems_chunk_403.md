![](image/fad83e1b0919bdd1937f1b1f0e6963f2c910d5aa4f6b5376bcc6a3a0e329a023.jpg)

<details>
<summary>text_image</summary>

R2
γ-
u = -1
u=0
A2(x10,x20)
u=+1
u=0
x2
R1
0
B
u=0
A4(x10,x20)
u=-1
D
u=0
C
u=+1
γ+
R3
R4
</details>

Figure 7.22 Fuel-Optimal Control Sequences

1. The $R_{1}(R_{3})$ is the region to the right (left) of $\gamma$ curve and for the positive (negative) values of $x_{2}$ .   
2. The $R_{2}(R_{4})$ is the region to the left (right) of $\gamma$ curve and for the positive (negative) values of $x_{2}$ .

Now, depending upon the initial position of the system, we have a particular optimal control sequence (see Figure 7.22).

1. $\gamma_{+}$ and $\gamma_{-}$ Curves: If the initial condition $(x_{10}, x_{20}) \in \gamma_{+}(\gamma_{-})$ , then the control $u(t) = +1(u(t) = -1)$ .   
2. $R_2$ and $R_4$ Regions: If the initial condition is $(x_{10}, x_{20}) \in R_4$ , then the control sequence $\{0, +1\}$ forces the system to $(0, 0)$ , through $A_4$ to $B$ , and then to $0$ , and hence is fuel-optimal. Although the control sequence $\{-1, 0, +1\}$ also drives the system to origin through $A_4CD0$ , it is not optimal. Similarly, in the region $R_2$ , the optimal control sequence is $\{0, -1\}$ .   
3. $R_{1}$ and $R_{3}$ Regions: Let us position the system at $A_{1}(x_{10}, x_{20})$ in the region $R_{1}$ , as shown in Figure 7.23. As seen, staying

![](image/b2d333327495c8e6d86191c19659ef6e40a992b92ba8d2bc721ab856882b7830.jpg)

<details>
<summary>text_image</summary>

R2
γ-
x2
R1
A1(x10,x20)
u=-1
ε²/8
B
0
D
C
u=0
-ε/2
E
R3
A3(x10,x20)
R4
γ+
γ+
</details>

Figure 7.23 $\epsilon$ -Fuel-Optimal Control

in region $R_{1}$ there is no way one can drive the system at $A_{1}$ to origin, as the control sequence $u^{*}(t) = 0$ drives the system towards right (or away from the origin).

Thus, there is no fuel-optimal solution for the system for region $R_{1}$ . However, given any $\epsilon > 0$ , there is a control sequence $\{-1, 0, +1\}$ , which forces the system to origin. Then,

the fuel consumed is

$$\boxed {J _ {\epsilon} = \left| x _ {2 0} \right| + \left| \frac {- \epsilon}{2} \right| + \left| \frac {\epsilon}{2} \right| = \left| x _ {2 0} \right| + \epsilon = J ^ {*} + \epsilon \geq J ^ {*}.} \tag {7.3.26}$$
