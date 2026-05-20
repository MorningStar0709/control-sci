$$
\begin{array}{l} \dot {x} _ {1} ^ {*} (t) = + \left(\frac {\partial \mathcal {H}}{\partial \lambda_ {1}}\right) _ {*} = x _ {2} ^ {*} (t) \\ \dot {x} _ {2} ^ {*} (t) = + \left(\frac {\partial \mathcal {H}}{\partial \lambda_ {2}}\right) _ {*} = - \lambda_ {2} ^ {*} (t) \\ \dot {\lambda} _ {1} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial x _ {1}}\right) _ {*} = 0 \\ \dot {\lambda} _ {2} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial x _ {2}}\right) _ {*} = - \lambda_ {1} ^ {*} (t). \tag {2.7.53} \\ \end{array}
$$

Solving the previous equations, we have the optimal state and costate as

$$
\begin{array}{l} x _ {1} ^ {*} (t) = \frac {C _ {3}}{6} t ^ {3} - \frac {C _ {4}}{2} t ^ {2} + C _ {2} t + C _ {1} \\ x _ {2} ^ {*} (t) = \frac {C _ {3}}{2} t ^ {2} - C _ {4} t + C _ {2} \\ \lambda_ {1} ^ {*} (t) = C _ {3} \\ \lambda_ {2} ^ {*} (t) = - C _ {3} t + C _ {4}. \tag {2.7.54} \\ \end{array}
$$

\- Step 5: Obtain the optimal control from

$$u ^ {*} (t) = - \lambda_ {2} ^ {*} (t) = C _ {3} t - C _ {4} \tag {2.7.55}$$

![](image/9f1585c506eff9a83e1954e78306c7880dc18a500285d0fce0e2a8363e2f3aa8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Optimal Controller"] -->|u*(t)| B["∫"]
    B -->|x₂*(t)| C["∫"]
    C -->|x₁*(t)| D["End"]
```
</details>

Figure 2.10 Optimal Controller for Example 2.12

where, $C_1, C_2, C_3$ , and $C_4$ are constants evaluated using the given boundary conditions (2.7.48). These are found to be

$$C _ {1} = 1, \quad C _ {2} = 2, \quad C _ {3} = 3, \quad \text { and } \quad C _ {4} = 4. \tag {2.7.56}$$

Finally, we have the optimal states, costates and control as

$$x _ {1} ^ {*} (t) = 0. 5 t ^ {3} - 2 t ^ {2} + 2 t + 1,x _ {2} ^ {*} (t) = 1. 5 t ^ {2} - 4 t + 2,\lambda_ {1} ^ {*} (t) = 3,\lambda_ {2} ^ {*} (t) = - 3 t + 4,u ^ {*} (t) = 3 t - 4. \tag {2.7.57}$$

The system with the optimal controller is shown in Figure 2.10.

The solution for the set of differential equations (2.7.53) with the boundary conditions (2.7.48) for Example 2.12 using Symbolic Toolbox of the MATLAB $^{©}$ , Version 6, is shown below.

```matlab
******************
%% Solution Using Symbolic Toolbox (STB) in
%% MATLAB Version 6.0
%%
S=dsolve('Dx1=x2,Dx2=-lambda2,Dlambda1=0,Dlambda2=-lambda1,...
x1(0)=1,x2(0)=2,x1(2)=1,x2(2)=0')
S.x1
S.x2
S.lambda1
S.lambda2

S =
    lambda1: [1x1 sym]
    lambda2: [1x1 sym]
    x1: [1x1 sym]
    x2: [1x1 sym]

S.x1

ans = 
```

2.7 Variational Approach to Optimal Control Systems
