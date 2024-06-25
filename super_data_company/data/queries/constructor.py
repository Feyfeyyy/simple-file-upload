from .methods import ExactMatch, PartialMatch


def get_constructor(match_type="exact"):
    if match_type == "exact":
        return ExactMatch()
    elif match_type == "partial":
        return PartialMatch()
    else:
        raise ValueError("Unsupported match type")
