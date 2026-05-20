MATLAB Program 10–14   
% Determination of transfer function of observer controller.
A = [0 1 0;0 0 0 1;0 -24 -10];
B = [0;10;-80];
Aaa = 0; Aab = [1 0]; Aba = [0;0]; Abb = [0 1;-24 -10];
Ba = 0; Bb = [10;-80];
Ka = 1.25; Kb = [1.25 0.19375];
Ke = [-1;6.25];
Ahat = Abb - Ke*Aab;
Bhat = Ahat*Ke + Aba - Ke*Aaa;
Fhat = Bb - Ke*Ba;
Atilde = Ahat - Fhat*Kb;
Btilde = Bhat - Fhat*(Ka + Kb*Ke);
Ctilde = -Kb;
Dtilde = -(Ka + Kb*Ke);
[num,den] = ss2tf(Atilde,Btilde,-Ctilde,-Dtilde)
num =
    1.2109 11.2125 25.3125
den =
    1.0000 6.0000 2.1406

Notice that this is a stable controller. Define the system with this observer controller as System 2. We shall proceed to obtain the response of System 2 to the given initial condition:

$$
\mathbf {x} (0) = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right], \qquad \mathbf {e} (0) = \left[ \begin{array}{c} 1 \\ 0 \end{array} \right]
$$

By substituting $u = - \mathbf { K } \widetilde { \mathbf { x } }$ into the state-space equation for the plant, we obtain

$$
\begin{array}{l} \dot {\mathbf {x}} = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \widetilde {\mathbf {x}} = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \left[ \begin{array}{c} x _ {a} \\ \widetilde {\mathbf {x}} _ {b} \end{array} \right] = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \left[ \begin{array}{c} x _ {a} \\ \mathbf {x} _ {b} - \mathbf {e} \end{array} \right] \\ = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \left\{\mathbf {x} - \left[ \begin{array}{l} 0 \\ \mathbf {e} \end{array} \right] \right\} = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \mathbf {x} + \mathbf {B} \left[ K _ {a} - \mathbf {K} _ {b} \right] \left[ \begin{array}{l} 0 \\ \mathbf {e} \end{array} \right] \tag {10-110} \\ \end{array}
$$

The error equation for the minimum-order observer is

$$\dot {\mathbf {e}} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \mathbf {e} \tag {10-111}$$

By combining Equations (10–110) and (10–111), we get

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} \\ \dot {\mathbf {e}} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {B K} & \mathbf {B K} _ {b} \\ \mathbf {0} & \mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \mathbf {e} \end{array} \right]
$$

with the initial condition
