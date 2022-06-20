%? Project Name:     gesture controled & voice designated robotic hand using myograph sensors
%? Author List:		Abhinav Lakhani
%? file name:		predict.m
%? Functions:		predict
%? Global Variables: none

function p = predict(theta, X)
%% PREDICT Predict whether the label is 0 or 1 using learned logistic 
%* regression parameters theta
%*   p = PREDICT(theta, X) computes the predictions for X using a 
%*   threshold at 0.5 (i.e., if sigmoid(theta'*x) >= 0.5, predict 1)

m = size(X, 1); %* Number of training examples

%* need to return the following variables correctly
p = zeros(m, 1);

%% Instructions: code to make predictions using
%%               your learned logistic regression parameters. 
%%               You should set p to a vector of 0's and 1's
%
pre_sig = zeros(1,5);
for i=1:m
  p(i) = (sigmoid(theta'*X(i,:)') >= 0.45) || (sigmoid(theta'*X(i,:)') <= 0.35) || (pre_sig(1) >= 0.45) || (pre_sig(1) <= 0.35) || (pre_sig(2) >= 0.45) || (pre_sig(2) <= 0.35) || (pre_sig(3) >= 0.45) || (pre_sig(3) <= 0.35) || (pre_sig(4) >= 0.45) || (pre_sig(4) <= 0.35) || (pre_sig(5) >= 0.45) || (pre_sig(5) <= 0.35); 
  pre_sig(5) = pre_sig(4);
  pre_sig(4) = pre_sig(3);
  pre_sig(3) = pre_sig(2);
  pre_sig(2) = pre_sig(1);
  pre_sig(1) = sigmoid(theta'*X(i,:)');
  end  
% =========================================================================
end
