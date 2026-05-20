# (3) 边界条件的离散化

时间取 $1 \leqslant j \leqslant nt$ ，根据边界条件，分为以下4种情况求 $y(i,j)$ ：

① $1 \leqslant i \leqslant 2$ ，根据边界条件求 $y(i, j)$ 。

由边界条件式（13.41）可知 $y(0,t) = 0$ ， $y_{x}(0,t) = 0$ 。由边界条件式 $y(0,t) = 0$ ，可得 $y(1,j) = 0$ ，由于 $y_{x}(0,t) = \frac{y(2,j) - y(1,j)}{dx}$ ，则由边界条件式 $y_{x}(0,t) = 0$ ，可得 $y(2,j) = 0$ ，即

$$y (1, j) = y (2, j) = 0 \tag {13.50}$$

② $3 \leqslant i \leqslant nx - 2$ ，求 $y(i, j)$ 。

由式（13.38）可知， $\rho\ddot{z}(x)=-\mathrm{EI}z_{xxxx}(x)$ ，展开，得

$$i \cdot \mathrm{d} x \cdot \ddot {\theta} (t) + \frac {y (i , j) - 2 y (i , j - 1) + y (i , j - 2)}{T ^ {2}} = - \frac {\mathrm{EI}}{\rho} y _ {x x x x} (x, t)\ddot {\theta} (t) = \frac {\theta (j) - 2 \theta (j - 1) + \theta (j - 2)}{T ^ {2}}\dot {y} (x, t) = \frac {y (i , j - 1) - y (i , j - 2)}{T}y _ {x x x x} (x, t) = \frac {y (i + 2 , j - 1) - 4 y (i + 1 , j - 1) + 6 y (i , j - 1) - 4 y (i - 1 , j - 1) + y (i - 2 , j - 1)}{\mathrm{d} x ^ {4}}$$

则

$$y (i, j) = T ^ {2} \left(- i \cdot \mathrm{d} x \cdot \ddot {\theta} (t) - \frac {\mathrm{EI}}{\rho} y _ {x x x x} (x, t)\right) + 2 y (i, j - 1) - y (i, j - 2) \tag {13.51}$$

③ i=nx-1，根据边界条件求 $y(nx-1,j)$ 。

由边界条件式（13.42）可知 $y_{xx}(L,t) = 0$ ，则

$$
\begin{array}{l} y _ {x x} (L, t) = \frac {y _ {x} (n x + 1 , j - 1) - y _ {x} (n x , j - 1)}{\mathrm{d} x} \\ = \frac {y (n x + 1 , j - 1) - 2 y (n x , j - 1) + y (n x - 1 , j - 1)}{\mathrm{d} x ^ {2}} = 0 \\ \end{array}
$$

即

$$y (n x + 1, j - 1) = 2 y (n x, j - 1) - y (n x - 1, j - 1) \tag {13.52}$$

以 $(nx-1,j-1)$ 为中心展开得

$$y _ {x x x x} (n x - 1, j - 1) = \frac {y (n x + 1 , j - 1) - 4 y (n x , j - 1) + 6 y (n x - 1 , j - 1) - 4 y (n x - 2 , j - 1) + y (n x - 3 , j - 1)}{\mathrm{d} x ^ {4}}$$

将式（13.52）代入上式得

$$y _ {x x x x} (n x - 1, j - 1) = \frac {- 2 y (n x , j - 1) + 5 y (n x - 1 , j - 1) - 4 y (n x - 2 , j - 1) + y (n x - 3 , j - 1)}{\mathrm{d} x ^ {4}} \tag {13.53}$$

将上式代入（13.51）式，取 $i = nx - 1$ ，可求出

$$y (n x - 1, j) = T ^ {2} \left(- (n x - 1) \cdot \mathrm{d} x \cdot \ddot {\theta} (t) - \frac {\mathrm{EI}}{\rho} y _ {x x x x} (n x - 1, j - 1)\right) + 2 y (n x - 1, j - 1) - y (n x - 1, j - 2) \tag {13.54}$$

④ i = nx ，根据边界条件求 $y(nx, j)$ 。

差分展开得

$$y _ {x x x} (L, t) = \frac {y (n x + 1 , j - 1) - 3 y (n x , j - 1) + 3 y (n x - 1 , j - 1) - y (n x - 2 , j - 1)}{\mathrm{d} x ^ {3}}$$

考虑式（13.52），可得

$$y _ {x x x} (L, t) = \frac {- y (n x , j - 1) + 2 y (n x - 1 , j - 1) - y (n x - 2 , j - 1)}{\mathrm{d} x ^ {3}}$$

由式（13.40）即 $F = m\ddot{z}(L) - \mathrm{EI}z_{xxx}(L)$ 可知 $\operatorname{EI}y_{xxx}(L,t) + F = m\big(L\ddot{\theta}(t) + \ddot{y}(L,t)\big)$ ，以 $(nx,j - 1)$ 为中心展开得

$$\frac {\mathrm{EI} y _ {x x x} (L , t) + F}{m} = L \ddot {\theta} + \frac {y (n x , j) - 2 y (n x , j - 1) + y (n x , j - 2)}{T ^ {2}}$$

则可得

$$y (n x, j) = T ^ {2} \times \left(- L \ddot {\theta} + \frac {\mathrm{EI} y _ {x x x} (L , t) + F}{m}\right) + 2 y (n x, j - 1) - y (n x, j - 2) \tag {13.55}$$
