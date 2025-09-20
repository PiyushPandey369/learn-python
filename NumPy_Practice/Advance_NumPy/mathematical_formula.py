# sigmoid -> y = 1 / (1 + e^(-x))
import numpy as np

# Example input values
inputs = np.random.random(10)
print("Input values:", inputs)

def sigmoid(values):
    """Apply sigmoid activation function element-wise."""
    denominator = 1 + np.exp(-values)
    return 1 / denominator

print("Sigmoid output:", sigmoid(inputs))


# Mean Squared Error -> (1/n) * Σ (y_true - y_pred)^2
actual_values = np.random.randint(1, 50, 20)
predicted_values = np.random.randint(1, 50, 20)

print("\nActual values:", actual_values)
print("Predicted values:", predicted_values)

def mean_squared_error(y_true, y_pred):
    """Calculate Mean Squared Error."""
    mse_value = np.mean((y_true - y_pred) ** 2)
    return mse_value

print("The Mean Squared Error is:", mean_squared_error(actual_values, predicted_values))


# Binary Cross Entropy -> -[y*log(p) + (1-y)*log(1-p)]
actual_probs = np.random.random(10)       # true labels (here: soft values, usually 0/1)
predicted_probs = np.random.random(10)    # predicted probabilities

print("\nActual values (BCE):", actual_probs)
print("Predicted values (BCE):", predicted_probs)

def binary_cross_entropy(y_true, y_pred):
    """Calculate Binary Cross-Entropy loss."""
    term1 = y_true * np.log(y_pred)
    term2 = (1 - y_true) * np.log(1 - y_pred)
    bce_value = -np.mean(term1 + term2)
    return bce_value

print("The Binary Cross Entropy is:", binary_cross_entropy(actual_probs, predicted_probs))
