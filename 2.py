from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_algorithms import Grover
from qiskit.circuit.library import GroverOperator

# Параметры задачи
n_qubits = 5  # Количество битов
target_state = '11111'  # Целевое состояние

# Создаем оракул
oracle = QuantumCircuit(n_qubits)
oracle.z(range(n_qubits))  # Отражаем целевое состояние 11111
oracle.name = "Oracle"

# Создаем схему алгоритма Гровера
grover_operator = GroverOperator(oracle)

# Создаем квантовую цепь для алгоритма Гровера
grover_circuit = QuantumCircuit(n_qubits)
grover_circuit.h(range(n_qubits))  # Применяем Hadamard-гейты ко всем кубитам
grover_circuit.append(grover_operator, range(n_qubits))  # Добавляем оператор Гровера
grover_circuit.h(range(n_qubits))  # Повторно применяем Hadamard-гейты
grover_circuit.measure_all()  # Измеряем все кубиты

# Сохраняем схему в файл (например, в формате PNG)
grover_circuit.draw('mpl', filename='grover_circuit.png')

# Симуляция
simulator = AerSimulator()  # Используем правильный импорт
compiled_circuit = transpile(grover_circuit, simulator)
result = simulator.run(compiled_circuit, shots=1000).result()
counts = result.get_counts()

# Вывод результата
print("Результат измерений:", counts)

# Проверим, нашли ли целевое состояние '11111'
if '11111' in counts:
    print("Целевое состояние 11111 найдено!")
else:
    print("Целевое состояние 11111 не найдено.")
