# Solve
- `..//fl../ag.txt.txt`
- `..//fl../ag.txt../`

# Notes
- Path traversal with sanitization
- `os.path.join` semantics ([docs](https://docs.python.org/3/library/os.path.html#os.path.join)):
    > If a segment is an absolute path (which on Windows requires both a drive and a root), then all previous segments are ignored and joining continues from the absolute path segment.