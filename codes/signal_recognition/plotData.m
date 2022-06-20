%? Project Name:     gesture controled & voice designated robotic hand using myograph sensors
%? Author List:		Abhinav Lakhani
%? file name:		plotData.m
%? Functions:		plotData
%? Global Variables: none

function plotData(X, y)
%% PLOTDATA Plots the data points X and y into a new figure 
%%   PLOTDATA(x,y) plots the data points with + for the positive examples
%%   and o for the negative examples. 
%%   X is assumed to be a Mx6 matrix.

% ====================== //// //// //// ======================
%%               Plot the positive and negative examples on a
%%               2D plot, using the option 'k+' for the positive
%%               examples and 'ko' for the negative examples.
%

%% find indices of the positive & negative examples
pos = find(y == 1); neg = find(y == 0);
t0 = X(:,1);t1 = X(:,2);
RMS1 = X(:,3);RMS2 = X(:,4);
MEAN1 = X(:,5);MEAN2 = X(:,6);
% =========================================================================
%* Create New Figure
figure1; hold on;
plot(t0(pos), t1(pos), 'k+',...
       'linewidth', 2, 'markersize', 7);
plot(t0(neg), t1(neg), 'ko',...
       'markerfacecolor', 'y', 'markersize', 7);
hold off;
% =========================================================================
%* Create New Figure
figure2; hold on;
plot(RMS1(pos), RMS2(pos), 'k+',...
       'linewidth', 2, 'markersize', 7);
plot(RMS1(neg), RMS2(neg), 'ko',...
       'markerfacecolor', 'y', 'markersize', 7);
hold off;
% =========================================================================
%* Create New Figure
figure3; hold on;
plot(MEAN1(pos), MEAN2(pos), 'k+',...
       'linewidth', 2, 'markersize', 7);
plot(MEAN1(neg), MEAN2(neg), 'ko',...
       'markerfacecolor', 'y', 'markersize', 7);
hold off;
% =========================================================================
end