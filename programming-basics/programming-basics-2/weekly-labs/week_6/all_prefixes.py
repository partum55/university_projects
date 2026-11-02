"""Module defining the all_prefixes function."""

def all_prefixes(s: str) -> set:
    """
    Returns a set of all prefixes (in lower case) of the given string.
    For example, all_prefixes("lead") returns {"l", "le", "lea", "lead"}.
    """
    s = s.lower()
    return {s[:i] for i in range(1, len(s)+1)}
