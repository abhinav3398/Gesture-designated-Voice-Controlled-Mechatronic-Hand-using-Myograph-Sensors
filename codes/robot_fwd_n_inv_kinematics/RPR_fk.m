%? Project Name:     gesture controled & voice designated robotic hand using myograph sensors
%? Author List:		Abhinav Lakhani
%? file name:		RPR_fk.m
%? Functions:		RPR_fk
%? Global Variables: none

function [ pos, R ] = RPR_fk( theta1, theta2, theta3, theta4, theta5, theta6, theta7)
%%    The input to the function will be the joint
%%    angles of the robot in radians, and the extension of the prismatic joint in inches.
%%    The output includes: 
%%    1) The position of the end effector and the position of 
%%    each of the joints of the robot
%%    2) The rotation matrix R_06
    xl=1;%small link length
    l1=xl;
    l2=xl;
    L3=15*1;
    l4=xl;
    L5=12.5*1;
    l6=xl;
    l7=xl;
    e = 1.*xl;
    g = xl;    
    pos = zeros(13, 3);
    R = eye(3);

    %first rotate w.r.t Y-axis
    temp = [0 0 -1 0; 0 1 0 0; 1 0 0 0; 0 0 0 1];
    
    tf1 = temp*compute_dh_matrix(0,(pi/2),l1,  theta1);
    tf2 = tf1*compute_dh_matrix(0,  -pi/2, l2, -theta2+pi/2);
    tf3 = tf2*compute_dh_matrix(0, -pi/2,  L3, theta3-pi/2);
    tf4 = tf3*compute_dh_matrix(0,  pi/2,  l4, theta4+pi/2);
    tf5 = tf4*compute_dh_matrix(0, pi/2,  L5, theta5-pi/2);
    tf6 = tf5*compute_dh_matrix(0, pi/2,  l6, theta6-pi/2);
    tf7 = tf6*compute_dh_matrix(0,     0,  l7, theta7+0);
    
    temp_pos8 =  tf7*[0     0 e 1]';
    temp_pos9 =  tf7*[g/2   0 e 1]';
    temp_pos10 =  tf7*[-g/2  0 e 1]';
    temp_pos11 =  tf7*[g/2   0  0 1]';
    temp_pos12 = tf7*[-g/2  0  0 1]';
    
    pos = [0        0        0;
           tf1(1,4) tf1(2,4) tf1(3,4);
           tf2(1,4) tf2(2,4) tf2(3,4);
           tf3(1,4) tf3(2,4) tf3(3,4);
           tf4(1,4) tf4(2,4) tf4(3,4);
           tf5(1,4) tf5(2,4) tf5(3,4);
           tf6(1,4) tf6(2,4) tf6(3,4);
           tf7(1,4) tf7(2,4) tf7(3,4);
           temp_pos8(1)    temp_pos8(2)    temp_pos8(3);
           temp_pos9(1)    temp_pos9(2)    temp_pos9(3);
           temp_pos10(1)    temp_pos10(2)    temp_pos10(3);
           temp_pos11(1)    temp_pos11(2)    temp_pos11(3);
           temp_pos12(1)   temp_pos12(2)  temp_pos12(3)];
       
    R = tf7(1:3, 1:3);
end
%* compute D-H table
function A = compute_dh_matrix(r, alpha, d, theta)    
    A = [cos(theta) -sin(theta)*cos(alpha) sin(theta)*sin(alpha) cos(theta)*r;
        sin(theta) cos(theta)*cos(alpha) -cos(theta)*sin(alpha) sin(theta)*r;
        0          sin(alpha)             cos(alpha)            d;
        0          0                      0                     1];
end