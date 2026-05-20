# MATLAB Program 5–15

t = 0:0.01:3;
A = [0 1;-10 -5];
B = [2;1];
[x,z,t] = step(A,B,A,B,1,t);
x1 = [1 0]*x';
x2 = [0 1]*x';
plot(t,x1,'x',t,x2,'-')
grid
title('Response to Initial Condition')
xlabel('t Sec')
ylabel('State Variables x1 and x2')
gtext('x1')
gtext('x2')

Figure 5–32 Response of system in Example 5–9 to initial condition.   
![](image/cf40f5b5acb01a944ce1f10ceff20dc092d7e254138c7e04d084896c3343930c.jpg)

<details>
<summary>line</summary>

| t Sec | x1 | x2 |
| --- | --- | --- |
| 0.0 | 2.0 | 1.0 |
| 0.5 | 1.0 | -2.5 |
| 1.0 | 0.5 | -1.0 |
| 1.5 | 0.0 | 0.0 |
| 2.0 | 0.0 | 0.0 |
| 2.5 | 0.0 | 0.0 |
| 3.0 | 0.0 | 0.0 |
</details>

For an illustrative example of how to use Equations (5–58) and (5–60) to find the response to the initial condition, see Problem A–5–16.

Obtaining Response to Initial Condition by Use of Command Initial. If the system is given in the state-space form, then the following command

$\mathsf { i n i t i a l } ( \mathsf { A } , \mathsf { B } , \mathsf { C } , \mathsf { D } , [ \mathsf { i n i t i a l \ c o n d i t i o n } ] , \mathsf { t } )$

will produce the response to the initial condition.

Suppose that we have the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u, \quad \mathbf {x} (0) = \mathbf {x} _ {0}y = \mathbf {C x} + D u$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 0 & - 5 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 0 \end{array} \right], \quad \mathbf {C} = [ 0 \quad 0 ], \quad D = 0

\mathbf {x} _ {0} = \left[ \begin{array}{c} 2 \\ 1 \end{array} \right]
$$

Then the command “initial” can be used as shown in MATLAB Program 5–16 to obtain the response to the initial condition. The response curves $x _ { 1 } ( t )$ and $x _ { 2 } ( t )$ are shown in Figure 5–33. They are the same as those shown in Figure 5–32.

<table><tr><td>MATLAB Program 5-16</td></tr><tr><td>t = 0:0.05:3;A = [0 1;-10 -5];B = [0;0];C = [0 0];D = [0];[y,x] = initial(A,B,C,D,[2;1],t);x1 = [1 0]*x&#x27;;x2 = [0 1]*x&#x27;;plot(t,x1,&#x27;o&#x27;,t,x1,t,x2,&#x27;x&#x27;,t,x2)gridtitle(&#x27;Response to Initial Condition&#x27;)xlabel(&#x27;t Sec&#x27;)ylabel(&#x27;State Variables x1 and x2&#x27;)gtext(&#x27;x1&#x27;)gtext(&#x27;x2&#x27;)</td></tr></table>

![](image/7740809bb7da0e75e3197547c6ef4e02886e2690532a4b9112316a4ea8f8e6b0.jpg)

<details>
<summary>line</summary>

| t Sec | x1 | x2 |
| --- | --- | --- |
| 0.0 | 2.0 | 1.0 |
| 0.5 | 1.0 | -2.8 |
| 1.0 | 0.5 | -1.0 |
| 1.5 | 0.0 | 0.0 |
| 2.0 | 0.0 | 0.0 |
| 2.5 | 0.0 | 0.0 |
| 3.0 | 0.0 | 0.0 |
</details>

Figure 5–33 Response curves to initial condition.
