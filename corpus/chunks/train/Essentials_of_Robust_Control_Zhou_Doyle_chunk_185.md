<table><tr><td>r</td><td>0</td><td>1</td><td>2</td><td>3</td></tr><tr><td> $\|G - G_r\|_\infty$ </td><td>1.9997</td><td>1.9983</td><td>1.9933</td><td>1.9845</td></tr><tr><td>Bounds:  $2\sum_{i=r+1}^{4}\sigma_i$ </td><td>7.9744</td><td>5.9748</td><td>3.9772</td><td>1.9845</td></tr><tr><td> $2\sigma_{r+1}$ </td><td>1.9996</td><td>1.9976</td><td>1.9926</td><td>1.9845</td></tr></table>

The balanced realization and truncation can be done using the following Matlab commands:

$\gg [ \mathbf { G _ { b } } , \mathbf { s i g } ] = \mathbf { s y s b a l } ( \mathbf { G } )$ ; % find a balanced realization $G _ { b }$ and the Hankel singular values sig.   
$\gg \bf G _ { \mathrm { r } } = \ s t r u n c ( G _ { b } , 2 )$ ; % truncate to the second-order.

Related MATLAB Commands: reordsys, resid, Hankmr
