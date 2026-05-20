$$\mathbf {y} = \mathbf {C} (\mathbf {A z} + \mathbf {B u}) = \mathbf {C A z} + \mathbf {C B u} \tag {5-60}$$

The solution of Equations (5–58) and (5–60), rewritten here

$$\dot {\mathbf {z}} = \mathbf {A} \mathbf {z} + \mathbf {B} u\mathbf {y} = \mathbf {C A z} + \mathbf {C B u}$$

where gives the response of the system to a given initial condi-B = x(0) and u = 1(t), tion. MATLAB commands to obtain the response curves (output curves y1 versus t, y2 versus t, ... , ym versus t) are shown next for two cases:

Case A. When the time vector t is not specified (that is, the time vector t is to be determined automatically by MATLAB):

% Specify matrices A, B, and C

$$[ y, z, t ] = \operatorname{step} (A, B, C ^ {*} A, C ^ {*} B);\mathrm{y} 1 = [ 1 \quad 0 \quad 0 \dots 0 ] ^ {*} \mathrm{y} ^ {\prime};\mathrm{y} 2 = [ 0 \quad 1 \quad 0 \dots 0 ] ^ {*} \mathrm{y} ^ {\prime};\mathrm{ym} = [ 0 0 0 \dots 1 ] ^ {*} \mathrm{y} ^ {\prime};\operatorname{plot} (t, y 1, t, y 2, \dots , t, y m)$$

Case B. When the time vector t is specified:

t = 0: Δt: tp;
% Specify matrices A, B, and C
[y,z,t] = step(A,B,C*A,C*B,1,t)
y1 = [1 0 0 ... 0]*y';
y2 = [0 1 0 ... 0]*y';
.
.
.
ym = [0 0 0 ... 1]*y';
plot(t,y1,t,y2, ..., t,ym)

EXAMPLE 5–9 Obtain the response of the system subjected to the given initial condition.

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 1 0 & - 5 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right], \quad \left[ \begin{array}{c} x _ {1} (0) \\ x _ {2} (0) \end{array} \right] = \left[ \begin{array}{c} 2 \\ 1 \end{array} \right]
$$

or

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x}, \quad \mathbf {x} (0) = \mathbf {x} _ {0}$$

Obtaining the response of the system to the given initial condition resolves to solving the unit-step response of the following system:

$$\dot {\mathbf {z}} = \mathbf {A} \mathbf {z} + \mathbf {B} u\mathbf {x} = \mathbf {A z} + \mathbf {B u}$$

where

$$\mathbf {B} = \mathbf {x} (0), \quad u = 1 (t)$$

Hence a possible MATLAB program for obtaining the response may be given as shown in MATLAB Program 5–15. The resulting response curves are shown in Figure 5–32.
