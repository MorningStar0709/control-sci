Now take the Laplace transform. Because the Laplace transform is a linear operawe can take the Laplace transform of each term individually. Based on table E.1, $\textstyle { \frac { d \omega } { d t } }$ becomes $s \omega$ and $\omega ( t )$ and $V ( t )$ become $\omega ( s )$ and $V ( s )$ respectively (the parenthetical notation has been dropped for clarity).

$$s \omega = - \frac {K _ {t}}{J R K _ {v}} \omega + \frac {K _ {t}}{J R} V \tag {E.13}$$

Solve for the transfer function $\textstyle H ( s ) = { \frac { \omega } { V } }$ .

$$s \omega = - \frac {K _ {t}}{J R K _ {v}} \omega + \frac {K _ {t}}{J R} V\left(s + \frac {K _ {t}}{J R K _ {v}}\right) \omega = \frac {K _ {t}}{J R} V\frac {\omega}{V} = \frac {\frac {K _ {t}}{J R}}{s + \frac {K _ {t}}{J R K _ {v}}}$$

That gives us a pole at $- \frac { K _ { t } } { J R K _ { v } }$ , which is actually stable. Notice that there is only one pole.

First, we’ll use a simple P controller.

$$V = K _ {p} (\omega_ {g o a l} - \omega)$$

Substitute this controller into equation (E.13).

$$s \omega = - \frac {K _ {t}}{J R K _ {v}} \omega + \frac {K _ {t}}{J R} K _ {p} (\omega_ {g o a l} - \omega)$$

Solve for the transfer function $\begin{array} { r } { H ( s ) = \frac { \omega } { \omega _ { g o a l } } } \end{array}$

$$s \omega = - \frac {K _ {t}}{J R K _ {v}} \omega + \frac {K _ {t} K _ {p}}{J R} (\omega_ {g o a l} - \omega)s \omega = - \frac {K _ {t}}{J R K _ {v}} \omega + \frac {K _ {t} K _ {p}}{J R} \omega_ {g o a l} - \frac {K _ {t} K _ {p}}{J R} \omega\left(s + \frac {K _ {t}}{J R K _ {v}} + \frac {K _ {t} K _ {p}}{J R}\right) \omega = \frac {K _ {t} K _ {p}}{J R} \omega_ {g o a l}\frac {\omega}{\omega_ {g o a l}} = \frac {\frac {K _ {t} K _ {p}}{J R}}{\left(s + \frac {K _ {t}}{J R K _ {v}} + \frac {K _ {t} K _ {p}}{J R}\right)}$$

This has a pole at $\begin{array} { r } { - \left( \frac { K _ { t } } { J R K _ { v } } + \frac { K _ { t } K _ { p } } { J R } \right) } \end{array}$ KtKp Assuming that that quantity is negative (i.e., we are stable), that pole corresponds to a time constant of $\frac { 1 } { \frac { K _ { t } } { J R K _ { v } } + \frac { K _ { t } K _ { p } } { J R } }$ . tJRKv

As can be seen above, a flywheel has a single pole. It therefore only needs a single pole controller to place that pole anywhere on the real axis.
