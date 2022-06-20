%? Project Name:     gesture controled & voice designated robotic hand using myograph sensors
%? Author List:		 Abhinav Lakhani
%? file name:		 animate_hand.m
%? Functions:		 animate_hand
%? Global Variables: totalTimeSteps, GraphingTimeDelay, q01, q02, q03, q04,
%?                   q05, q06, q07, q11, q12, q13, q14, q15, q16, q17, 
%?                   scale_f, hrobot, i, t, pos, R
%% Helper script to visualize forward kinematics of a the robot
%% _fk function 
close all
pause on;  %* Set this to on if want to watch the animation
GraphingTimeDelay = 0.1; %* The length of time that Matlab should pause between positions when graphing, if at all, in seconds.
totalTimeSteps = 100; %* Number of steps in the animation
%% Generate the starting and final joint angles, and gripper distance
%% Set values manually, or randomise as shown below
q01 = 0;
q02 = 0;
q03 = 0;
q04 = 0;
q05 = 0;
q06 = 0;
q07 = 0;

q11 = 0;
q12 = 0;
q13 = 0;
q14 = 0;    
q15 = 0;
q16 = 0;
q17 = 0;
%% Use below code if want to randomise
% q01 = rand(1) * 2 * pi;
% q02 = rand(1) * 2 * pi;
% q03 = rand(1) * 2 * pi;
% q04 = rand(1) * 2 * pi;
% q05 = rand(1) * 2 * pi;
% q06 = rand(1) * 2 * pi;
% q07 = rand(1) * 2 * pi;
% g0 = rand(1) * 2;
% 
% q11 = rand(1) * 2 * pi;
% q12 = rand(1) * 2 * pi;
% q13 = rand(1) * 2 * pi;
% q14 = rand(1) * 2 * pi;
% q15 = rand(1) * 2 * pi;
% q17 = rand(1) * 2 * pi;
% q16 = rand(1) * 2 * pi;
% g1 = 0;

%% Setup plot
figure
scale_f = 100;
axis vis3d
axis(scale_f*[-1/2 1/2 -1/2 1/2 -3/4 1/2])
grid on
view(70,10)
xlabel('X (in.)')
ylabel('Y (in.)')
zlabel('Z (in.)')
%% Plot robot initially
hold on
hrobot = plot3([0 0 10], [0 0 0], [0 6 6],'k.-','linewidth',1,'markersize',10);
%% Animate the vector
pause(GraphingTimeDelay);
for i = 1:totalTimeSteps
    t = i/totalTimeSteps;
    [pos, R] = RPR_fk(q01*(1-t) + q11*(t), q02*(1-t) + q12*(t),...
        q03*(1-t) + q13*(t),q04*(1-t) + q14*(t),q05*(1-t) + q15*(t),...
        q06*(1-t) + q16*(t), q07*(1-t) + q17*(t));
%test - 1    
%     pos =[0         0         0;
%          0         0    3.0000;
%     0.0000   -0.0000    8.7500;
%     7.3750   -0.0000    8.7500;
%     7.3750   -0.0000    8.7500;
%    10.3750   -0.0000    8.7500;
%    10.3750   -0.0000    7.7500;
%    10.3750   -0.0000    9.7500;
%    11.5000   -0.0000    7.7500;
%    11.5000   -0.0000    9.7500];
%test - 2
%    pos = lynx_fk(pi,pi/2,pi/2,-pi/2,-pi/6,2);
    
    set(hrobot,'xdata',[pos(1, 1) pos(2, 1) pos(3, 1) pos(4, 1) pos(5, 1) pos(6, 1) pos(7, 1) pos(8, 1) pos(9, 1) pos(10, 1) pos(11, 1) pos(12, 1) pos(13, 1)]',...
        'ydata',[pos(1, 2) pos(2, 2) pos(3, 2) pos(4, 2) pos(5, 2) pos(6, 2) pos(7, 2) pos(8, 2) pos(9, 2) pos(10, 2) pos(11, 2) pos(12, 2) pos(13, 2)]',...
        'zdata',[pos(1, 3) pos(2, 3) pos(3, 3) pos(4, 3) pos(5, 3) pos(6, 3) pos(7, 3) pos(8, 3) pos(9, 3) pos(10, 3) pos(11, 3) pos(12, 3) pos(13, 3)]');
    
    pause(GraphingTimeDelay);
end