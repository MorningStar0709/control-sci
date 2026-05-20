% % % % % % 路径寻优作图  
```matlab
function PlotR(V, cities)
figure;
cities=[cities cities(:,1)]; 
```

```matlab
[xxx, order] = max(V);
New = cities(:, order);
New = [New New(:, 1)];
subplot(1, 2, 1);
plot(cities(1, 1), cities(2, 1), 'r*'); % First city
hold on;
plot(cities(1, 2), cities(2, 2), '+'); % Second city
hold on;
plot(cities(1,:), cities(2,:), 'o-'), xlabel('X axis'), ylabel('Y axis'), title('Original Route');
axis([0, 1, 0, 1]);
subplot(1, 2, 2);
plot(New(1, 1), New(2, 1), 'r*'); % First city
hold on;
plot(New(1, 2), New(2, 2), '+'); % Second city
hold on;
plot(New(1,:), New(2,:), 'o-');
title('TSP solution');
xlabel('X axis'); ylabel('Y axis');
title('New Route');
axis([0, 1, 0, 1]);
axis on 
```

8个城市路径坐标程序:city8.txt  
```csv
0.1 0.1
0.9 0.5
0.9 0.1
0.45 0.9
0.9 0.8
0.7 0.9
0.1 0.45
0.45 0.1 
```
