import matplotlib.pyplot as plt
import numpy as np

def factorial(num: int) -> int:
    """
    Calculate the factorial of a number.
    """
    fact: int = 1
    for n in range(2, num + 1):
        fact *= n
    return fact

def sine(rad: float, num_terms: int = 10) -> float:
    """
    Calculate sine using the Taylor series expansion.
    """
    sine_value = 0
    for n in range(num_terms):
        term = ((-1)**n) * (rad**(2*n + 1)) / factorial(2*n + 1)
        sine_value += term
    return sine_value

def graph_sine():
    """
    Graph the sine function calculated using Taylor series and compare with the math.sin function.
    """
    # Generate angles from -2π to 2π
    x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    
    # Calculate sine values using the Taylor series and the math.sin function
    y_taylor = [sine(x, 15) for x in x_values]
    y_actual = np.sin(x_values)
    
    # Plot the graphs
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_taylor, label='Custom Sine Taylor', linestyle='--')
    plt.plot(x_values, y_actual, label='Biblioteca math.sin', linestyle='-')
    
    plt.ylim(-1, 1)

    # Add labels, legend, and title
    plt.title("Funcion seno: Custom Taylos vs Biblioteca math.sin")
    plt.xlabel("Angulo Radianes")
    plt.ylabel("Valor")
    plt.axhline(0, color='black', linewidth=0.5, linestyle='dotted')
    plt.axvline(0, color='black', linewidth=0.5, linestyle='dotted')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    angle_in_radians = 1.0
    precision = 10 
    result = sine(angle_in_radians, precision)

    n = 10
    print(f"Factorial de {2*n + 1}={factorial(2*n + 1)}")
    
    print(f"Sine({angle_in_radians}) with {precision} terms: {result}")
    
    # Display the graph
    graph_sine()

if __name__ == "__main__":
    main()
