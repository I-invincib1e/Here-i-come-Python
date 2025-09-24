"""
DSA algorithm visualizations using matplotlib.
Provides visual learning tools for understanding algorithms.
"""

try:
    import matplotlib.pyplot as plt
    import numpy as np
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    plt = None
    np = None


def check_visualization_dependencies():
    """Check if visualization dependencies are available."""
    if not HAS_MATPLOTLIB:
        raise ImportError(
            "Visualization requires matplotlib and numpy. "
            "Install with: pip install -e .[visualization]"
        )
