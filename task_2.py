import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Метод Монте-Карло
def monte_carlo_integration(func, a, b, num_samples=10000):
    x_random = np.random.uniform(a, b, num_samples)
    
    y_max = max(f(np.linspace(a, b, 1000)))  # Знаходимо максимум f(x) на [a, b]
    y_random = np.random.uniform(0, y_max, num_samples)
    
    under_curve = y_random < func(x_random)
    area = (b - a) * y_max * np.mean(under_curve)
    
    return area

# Обчислення інтеграла методом Монте-Карло
monte_carlo_result = monte_carlo_integration(f, a, b)

# Перевірка результату за допомогою функції quad
result, error = spi.quad(f, a, b)

# Оцінка похибки
relative_error = abs(monte_carlo_result - result) / result

# Виведення результатів
print(f"Результат методом Монте-Карло: {monte_carlo_result:.5f}")
print(f"Інтеграл (функція quad): {result:.5f}, Абсолютна похибка: {error:.2e}")
print(f"Відносна похибка методу Монте-Карло: {relative_error:.2%}")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')

ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()
