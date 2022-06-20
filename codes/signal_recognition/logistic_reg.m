%? Project Name:     gesture controled & voice designated robotic hand using myograph sensors
%? Author List:		Abhinav Lakhani
%? file name:		logistic_reg,m
%? Functions:		none
%? Global Variables: data, X, y, m, n, initial_theta, cost, grad, options,
%?                   p, lambda
%% Logistic Regression

%% Initialization
clear ; close all; clc

%% Load Data
%*  The first two columns contains the raw signal values
%*  3ed & 4th columns contains RMS values of the signals
%*  5ed & 6th columns contains MEAN values of the signals
%*  last column contains lables(i.e muscle flex(1) or no flex(0))

data = load('emg_entries.txt');
%% first few values are null values
data = data(20:10500,:);
X = data(11:end, 1); y = data(11:end, end);
%% each row contains data as follows
%% [signal1_samples signal1_RMS signal1_MEAN signal2_samples signal2_RMS signal2_MEAN]
X = [X zeros(size(X,1), 11) data(11:end, 3) data(11:end, 5) data(11:end, 2) zeros(size(X,1), 11) data(11:end, 4) data(11:end, 6)];
%% sample propogation
for i = 2:(size(X,2)/2)
  X(i:end,i)=X(1:end-(i-1),1);
  X(i:end,i+(size(X,2)/2))=X(1:end-(i-1),(size(X,2)/2)+1);
end

%% ==================== Part 0: Plotting ====================
fprintf(['Plotting data with + indicating (y = 1) examples and o ' ...
         'indicating (y = 0) examples.\n']);

plotData(data(:,1:end-1), y);
fprintf('\nProgram paused. Press enter to continue.\n');
pause;

%% =========== Part 1: Regularized Logistic Regression ============
%*  To do Regularized Logistic Regression so, 
%*  we introduce more features to use -- in particular, we add
%*  polynomial features to our data matrix (similar to polynomial
%*  regression).
%

%* Add Polynomial Features

%* Note that mapFeature also adds a column of ones for us, so the intercept
%* term is handled
X = mapFeature(X(:,1), X(:,2));

%* Initialize fitting parameters
initial_theta = zeros(size(X, 2), 1);

%* Set regularization parameter lambda to 1
lambda = 1;

%* Compute and display initial cost and gradient for regularized logistic
%* regression
[cost, grad] = costFunctionReg(initial_theta, X, y, lambda);

fprintf('Cost at initial theta (zeros): %f\n', cost);
fprintf('Gradient at initial theta (zeros) - first five values only:\n');
fprintf(' %f \n', grad(1:5));
fprintf('\nProgram paused. Press enter to continue.\n');
pause;

%* Compute and display cost and gradient
%* with all-ones theta and lambda = 10
test_theta = ones(size(X,2),1);
[cost, grad] = costFunctionReg(test_theta, X, y, 10);

fprintf('\nCost at test theta (with lambda = 10): %f\n', cost);
fprintf('Gradient at test theta - first five values only:\n');
fprintf(' %f \n', grad(1:5));
fprintf('\nProgram paused. Press enter to continue.\n');
pause;

%% ============= Part 2: Regularization and Accuracies =============
%*  Try the following values of lambda (0, 1, 10, 100).

%* Initialize fitting parameters
initial_theta = zeros(size(X, 2), 1);

%* Set regularization parameter lambda to 1 (you should vary this)
lambda = 10;

%* Set Options
options = optimset('GradObj', 'on', 'MaxIter', 400);

%* Optimize
[theta, J, exit_flag] = ...
	fminunc(@(t)(costFunctionReg(t, X, y, lambda)), initial_theta, options);

%* Compute accuracy on our training set
p = predict(theta, X);

fprintf('Train Accuracy: %f\n', mean(double(p == y)) * 100);