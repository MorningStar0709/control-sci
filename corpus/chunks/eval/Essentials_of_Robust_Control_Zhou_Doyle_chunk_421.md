# Illustrative MATLAB Commands:

$\mathbf { b _ { p , k } } = \mathbf { e m a r g i n } ( \mathbf { P } , \mathbf { K } ) ;$ % given P and K, compute $b _ { P , K }$   
$\mathbf { \boldsymbol { \gg } } \left[ \mathbf { K } _ { \mathrm { o p t } } , \mathbf { b _ { p , k } } \right] = \mathbf { n c f s y n } ( \mathbf { P } , \mathbf { 1 } )$ ; % find the optimal controller $K _ { \mathrm { o p t } }$   
$\begin{array} { r } { \gg [ { \bf K } _ { \mathrm { s u b } } , \mathbf { b } _ { \mathbf { p } , \mathbf { k } } ] = \mathbf { n c f s y n } ( \mathbf { P } , \mathbf { 2 } ) ; } \end{array}$ % find a suboptimal controller $K _ { s u b }$
