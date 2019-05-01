# coding: utf-8
import numpy as np

# np.random.choice
batch_mask = np.random.choice(100,10)
print(batch_mask)

# np.random.randn

input_size = 10
hidden_size = 20
output_size = 10

params = {}
params['W1'] = np.random.randn(input_size,hidden_size)
params['B1'] = np.zeros(hidden_size)
params['W2'] = np.random.randn(hidden_size,output_size)
params['B2'] = np.zeros(output_size)


input_data = np.random.choice(10,10)
print(input_data)

W1, W2 = params['W1'], params['W2']
B1, B2 = params['B1'], params['B2']

node1 = np.dot(input_data,W1)
node1 += B1
print(node1)

node2 = np.dot(node1,W2)
node2 += B2
print(node2);

