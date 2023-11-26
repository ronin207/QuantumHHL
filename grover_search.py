"""
Grover's algorithm could offer a quadratic speedup in unstructured search problems.
While a classicial search through a list of size N could take between N/2 and N tries to find an item,
Grover's algorithm could find the item in sqrt(N) steps. Additionally, if you wanted to search through 
a list of numbers to see if a given number is there, Grover's algorithm begins with an oracle function which
marks any values that fulfull the search criteria. Then a diffuser function is applied to the marked values
makes returning the location of the marked item more likely than other item. Roughly sqrt(N) steps are required, 
where N is the size of the list, amplifies the amplitude value associated with the location of the marked item 
to near 1.0, while the amplitude values associated with the other items are reduced to near 0.0.

Initial State: \ket{\psi} = \frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} \ket{x}
Diffuser Operator: U = 0.5I - 0.5\ket{\psi}\bra{\psi}

Pseudocode:
INPUT
    N: number of items in the list
    oracle(x): function that returns true if x is the target item, and false otherwise

Steps: 
    1. Initialise state (Hadamard transform on all qubits)
    2. Iterate over Grover's algorithm
        for k = 1 to sqrt(N) do
            2a. Apply oracle
            2b. Apply diffuser
                Hadamard transform on all qubits
                Apply an X gate on all qubits
                Apply a multi-controlled Z gate (which flips the sign of the state only if all qubits are in the state \ket{1})
                Apply an X gate on all qubits
                Hadamard transform on all qubits
        end for
    3. Measure the state
    4. Return the measured value
"""

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute

class Grover:
    def __init__(self):
        pass

if __name__ == "__main__":
    pass