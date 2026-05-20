$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & - 5 & - 6 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right]
$$

By using state feedback control $u = - \mathbf { K } \mathbf { x } ,$ it is desired to have the closed-loop poles at $s = \mu _ { i }$ $( i = 1 , 2 , 3 )$ , where

$$\mu_ {1} = - 2 + j 4, \quad \mu_ {2} = - 2 - j 4, \quad \mu_ {3} = - 1 0$$

Determine the state feedback-gain matrix K with MATLAB.

MATLAB programs that generate matrix K are shown in MATLAB Programs 10–1 and 10–2. MATLAB Program 10–1 uses command acker and MATLAB Program 10–2 uses command place.

<table><tr><td>MATLAB Program 10-1</td></tr><tr><td>A = [0 1 0;0 0 0 1;-1 -5 -6];B = [0;0;1];J = [-2+j*4 -2-j*4 -10];K = acker(A,B,J)K =199 55 8</td></tr></table>

<table><tr><td>MATLAB Program 10-2</td></tr><tr><td>A = [0 1 0;0 0 0 1;-1 -5 -6];B = [0;0;1];J = [-2+j*4 -2-j*4 -10];K = place(A,B,J)place: ndigits = 15K =199.0000 55.0000 8.0000</td></tr></table>

Consider the same system as discussed in Example 10–1. It is desired that this regulator system have closed-loop poles at

$$s = - 2 + j 4, \quad s = - 2 - j 4, \quad s = - 1 0$$

The necessary state feedback gain matrix K was obtained in Example 10–1 as follows:

$$
\mathbf {K} = \left[ \begin{array}{c c c} 1 9 9 & 5 5 & 8 \end{array} \right]
$$

Using MATLAB, obtain the response of the system to the following initial condition:

$$
\mathbf {x} (0) = \left[ \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right]
$$

Response to Initial Condition: To obtain the response to the given initial condition $\mathbf { x } ( 0 )$ , we substitute $u = - \mathbf { K } \mathbf { x }$ into the plant equation to get

$$
\dot {\mathbf {x}} = (\mathbf {A} - \mathbf {B K}) \mathbf {x}, \quad \mathbf {x} (0) = \left[ \begin{array}{l} 1 \\ 0 \\ 0 \end{array} \right]
$$

To plot the response curves $( x _ { 1 }$ versus $t , x _ { 2 }$ versus t, and $x _ { 3 }$ versus $t ) _ { }$ , we may use the command initial. We first define the state-space equations for the system as follows:

$$\dot {\mathbf {x}} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} + \mathbf {I u}\mathbf {y} = \mathbf {I x} + \mathbf {I u}$$

where we included u (a three-dimensional input vector). This u vector is considered 0 in the computation of the response to the initial condition. Then we define

$$\mathrm{sys} = \mathrm{ss} (\mathrm{A} - \mathrm{BK}, \text { eye } (3), \text { eye } (3), \text { eye } (3))$$

and use the initial command as follows:

$$x = \text { initial } (\text { sys }, [ 1; 0; 0 ], t)$$

where t is the time duration we want to use, such as

$$t = 0: 0. 0 1: 4;$$

Then obtain x1, x2, and x3 as follows:

$$
\begin{array}{l} x 1 = [ 1 0 0 ] ^ {*} x ^ {\prime}; \\ x 2 = [ 0 \quad 1 \quad 0 ] ^ {*} x ^ {\prime}; \\ x 3 = [ 0 0 1 ] ^ {*} x ^ {\prime}; \\ \end{array}
$$

and use the plot command. This program is shown in MATLAB Program 10–3. The resulting response curves are shown in Figure 10–3.
