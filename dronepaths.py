import matplotlib.pyplot as plt
import numpy as np

def plot_drone_paths():
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Create figure
    plt.figure(figsize=(8, 6))
    
    # Generate and plot 5 random paths
    for i in range(5):
        x = np.random.rand(10)
        y = np.random.rand(10)
        plt.plot(x, y, 'bo-', label=f'Path {i+1}')
    
    # Add title and labels
    plt.title('Random Drone Flight Paths', fontsize=14)
    plt.xlabel('X-axis (km)', fontsize=12)
    plt.ylabel('Y-axis (km)', fontsize=12)
    
    # Add legend
    plt.legend()
