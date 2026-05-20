# Example B.1

Plot y(t) = 2 sin 3t for 0 ≤ t ≤ 6 s.   
```matlab
>> t = linspace(0,6,500); % define time vector t from 0 to 6 with 500 points
>> y = 2*sin(3*t); % define vector y(t) = 2 sin 3t (size is 1x500)
>> plot(t,y) % plot vector y vs. vector t
>> title('Graph of y(t)');
>> xlabel('Time, s') % add graph title (top of graph)
>> ylabel('y(t)');
>> grid % add x-axis label
% add y-axis label
% add grid lines to x and y axes 
```

The plot command has several options for creating graphs with various line types, symbols, and colors. The user should consult the on-screen tutorial by typing help plot to view the details of the various plotting options. As an example, the following commands plot y(t) = 2 sin 3t as a dashed red line with a circle (o) at each data point:

```matlab
>> t = linspace(0,4,50); % define time vector t from 0 to 4 with 50 points
>> y = 2*sin(3*t); % define vector y(t) = 2 sin 3t (size is 1x50)
>> plot(t,y,'ro--') % plot y(t) as red dashed line with circle symbol 
```

Several curves can be plotted on the same graph by entering multiple x–y vector pairs.
