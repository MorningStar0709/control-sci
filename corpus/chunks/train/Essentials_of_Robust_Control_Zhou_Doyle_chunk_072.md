# Illustrative MATLAB Commands:

G=pck([], [], [], 10) % create a constant system matrix   
[y, x, t]=step(A, B, C, D, Iu) % Iu=i (step response of the ith channel)   
$\gg [ \mathbf { y } , \mathbf { x } , \mathbf { t } ] \mathrm { = i n i t i a l } ( \mathbf { A } , \mathbf { B } , \mathbf { C } , \mathbf { D } , \mathbf { x _ { 0 } } )$ % initial response with initial condition x0   
$\gg [ \mathbf { y } , \mathbf { x } , \mathbf { t } ] { = } \mathbf { i m p u l s e } ( \mathbf { A } , \mathbf { B } , \mathbf { C } , \mathbf { D } , \mathbf { I u } )$ % impulse response of the Iuth channel   
[y,x]=lsim(A,B,C,D,U,T) % U is a length(T ) × column(B) matrix input; $T$ is the sampling points.

Related MATLAB Commands: minfo, trsp, cos tr, sin tr, siggen
