from itertools import product
import random

def binary_combinations(n):
    '''returns list of all binary combinations necessary for the AND-Gate'''
    return list(product([0, 1], repeat=n))

def initilize_weight(dimension):
    '''Returns the random weights. Last weight in the list is the bias.'''
    return [random.uniform(-1, 1) for _ in range(dimension+1)]

def check_and_gate_result(gate_result):
    '''Returns the amount of correct and-gate classifications for a given gate result'''
    correct_results = 0
    for i in range(len(gate_result)):
        if i == len(gate_result) - 1 and gate_result[i] == 1:
            correct_results += 1
        elif i != len(gate_result) - 1 and gate_result[i] == 0:
            correct_results += 1
    return correct_results

def and_gate(input, weights):
    # weights has the size of len(input) + 1 and the last entry is the bias
    sum = weights[len(input)]
    for i in range(len(input)):
        sum += input[i]*weights[i]
    # using the step function as the activation function
    if sum > 0:
        return 1
    return 0

# Main Loop from the excercise
def main(n):
    inputs = binary_combinations(n)
    print(inputs)
    result = []
    count = 0
    while check_and_gate_result(result) != len(inputs):
        result = []
        weights = initilize_weight(n)
        for i in range(len(inputs)):
            result.append(and_gate(inputs[i], weights))
        count += 1
        print("Try: " + str(count) + "\nCorrect classifications: " +
              str(check_and_gate_result(result)))
    print(weights)

main(2)
