$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

and the control signal is given by

$$u = - \mathbf {K x}$$

The feedback gain matrix K that forces the eigenvalues of A-BK to be $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n }$ (desired values) can be determined by the following steps (if $\mu _ { i }$ is a complex eigenvalue, then its conjugate must also be an eigenvalue of $\mathbf { A } - \mathbf { B } \mathbf { K } )$ :

Step 1: Check the controllability condition for the system. If the system is completely state controllable, then use the following steps:

Step 2: From the characteristic polynomial for matrix A, that is,

$$\left| s \mathbf {I} - \mathbf {A} \right| = s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n - 1} s + a _ {n}$$

determine the values of $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$

Step 3: Determine the transformation matrix T that transforms the system state equation into the controllable canonical form. (If the given system equation is already in the controllable canonical form, then T=I.) It is not necessary to write the state equation in the controllable canonical form. All we need here is to find the matrix T. The transformation matrix T is given by Equation (10–4), or

$$\mathbf {T} = \mathbf {M W}$$

where M is given by Equation (10–5) and W is given by Equation (10–6).

Step 4: Using the desired eigenvalues (desired closed-loop poles), write the desired characteristic polynomial:

$$(s - \mu_ {1}) (s - \mu_ {2}) \dots (s - \mu_ {n}) = s ^ {n} + \alpha_ {1} s ^ {n - 1} + \dots + \alpha_ {n - 1} s + \alpha_ {n}$$

and determine the values of $\alpha _ { 1 } , \alpha _ { 2 } , \ldots , \alpha _ { n } .$ .

Step 5: The required state feedback gain matrix K can be determined from Equation (10–13), rewritten thus:

$$\mathbf {K} = \left[ \alpha_ {n} - a _ {n} \mid \alpha_ {n - 1} - a _ {n - 1} \mid \dots \mid \alpha_ {2} - a _ {2} \mid \alpha_ {1} - a _ {1} \right] \mathbf {T} ^ {- 1}$$

Determination of Matrix K Using Direct Substitution Method. If the system is of low order $( n \leq 3 )$ , direct substitution of matrix K into the desired characteristic polynomial may be simpler. For example, if n=3, then write the state feedback gain matrix K as

$$
\mathbf {K} = \left[ \begin{array}{c c c} k _ {1} & k _ {2} & k _ {3} \end{array} \right]
$$

Substitute this K matrix into the desired characteristic polynomial $| s \mathbf { I } - \mathbf { A } + \mathbf { B } \mathbf { K } |$ and∑ equate it to $( s - \mu _ { 1 } ) ( s - \mu _ { 2 } ) ( s - \mu _ { 3 } )$ , or
