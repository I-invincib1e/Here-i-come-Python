"""
Visualization for Kadane's algorithm (Maximum Subarray Sum).
Shows the step-by-step process of finding the maximum contiguous subarray.
"""

from typing import List, Optional
from . import check_visualization_dependencies, plt, np


def visualize_kadane_algorithm(arr: List[int], step_by_step: bool = True,
                              save_path: Optional[str] = None) -> None:
    """
    Visualize Kadane's algorithm execution.

    Args:
        arr: Input array of integers
        step_by_step: If True, show each step interactively
        save_path: Optional path to save the final visualization
    """
    check_visualization_dependencies()

    if not arr:
        print("Empty array provided")
        return

    # Algorithm execution with state tracking
    max_current = max_global = arr[0]
    start = end = 0
    temp_start = 0

    # Track state at each step for visualization
    states = [{
        'step': 0,
        'current': arr[0],
        'global': arr[0],
        'current_subarray': [0, 0],  # start, end indices
        'global_subarray': [0, 0],
        'temp_start': 0
    }]

    for i in range(1, len(arr)):
        # Kadane's algorithm logic
        if arr[i] > max_current + arr[i]:
            max_current = arr[i]
            temp_start = i
        else:
            max_current += arr[i]

        if max_current > max_global:
            max_global = max_current
            start = temp_start
            end = i

        # Record state
        states.append({
            'step': i,
            'current': max_current,
            'global': max_global,
            'current_subarray': [temp_start, i],
            'global_subarray': [start, end],
            'temp_start': temp_start
        })

    # Create visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle("Kadane's Algorithm: Maximum Subarray Sum", fontsize=16)

    # Plot the array
    x = np.arange(len(arr))
    bars = ax1.bar(x, arr, color='lightblue', alpha=0.7)

    # Add value labels on bars
    for i, v in enumerate(arr):
        ax1.text(i, v + max(arr) * 0.02, str(v), ha='center', va='bottom' if v >= 0 else 'top')

    ax1.set_title('Input Array')
    ax1.set_xlabel('Index')
    ax1.set_ylabel('Value')
    ax1.grid(True, alpha=0.3)

    # Current and Global max tracking
    steps = [s['step'] for s in states]
    current_maxes = [s['current'] for s in states]
    global_maxes = [s['global'] for s in states]

    ax2.plot(steps, current_maxes, 'b-o', label='Current Max', linewidth=2, markersize=6)
    ax2.plot(steps, global_maxes, 'r-s', label='Global Max', linewidth=2, markersize=6)
    ax2.set_title('Algorithm Progress')
    ax2.set_xlabel('Step')
    ax2.set_ylabel('Sum Value')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Add final result annotation
    final_global = states[-1]['global']
    final_subarray = states[-1]['global_subarray']
    ax2.annotate(f'Final Max Sum: {final_global}\nSubarray: [{final_subarray[0]}, {final_subarray[1]}]',
                xy=(len(states)-1, final_global),
                xytext=(len(states)-2, final_global + max(global_maxes) * 0.1),
                arrowprops=dict(arrowstyle='->', color='red'),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.8))

    plt.tight_layout()

    if step_by_step:
        _show_step_by_step_visualization(arr, states, bars)
    else:
        # Highlight final subarray
        for i in range(final_subarray[0], final_subarray[1] + 1):
            bars[i].set_color('orange')
            bars[i].set_alpha(0.9)

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Visualization saved to: {save_path}")

    plt.show()


def _show_step_by_step_visualization(arr: List[int], states: List[dict], bars):
    """Show step-by-step visualization with user interaction."""
    print("\n" + "="*60)
    print("KADANE'S ALGORITHM STEP-BY-STEP VISUALIZATION")
    print("="*60)
    print("At each step, press Enter to continue...")

    for state in states:
        step = state['step']
        current = state['current']
        global_max = state['global']
        current_subarray = state['current_subarray']
        global_subarray = state['global_subarray']

        print(f"\nStep {step}:")
        print(f"  Current element: {arr[step] if step < len(arr) else 'N/A'}")
        print(f"  Current max sum: {current}")
        print(f"  Global max sum: {global_max}")
        print(f"  Current subarray: indices {current_subarray}")
        print(f"  Global subarray: indices {global_subarray}")

        # Update visualization
        # Reset all bars
        for bar in bars:
            bar.set_color('lightblue')
            bar.set_alpha(0.7)

        # Highlight current subarray (blue)
        for i in range(current_subarray[0], current_subarray[1] + 1):
            bars[i].set_color('blue')
            bars[i].set_alpha(0.9)

        # Highlight global subarray (orange)
        for i in range(global_subarray[0], global_subarray[1] + 1):
            bars[i].set_color('orange')
            bars[i].set_alpha(0.9)

        plt.pause(0.1)  # Small pause for update
        plt.draw()

        # Wait for user input
        try:
            input("Press Enter for next step...")
        except KeyboardInterrupt:
            print("\nVisualization interrupted by user")
            break

    print("\n" + "="*60)
    print("VISUALIZATION COMPLETE")
    print("="*60)
    print(f"Final result: Maximum subarray sum = {states[-1]['global']}")
    print(f"Subarray indices: {states[-1]['global_subarray']}")


def demonstrate_kadane_visualization():
    """Demonstrate Kadane's algorithm visualization with example data."""
    # Classic example from the algorithm
    example_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print("Visualizing Kadane's Algorithm")
    print(f"Input array: {example_array}")
    print("\nBlue bars: Current subarray being considered")
    print("Orange bars: Best subarray found so far")
    print("The algorithm finds the maximum sum contiguous subarray.")

    try:
        visualize_kadane_algorithm(example_array, step_by_step=True)
    except ImportError as e:
        print(f"Visualization not available: {e}")


if __name__ == "__main__":
    demonstrate_kadane_visualization()
