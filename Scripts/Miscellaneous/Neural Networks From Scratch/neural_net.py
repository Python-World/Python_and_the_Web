import numpy as np


def sigmoid(x, deriv=False):
    """Calculates sigmoid function for given input.

    Args:
      x: Numeric input.
      deriv: If true, returns derivative on that point.

    Returns:
      Sigmoid or sigmoid derivative at specific point.
    """
    if deriv:
        return sigmoid(x) * (1 - sigmoid(x))
    return 1 / (1 + np.exp(-x))


class MLP:
    """
    A implementation of a simple 2 layers Multilayer Perceptron.
    """

    def __init__(self, input_size, hidden_size, output_size):
        self.Wxh = np.random.randn(input_size + 1, hidden_size)
        self.Who = np.random.randn(hidden_size, output_size)

    def forward(self, X):
        """Pass the input through the network and calculates the
        corresponding output for each layer.

        Args:
          X: Input vector with shape (N,x).

        Returns:
          Output vector with shape (L,N,o).
        """
        ones_l0 = np.ones((X.shape[0], 1))

        l0 = np.concatenate((X, ones_l0), axis=1)
        l1 = sigmoid(np.dot(l0, self.Wxh))
        l2 = sigmoid(np.dot(l1, self.Who))

        return l0, l1, l2

    def predict(self, X):
        """Returns the output in the last layer.

        Args:
          X: Input vector with shape (N,x).

        Returns:
          Output vector with shape (N,o).
        """
        l2 = self.forward(X)[2]
        return l2

    def fit(self, X, y, epochs=50, lr=1e-3):
        """Fit the model into given data.

        Args:
          X: Training input vectors with shape (N,x).
          y: Training output classes with shape (N).
          epochs: Number of epochs.
          lr: Learning rate.

        Returns:
          A history of losses in each epoch.
        """
        total_loss = []

        for epoch in range(epochs):
            l0, l1, l2 = self.forward(X)

            l2_error = y - l2
            l2_delta = l2_error * sigmoid(l2, deriv=True)

            l1_error = l2_delta.dot(self.Who.T)
            l1_delta = l1_error * sigmoid(l1, deriv=True)

            self.Who += lr * l1.T.dot(l2_delta)
            self.Wxh += lr * l0.T.dot(l1_delta)

            epoch_loss = np.mean(np.abs(l2_error))

            if (epoch % 1000) == 0:
                total_loss.append(epoch_loss)
                print("Loss: " + str(epoch_loss))

        return total_loss


# Heres a simple example with the XOR gate.
X_train = np.array(
    [[0, 0], [0, 1], [1, 0], [1, 1]]
)  # Generate the training X data

y_train = np.array([[0], [1], [1], [0]])  # Generate the training y data

model = MLP(2, 3, 1)  # Instanciate the model

loss = model.fit(X_train, y_train, 10000, 1)  # Fit the model with given data

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Test data

model.predict(X)  # Predict test output
