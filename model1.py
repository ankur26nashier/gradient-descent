def gradientdescent(feacture_matrix, value_matrix, theta_matrix, alpha, iterations):
 import numpy
 length = len(value_matrix) 
 cost_history = []
 for i in range(iterations):
  prediction = numpy.dot(feature_matrix, theta_matrix)
  theta_matrix = theta_matrix - (alpha/m) * numpy.((prediction - value_matrix), feature_matrix)
  cost = compute_cost(feature_matrix, value_matrix, theta_matrix)
  cost_history.append(cost)

 return theta_matrix, pandas.Series(cost_history)
 






def compute_cost(feature_matrix, value_matrix, theta_matrix):
 """
 compute the cost function given a set of features /values and values for our theatas
 """
 m = len(value_matrix)
 sum_of_square_error = numpy.square(numpy.dot(feature_matrix, theta_matrix) - value_matrix).sum()
 cost = sum_of_square_error / (2*m)
 return cost
