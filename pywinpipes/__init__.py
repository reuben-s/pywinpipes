import sys

base = sys.path[0] + "\\pywinpipes\\"
sys.path.append(sys.path[0] + "\\pywinpipes\\server")
sys.path.append(sys.path[0] + "\\pywinpipes\\bindings")
sys.path.append(sys.path[0] + "\\pywinpipes\\")

__all__ = (
    "server",
    "bindings"
)