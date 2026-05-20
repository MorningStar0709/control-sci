# Solution

(a) Integrating disturbances are added to the two controlled variables (first and third outputs) by choosing

$$
C _ {d} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 0 \\ 0 & 1 \end{array} \right] \qquad B _ {d} = 0
$$

![](image/8b8fcc05a5b3fe0453595ef1a2da2e3b02bae0a402daff4618dab6bb00965dcc.jpg)  
Figure 1.8: Two manipulated inputs versus time after a step change in inlet flowrate at 10 minutes; $n _ { d } = 2$ .

The results with two integrating disturbances are shown in Figures 1.7 and 1.8. Notice that despite adding integrating disturbances to the two controlled variables, c and h, both of these controlled variables as well as the third output, T , all display nonzero offset at steady state.

(b) A third integrating disturbance is added to the second output giving

$$
C _ {d} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right] \qquad B _ {d} = 0
$$

The augmented system is not detectable with this disturbance model. The rank of $\left[ \begin{array} { l l } { I - A \ - B _ { d } } \\ { C } & { C _ { d } } \end{array} \right]$ I−A −Bd is only 5 instead of 6. The problem here is that the system level is itself an integrator, and we cannot distinguish h from the integrating disturbance added to h.

![](image/3d85e79f4d834b626ce7cf4f5daa80f64f2d51ceaf6247dccec72d31519c8c96.jpg)  
Figure 1.9: Three measured outputs versus time after a step change in inlet flowrate at 10 minutes; $n _ { d } = 3$ .

![](image/9d9de4077bdec79981edfacd3022353a398457532cd6cbcd3592182348afae4d.jpg)  
Figure 1.10: Two manipulated inputs versus time after a step change in inlet flowrate at 10 minutes; $n _ { d } = 3$ .

(c) Next we try three integrating disturbances: two added to the two controlled variables, and one added to the second manipulated variable

$$
C _ {d} = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \qquad B _ {d} = \left[ \begin{array}{c c c} 0 & 0 & 0. 1 6 5 5 \\ 0 & 0 & 9 7. 9 1 \\ 0 & 0 & - 6. 6 3 7 \end{array} \right]
$$

The augmented system is detectable for this disturbance model.

The results for this choice of three integrating disturbances are shown in Figures 1.9 and 1.10. Notice that we have zero offset in the two controlled variables, c and h, and have successfully forced the steady-state effect of the inlet flowrate disturbance entirely into the second output, T .

Notice also that the dynamic behavior of all three outputs is superior to that achieved with the model using two integrating disturbances. The true disturbance, which is a step at the inlet flowrate, is better represented by including the integrator in the outlet flowrate. With a more accurate disturbance model, better overall control is achieved. The controller uses smaller manipulated variable action and also achieves better output variable behavior. An added bonus is that steady offset is removed in the maximum possible number of outputs. -
