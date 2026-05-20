# 7.9.4 Dormand-Prince method

Dormand-Prince (RKDP) is a fourth-order method with fifth-order error checking. It uses an adaptive stepsize to enforce an upper bound on the integration error.

Theorem 7.9.3 — Dormand-Prince integration. Given the differential equation $\dot { \mathbf { x } } = f ( \mathbf { x } _ { k } , \mathbf { u } _ { k } )$ , this method solves for $\mathbf { x } _ { k + 1 }$ at h seconds in the future. u is assumed to be held constant between timesteps. It has the following Butcher tableau.

0 $\frac{1}{5}$ $\frac{1}{5}$ $\frac{3}{10}$ $\frac{3}{40}$ $\frac{9}{40}$ $\frac{4}{5}$ $\frac{44}{45}$ $-\frac{56}{15}$ $\frac{32}{9}$ $\frac{8}{9}$ $\frac{19372}{6561}$ $-\frac{25360}{2187}$ $\frac{64448}{6561}$ $-\frac{212}{729}$ 1 $\frac{9017}{3168}$ $-\frac{355}{33}$ $\frac{46732}{5247}$ $\frac{49}{176}$ $-\frac{5103}{18656}$ 1 $\frac{35}{384}$ 0 $\frac{500}{1113}$ $\frac{125}{192}$ $-\frac{2187}{6784}$ $\frac{11}{84}$ $\frac{35}{384}$ 0 $\frac{500}{1113}$ $\frac{125}{192}$ $-\frac{2187}{6784}$ $\frac{11}{84}$ 0 $\frac{5179}{57600}$ 0 $\frac{7571}{16695}$ $\frac{393}{640}$ $-\frac{92097}{339200}$ $\frac{187}{2100}$ $\frac{1}{40}$

The first row of coefficients below the table divider gives the fifth-order accurate solution. The second row gives an alternative solution which, when subtracted from the first solution, gives the error estimate.

Here’s a reference implementation.   
```cpp
#include <algorithm>
#include <array>
#include <cmath>

#include <Eigen/Core>

/// Performs adaptive Dormand-Prince integration of dx/dt = f(x, u) for dt.
/// @param f The function to integrate. It must take two arguments x and u.
/// @param x The initial value of x.
/// @param u The value u held constant over the integration period.
/// @param dt The time over which to integrate.
/// @param max_error The maximum acceptable truncation error. Usually a small number like 1e-6.
template <typename F, typename T, typename U>
T rkdp(F&& f, T x, U u, double dt, double max_error = 1e-6) {
    // See https://en.wikipedia.org/wiki/Dormand%E2%80%93Prince_method for the
    // Butcher tableau the following arrays came from.

constexpr int DIM = 7;
