# Quant_Grover
Grover for MaxCut problem
This is Grover's quantum algorithm that solves the MaxCut problem for a set of (11111).
It works as follows:
1. Create a quantum superposition of all possible states using Hadamard gates to all qubits. We get a uniform distribution over all states;
2. Apply the oracle operator to mark the target state (11111), imposing a phase shift on it. In the case of the problem (11111), the oracle changes the phase of this state to −1. For all other states, the phase remains unchanged;
3. Set the Grover operator (diffusion). After the oracle has marked the target state, we need to increase the probability that we will measure this state. To do this, we use the diffusion operator, which increases the probability of the "correct" state. The diffusion operator inverts the amplitude with respect to the mean;
4. Repeat steps 2,3 several times;
5. After applying the oracle and Grover operator several times, we measure the state. Due to the increased probability, we are more likely to get the target state, for example 11111.
![Scheme of Grover](https://raw.githubusercontent.com/Space-Lizards/Quant_Grover/main/grover_circuit.png)
