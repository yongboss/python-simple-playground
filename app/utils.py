def reverse_string(s):
    """Return s reversed."""
    return s[::-1]

def is_palindrome(s):
    """Return True if s reads the same backwards."""
    return s == s[::-1]

def chunk(xs, n):
    """Split xs into lists of size n."""
    return [xs[i:i + n] for i in range(0, len(xs), n)]

def flatten(xss):
    """Flatten one level of nesting."""
    return [x for xs in xss for x in xs]
