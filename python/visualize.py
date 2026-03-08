import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def main():
    if not os.path.exists('particles.txt'):
        print("Error: particles.txt not found. Run the Java simulation first.")
        return

    particles = {}
    with open('particles.txt', 'r') as f:
        N = int(f.readline().strip())
        L = float(f.readline().strip())
        M = int(f.readline().strip())
        target_global = int(f.readline().strip())
        
        for _ in range(N):
            parts = f.readline().strip().split()
            p_id = int(parts[0])
            x = float(parts[1])
            y = float(parts[2])
            radius = float(parts[3])
            prop = float(parts[4])
            particles[p_id] = (x, y, radius, prop)
            
        # Parse target particle and its neighbors
        target_line = f.readline()
        neighbors_line = f.readline()
        
        target = -1
        neighbors = set()
        
        if target_line and target_line.startswith("TARGET"):
            target = int(target_line.strip().split()[1])
            
        if neighbors_line and neighbors_line.startswith("NEIGHBORS"):
            parts = neighbors_line.strip().split()
            if len(parts) > 1:
                neighbors = set(int(n) for n in parts[1:])

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_aspect('equal')
    ax.set_title(f'Particle Distribution (N={N}, L={L}, M={M})\nTarget: {target}, Neighbors: {len(neighbors)}')

    # Draw grid
    cell_size = L / M
    for i in range(M + 1):
        ax.axhline(i * cell_size, color='lightgray', linestyle='--')
        ax.axvline(i * cell_size, color='lightgray', linestyle='--')

    # Draw particles
    for p_id, (x, y, radius, prop) in particles.items():
        if p_id == target:
            color = 'red'
            zorder = 5
        elif p_id in neighbors:
            color = 'yellow'
            zorder = 4
        else:
            color = 'cyan'
            zorder = 3
            
        circle = patches.Circle((x, y), radius, edgecolor='black', facecolor=color, alpha=0.8, zorder=zorder)
        ax.add_patch(circle)
        # Optional: Add ID labels
        # ax.text(x, y, str(p_id), color='black', fontsize=8, ha='center', va='center')

    plt.xlabel('X coordinate')
    plt.ylabel('Y coordinate')
    plt.grid(False) # Turn off default grid since we drew custom cells
    
    # Save the plot explicitly just in case, before showing
    plt.savefig('visualization.png')
    print("Saved plot to visualization.png")
    
    # Show the interactive plot window
    try:
        plt.show(block=False)
        plt.pause(2)
        plt.close()
    except Exception:
        pass

if __name__ == '__main__':
    main()
