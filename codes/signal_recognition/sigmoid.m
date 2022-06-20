%? Project Name:     gesture controled & voice designated robotic hand using myograph sensors
%? Author List:		Abhinav Lakhani
%? file name:		sigmoid.m
%? Functions:		sigmoid
%? Global Variables: none



function g = sigmoid(z)
%% SIGMOID Compute sigmoid function
%%   g = SIGMOID(z) computes the sigmoid of z.
% need to return the following variables correctly 
g = zeros(size(z));
% ====================== //// //// //// ======================
%% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%%               vector or scalar).
g = 1 ./ (1 .+ exp(-z));
% =============================================================
end
