def get_feedback(self, guess: tuple, secret: tuple) -> list:
    """Returns the feedback for a given guess."""
    # Optimized abstract algorithm (assuming correct input)
    list1 = [0] * (self.number_of_colors + 1)  # black pegs + color count of guess
    list2 = [0] * (self.number_of_colors + 1)  # white pegs + color count of secret

    # Count colors in guess and secret code
    for dot1, dot2 in zip(guess, secret):
        if dot1 == dot2:  # if exact match found
            list1[0] += 1  # black pegs count += 1
        else:  # otherwise increment the color count to find potential white pegs
            list1[dot1] += 1  # count of color in guess += 1
            list2[dot2] += 1  # count of color in secret += 1

    # Iterate through color count (skip pegs count) to count white pegs
    for count1, count2 in zip(list1[1:], list2[1:]):
        list2[0] += min(count1, count2)  # list2[0] is white pegs count

    return list1[0], list2[0]  # return black and white pegs count


class FStringTemplate:
    """A class to represent a formatted string template."""

    def __init__(self, template: str) -> None:
        """Initialize with a template string."""
        self.template = template

    def eval(self, **kwargs):
        """Evaluate the template with the given keyword arguments."""
        return self.template.format(**kwargs)
