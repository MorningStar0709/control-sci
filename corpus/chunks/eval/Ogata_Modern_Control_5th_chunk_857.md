<table><tr><td>MATLAB Program 10-27</td></tr><tr><td>% Response to initial condition</td></tr><tr><td>A = [0 0 1 0;0 0 0 1;-36 36 -0.6 0.6;18 -18 0.3 -0.3];</td></tr><tr><td>B = [0;0;1;0];</td></tr><tr><td>K = [130.4444 -41.5556 23.1000 15.4185];</td></tr><tr><td>Ke = [14.4 0.6;0.3 15.7];</td></tr><tr><td>F = [0 0;0 0;1 0;0 1];</td></tr><tr><td>Aab = [1 0;0 1];</td></tr><tr><td>Abb = [-0.6 0.6;0.3 -0.3];</td></tr><tr><td>AA = [A-B*K B*K*F; zeros(2,4) Abb-Ke*Aab];</td></tr><tr><td>sys = ss(AA,eye(6),eye(6),eye(6));</td></tr><tr><td>t = 0:0.01:4;</td></tr><tr><td>y = initial(sys,[0.1;0;0;0;0.1;0.05],t);</td></tr><tr><td>x1 = [1 0 0 0 0 0]*y&#x27;;</td></tr><tr><td>x2 = [0 1 0 0 0 0]*y&#x27;;</td></tr><tr><td>x3 = [0 0 1 0 0 0]*y&#x27;;</td></tr><tr><td>x4 = [0 0 0 1 0 0]*y&#x27;;</td></tr><tr><td>e1 = [0 0 0 0 1 0]*y&#x27;;</td></tr><tr><td>e2 = [0 0 0 0 0 1]*y&#x27;;</td></tr><tr><td>subplot(3,2,1); plot(t,x1); grid; title(&#x27;Response to initial condition&#x27;),xlabel(&#x27;t (sec)&#x27;); ylabel(&#x27;x1&#x27;)</td></tr><tr><td>subplot(3,2,2); plot(t,x2); grid; title(&#x27;Response to initial condition&#x27;),xlabel(&#x27;t (sec)&#x27;); ylabel(&#x27;x2&#x27;)</td></tr><tr><td>subplot(3,2,3); plot(t,x3); grid; xlabel(&#x27;t (sec)&#x27;); ylabel(&#x27;x3&#x27;)</td></tr><tr><td>subplot(3,2,4); plot(t,x4); grid; xlabel(&#x27;t (sec)&#x27;); ylabel(&#x27;x4&#x27;)</td></tr><tr><td>subplot(3,2,5); plot(t,e1); grid; xlabel(&#x27;t (sec)&#x27;);ylabel(&#x27;e1&#x27;)</td></tr><tr><td>subplot(3,2,6); plot(t,e2); grid; xlabel(&#x27;t (sec)&#x27;); ylabel(&#x27;e2&#x27;)</td></tr></table>

A–10–14. Consider the system shown in Figure 10–51.Design both the full-order and minimum-order observers for the plant.Assume that the desired closed-loop poles for the pole-placement part are located at

$$s = - 2 + j 2 \sqrt {3}, \quad s = - 2 - j 2 \sqrt {3}$$

Assume also that the desired observer poles are located at

(a) $s = - 8 , s = - 8$ for the full-order observer   
(b) s=–8 for the minimum-order observer

Compare the responses to the initial conditions specified below:

(a) for the full-order observer:

$$x _ {1} (0) = 1, \quad x _ {2} (0) = 0, \quad e _ {1} (0) = 1, \quad e _ {2} (0) = 0$$
