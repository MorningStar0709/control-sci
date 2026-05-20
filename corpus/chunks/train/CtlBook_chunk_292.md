# 9.2 System Type and Steady State Error

In this section, we will examine the error we have computed in control systems at the summing junction on the left side of the closed loop negative feedback system (Figure 9.1). Since in control systems, we most often consider $H ( s ) = 1$ , the error $( \breve { E } ( s ) = X ( s ) - H \bar { ( } s ) Y ( s ) \ )$ is a direct comparison between the input and the output. In some applications, (consider a medical device or a ight control system for an interplanetary spacecraft) it is critical to eliminate error. In others (consider a temperature control system for buildings) an error of one or two percent might not matter.

Steady State refers to the error between input and output as t → ∞. In practical applications, what do we mean by innite time? We really mean the time that all transient terms become of insignicant magnitude. For example, if

$$y _ {1} (t) = 5 e ^ {- 0. 1 t}$$

then for t = 85sec, $y _ { 1 } ( 8 5 ) = 0 . 0 0 1 ;$ a very small value compared to the amplitude 5. For $t = 8 5$ , the transient due to $y _ { 1 } ( t )$ is $\ " { \mathrm { o v e r } } ^ { , \bullet } .$ . On the other hand, for

$$y _ {2} (t) = 5 e ^ {- 2 0 t}$$

then for $t = 0 . 4 2 5 \mathrm { s e c }$ , $y _ { 2 } ( 0 . 4 2 5 ) = 0 . 0 0 1$ . For $y _ { 2 } ( t )$ , 0.43 sec is essentially innite. Thus innite time depends on the real part of the system's closed loop poles.

It turns out that a key variable in studying the magnitude of error in a closed loop negative feedback system is the number of poles at the origin in the loop gain $( C ( s ) P ( s ) H ( s )$ of Figure 9.1). We call this number the system type. The error also critically depends on the kind of input. Some inputs are simply easier to track than others.

Some key points about system type and steady state error:

 System type is $\#$ of poles at origin: $\frac { 1 } { s ^ { n } }$ in the controller/plant   
 Input of amplitude A can be $\left\{ \begin{array} { l l } { \mathrm { S t e p } } & { \frac { A } { s } } \\ { } & { } \\ { \mathrm { R a m p } } & { \frac { A } { s ^ { 2 } } } \\ { } & { } \\ { \mathrm { P a r a b o l a } } & { \frac { A } { s ^ { 3 } } } \end{array} \right.$   
 If input is $\textstyle { \frac { A } { s ^ { n } } }$ , and your controller has at least n type, then there will be zero steady state error.
