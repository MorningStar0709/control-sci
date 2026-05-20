# Example B.2

Plot $y _ { 1 } ( t ) = 2$ sin 3t and $y _ { 2 } ( t ) = - 4$ cos 8t for $0 \leq t \leq 4 \mathrm { s } .$

>> t = linspace(0,4,200); % define time vector t from 0 to 4 with 200 points
>> y1 = 2*sin(3*t); % define vector $y_{1}(t)=2\sin3t$ (size is 1x200)
>> y2 = -4*cos(8*t); % define vector $y_{2}(t)=-4\cos8t$ (size is 1x200)
>> plot(t,y1,t,y2) % plot vectors y1 vs. t and y2 vs. t

In this simple example, the two x–y pairs (t,y1) and $( \ t , \ y 2 )$ are both $\mathtt { 1 } \mathtt { x } 2 0 0$ row vectors. The only dimensional requirement for the plot command is that the x–y vector pairs must have the same dimensions.

Finally, the user may use logarithmic-scaled axes using the following commands:

```erlang
>> semilogx(x,y)    % plot vectors y vs. x with a logarithmic scale for the x-axis
>> semilogy(x,y)    % plot vectors y vs. x with a logarithmic scale for the y-axis
>> loglog(x,y)    % plot vectors y vs. x with logarithmic scales for both axes 
```

These plotting commands have the same syntax rules as the plot command.
