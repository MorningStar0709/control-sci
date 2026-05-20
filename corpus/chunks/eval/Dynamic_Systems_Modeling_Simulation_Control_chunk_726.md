# B.2 BASIC MATLAB COMPUTATIONS

MATLAB is a command-driven computing tool. Once the user has started MATLAB, he or she will see the following prompt

>>

The user may now type in single-line commands to perform calculations. For example, the user can define variables (real or complex) by assigning numerical values. When a user defines a variable, MATLAB “echoes back” the assignment to the screen:

$> > \texttt { x } = \texttt { 2 }$

% This command defines variable x = 2

Upon hitting the return key MATLAB displays

$\mathrm { ~ \textbf ~ { ~ x ~ } ~ } = \mathrm { ~ \textbf ~ { ~ 2 ~ } ~ }$

The user can suppress the print to the screen by inserting a semicolon (;) after the command. Note that in the previous simple example the character % defines the start of a “comment” line, where the user can add descriptive text that is not processed by MATLAB. After defining variables, the user can perform basic mathematical operations using + for addition, − for subtraction, \* for multiplication, / for division, and ̂ for power. The following simple commands illustrate the use of these math operations:

>> x = 2 % define variable $x = 2$ >> y = 6 % define variable $y = 6$ >> z = 3*x + 4.5*y; % define variable $z = 3x + 4.5y$ (no print to screen)  
>> a = z/6 - 2.1*x^3; % define variable $a = z/6 - 2.1x^3$ (no print to screen)

After executing these commands, the four variables x, y, z, and a will be assigned numerical values in MATLAB’s workspace. These four variables can be used at any time during the MATLAB session. The following commands display and clear the workspace:

>> whos % list all variables in the workspace and their size
>> clear % remove all variables from the workspace memory

The user can always obtain a brief on-screen tutorial on MATLAB’s built-in functions by using the help ‘function name’ command. For example, typing help clear explains the built-in clear function.
