rulelist = [1 1 1 1 1;    % Edit rule base
    1 2 3 1 1;
    1 3 4 1 1;

2 1 2 1 1;
    2 2 3 1 1;
    2 3 4 1 1;

3 1 3 1 1;
    3 2 4 1 1;
    3 3 5 1 1];

a = addrule(a, rulelist);
showrule(a)    % Show fuzzy rule base

al = setfis(a, 'DefuzzMethod', 'mom'); % Defuzzy
writefis(al, 'wash');    % Save to fuzzy file "wash.fis" 
```

```matlab
a2 = readfis('wash');
figure(1);
plotfis(a2);
figure(2);
plotmf(a,'input',1);
figure(3);
plotmf(a,'input',2);
figure(4);
plotmf(a,'output',1);

ruleview('wash'); % Dynamic Simulation
x = 60;
y = 70;
z = evalfis([x,y],a2) % Using fuzzy inference 
```

模糊自适应整定 PID 仿真程序: 包括模糊推理系统设计程序 chap4\_7a.m 及模糊 PID 控制程序 chap4\_7b.m。

(1) 模糊推理系统设计程序: chap4\_7a.m  
```matlab
% Fuzzy Tunning PI Control
clear all;
close all;
a = newfis('fuzzpid');

a = addvar(a, 'input', 'e', [-1, 1]); % Parameter e
a = addmf(a, 'input', 1, 'N', 'zmf', [-1, -1/3]);
a = addmf(a, 'input', 1, 'Z', 'trimf', [-2/3, 0, 2/3]);
a = addmf(a, 'input', 1, 'P', 'smf', [1/3, 1]);

a = addvar(a, 'input', 'ec', [-1, 1]); % Parameter ec
a = addmf(a, 'input', 2, 'N', 'zmf', [-1, -1/3]);
a = addmf(a, 'input', 2, 'Z', 'trimf', [-2/3, 0, 2/3]);
a = addmf(a, 'input', 2, 'P', 'smf', [1/3, 1]);

a = addvar(a, 'output', 'kp', 1/3* [-10, 10]); % Parameter kp
a = addmf(a, 'output', 1, 'N', 'zmf', 1/3* [-10, -3]);
a = addmf(a, 'output', 1, 'Z', 'trimf', 1/3* [-5, 0, 5]);
a = addmf(a, 'output', 1, 'P', 'smf', 1/3* [3, 10]);

a = addvar(a, 'output', 'ki', 1/30* [-3, 3]); % Parameter ki
a = addmf(a, 'output', 2, 'N', 'zmf', 1/30* [-3, -1]);
a = addmf(a, 'output', 2, 'Z', 'trimf', 1/30* [-2, 0, 2]);
a = addmf(a, 'output', 2, 'P', 'smf', 1/30* [1, 3]);

rulelist = [1 1 1 2 1 1;
    1 2 1 2 1 1;
    1 3 1 2 1 1; 
```

```matlab
2 1 1 3 1 1;
2 2 3 3 1 1;
2 3 3 3 1 1;

3 1 3 2 1 1;
3 2 3 2 1 1;
3 3 3 2 1 1];

a = addrule(a, rulelist);
a = setfis(a, 'DefuzzMethod', 'centroid');
writefis(a, 'fuzzpid');

a = readfis('fuzzpid');
figure(1);
plotmf(a, 'input', 1);
figure(2);
plotmf(a, 'input', 2);
figure(3);
plotmf(a, 'output', 1);
figure(4);
plotmf(a, 'output', 2);
figure(5);
plotfis(a);

fuzzy fuzzpid;
showrule(a)
ruleview fuzzpid; 
```

(2) 模糊 PID 控制程序: chap4\_7b.m  
```matlab
% Fuzzy PI Control
close all;
clear all;

warning off;
a = readfis('fuzzpid');    % Load fuzzpid.fis

ts = 0.001;
sys = tf(133, [1,25,0]);
dsys = c2d(sys, ts, 'z');
[num, den] = tfdata(dsys, 'v');

u_1 = 0; u_2 = 0;
y_1 = 0; y_2 = 0;
e_1 = 0; ec_1 = 0; ei = 0;

kp0 = 0; ki0 = 0;
for k = 1:1:1000
time(k) = k* ts;

r(k) = 1;
% Using fuzzy inference to tunning PI
k_pid = evalfis([e_1, ec_1], a); 
```
