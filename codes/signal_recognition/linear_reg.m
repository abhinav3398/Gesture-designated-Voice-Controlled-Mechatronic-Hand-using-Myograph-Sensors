%? Project Name:     gesture controled & voice designated robotic hand using myograph sensors
%? Author List:		Abhinav Lakhani
%? file name:		linear_reg,m
%? Functions:		none
%? Global Variables: data, X, y, m, n, initial_theta, cost, grad, options, p

%% Logistic Regression of EMG signal
%% Initialization
clear ; close all;

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

%% ==================== Part 1: Plotting ====================
fprintf(['Plotting data with + indicating (y = 1) examples and o ' ...
         'indicating (y = 0) examples.\n']);
plotData(data(:,1:end-1), y);
fprintf('\nProgram paused. Press enter to continue.\n');
pause;

%% ============ Part 2: Compute Cost and Gradient ============
%*  In this part implement the cost and gradient
%*  for logistic regression.

%*  Setup the data matrix appropriately, and add ones for the intercept term
[m, n] = size(X);

%* Add intercept term to x and X_test
X = [ones(m, 1) X];

%* Initialize fitting parameters
initial_theta = zeros(n + 1, 1);

%* Compute and display initial cost and gradient
[cost, grad] = costFunction(initial_theta, X, y);

fprintf('\nProgram paused. Press enter to continue.\n');
pause;

%% ============= Part 3: Optimizing using fminunc  =============
%*  use a built-in function (fminunc) to find the
%*  optimal parameters theta.

%*  Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 400);

%*  Run fminunc to obtain the optimal theta
%*  This function will return theta and the cost 
[theta, cost] = ...
	fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);

%* Print theta to screen
fprintf('Cost at theta found by fminunc: %f\n', cost);
fprintf('theta: \n');
fprintf(' %f \n', theta);
fprintf('\nProgram paused. Press enter to continue.\n');
pause;

%% ============== Part 4: Predict and Accuracies ==============
%*  After learning the parameters, WE'll like to use it to predict the outcomes
%*  on unseen data. 
%
p = predict(theta, X);
fprintf('Train Accuracy: %f\n', mean(double(p == y)) * 100);