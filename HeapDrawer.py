# import packages
import matplotlib.pyplot as plt

# Render an image of the array as a heap
def drawHeap(heap, image_name='heap_plot.png'):
    # Get the height of the heap
    height = 0
    while 2**height <= len(heap):
        height += 1
    height -= 1

    # Get the width of the heap
    width = 2**height - 1

    # Prepare to assign positions
    x_positions = [0]*len(heap)
    y_positions = [0]*len(heap)
    x_current = [0]  # Use list to make it mutable in nested function

    def assign_positions(index, depth):
        if index >= len(heap):
            return
        # Left child
        assign_positions(2*index+1, depth+1)

        # Assign position to current node
        x_positions[index] = x_current[0]
        y_positions[index] = depth
        x_current[0] += 1

        # Right child
        assign_positions(2*index+2, depth+1)

    # Start position assignment
    assign_positions(0, 0)

    # Now plot the heap
    fig, ax = plt.subplots()

    # Draw edges
    for i in range(len(heap)):
        # Left child
        left_index = 2*i +1
        if left_index < len(heap):
            ax.plot([x_positions[i], x_positions[left_index]],
                    [-y_positions[i], -y_positions[left_index]], 'k-')

        # Right child
        right_index = 2*i +2
        if right_index < len(heap):
            ax.plot([x_positions[i], x_positions[right_index]],
                    [-y_positions[i], -y_positions[right_index]], 'k-')

    # Draw nodes
    for i in range(len(heap)):
        ax.plot(x_positions[i], -y_positions[i], 'ro')
        ax.text(x_positions[i], -y_positions[i], str(heap[i]),
                ha='center', va='center', fontsize=12,
                bbox=dict(facecolor='white', edgecolor='none', pad=1.0))

    # Remove axes
    ax.axis('off')
    plt.savefig(image_name)

# Take comma seperated array as imput
file_name = f"heap_plot_{input('Enter the file number: ')}.png"
heap = [int(x) for x in input().split(",")]
drawHeap(heap, file_name)