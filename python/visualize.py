import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def main():
    if not os.path.exists('particles.txt'):
        print("Error: particles.txt not found. Run the Java simulation first.")
        return

    # load basic particle information
    particles = {}
    with open('particles.txt', 'r') as f:
        N = int(f.readline().strip())
        L = float(f.readline().strip())
        M = int(f.readline().strip())
        _ = f.readline().strip()  # placeholder target id written by generator (ignored)

        for _ in range(N):
            parts = f.readline().strip().split()
            p_id = int(parts[0])
            x = float(parts[1])
            y = float(parts[2])
            radius = float(parts[3])
            prop = float(parts[4])
            particles[p_id] = (x, y, radius, prop)

    # ask user which particle to analyze
    try:
        target = int(input("Enter target particle id: "))
    except Exception:
        print("Invalid input, using 0 as default target.")
        target = 0

    # read neighbours from output.txt
    neighbors = set()
    if os.path.exists('output.txt'):
        with open('output.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if not line or line[0] != '[':
                    continue
                tokens = line.replace('[', '').replace(']', '').split()
                pid = int(tokens[0])
                if pid == target:
                    for tok in tokens[1:]:
                        neighbors.add(int(tok))
                    break
    else:
        print("Warning: output.txt not found, neighbour information unavailable.")

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
            # Draw the interaction radius (rc) of the selected particle colored in red
            interaction_circle = patches.Circle((x, y), radius + prop, edgecolor='red', facecolor='none', linestyle='dashed', zorder=6)
            ax.add_patch(interaction_circle)
        elif p_id in neighbors:
            color = 'yellow'
            zorder = 4
        else:
            color = 'cyan'
            zorder = 3
            
        circle = patches.Circle((x, y), radius, edgecolor='black', facecolor=color, alpha=0.8, zorder=zorder)
        ax.add_patch(circle)
        # Add ID labels inside the particles
        ax.text(x, y, str(p_id), color='black', fontsize=8, ha='center', va='center', zorder=10)

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
