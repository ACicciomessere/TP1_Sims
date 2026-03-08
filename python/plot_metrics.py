import matplotlib.pyplot as plt
import numpy as np

def plot_benchmark_N():
    data = np.loadtxt('benchmark_N.txt', skiprows=1)
    N = data[:, 0]
    bf_mean = data[:, 1]
    bf_std = data[:, 2]
    cim_mean = data[:, 3]
    cim_std = data[:, 4]

    plt.figure(figsize=(10, 6))
    plt.errorbar(N, bf_mean, yerr=bf_std, fmt='-o', label='Brute Force')
    plt.errorbar(N, cim_mean, yerr=cim_std, fmt='-s', label='Cell Index Method')
    
    plt.xlabel('Number of particles (N)')
    plt.ylabel('Execution Time (ms)')
    plt.title('Execution Time vs N (Fixed M=13)')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig('time_vs_n.png')
    print("Saved time_vs_n.png")

def plot_benchmark_M():
    data = np.loadtxt('benchmark_M.txt', skiprows=1)
    M = data[:, 0]
    bf_mean = data[:, 1]
    bf_std = data[:, 2]
    cim_mean = data[:, 3]
    cim_std = data[:, 4]

    plt.figure(figsize=(10, 6))
    plt.errorbar(M, bf_mean, yerr=bf_std, fmt='-o', label='Brute Force')
    plt.errorbar(M, cim_mean, yerr=cim_std, fmt='-s', label='Cell Index Method')
    
    plt.xlabel('Number of Cells per dimension (M)')
    plt.ylabel('Execution Time (ms)')
    plt.title('Execution Time vs M (Fixed N=1000)')
    plt.yscale('log')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig('time_vs_m.png')
    print("Saved time_vs_m.png")

if __name__ == '__main__':
    try:
        plot_benchmark_N()
        plot_benchmark_M()
    except Exception as e:
        print("Error processing benchmark files. Run 'java -cp src Benchmark' first.")
        print(e)
