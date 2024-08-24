class Suitor:
    def __init__(self, id, preference_list):
        self.preference_list = preference_list
        self.index_to_propose_to = 0
        self.id = id

    def preference(self):
        return self.preference_list[self.index_to_propose_to]

    def post_rejection(self):
        self.index_to_propose_to += 1

    def __str__(self):
        return str(self.id)


class Suited:
    def __init__(self, id, preference_list):
        self.preference_list = preference_list
        self.held = None
        self.current_suitors = set()
        self.id = id

    def reject(self):
        """Return the subset of Suitors in self.current_suitors to reject,
        leaving only the held Suitor in self.current_suitors.
        """
        if len(self.current_suitors) == 0:
            return set()
        self.held = min(
            self.current_suitors,
            key=lambda suitor: self.preference_list.index(suitor.id),
        )
        rejected = self.current_suitors - {self.held}
        self.current_suitors = {self.held}
        return rejected

    def add_suitor(self, suitor):
        self.current_suitors.add(suitor)

    def __str__(self):
        return str(self.id)


def stable_marriage(suitors, suiteds):
    """Construct a stable marriage between Suitors and Suiteds."""
    unassigned = set(suitors)
    while len(unassigned) > 0:
        for suitor in unassigned:
            next_to_propose_to = suiteds[suitor.preference()]
            next_to_propose_to.add_suitor(suitor)
        unassigned = set()
        for suited in suiteds:
            unassigned |= suited.reject()  # python set union operator
        for suitor in unassigned:
            suitor.post_rejection()  # have some ice cream
    return dict([(suited.held, suited) for suited in suiteds])


suitors = [
    Suitor(0, [3, 5, 4, 2, 1, 0]),
    Suitor(1, [2, 3, 1, 0, 4, 5]),
    Suitor(2, [5, 2, 1, 0, 3, 4]),
    Suitor(3, [0, 1, 2, 3, 4, 5]),
    Suitor(4, [4, 5, 1, 2, 0, 3]),
    Suitor(5, [0, 1, 2, 3, 4, 5]),
]

suiteds = [
    Suited(0, [3, 5, 4, 2, 1, 0]),
    Suited(1, [2, 3, 1, 0, 4, 5]),
    Suited(2, [5, 2, 1, 0, 3, 4]),
    Suited(3, [0, 1, 2, 3, 4, 5]),
    Suited(4, [4, 5, 1, 2, 0, 3]),
    Suited(5, [0, 1, 2, 3, 4, 5]),
]

d = stable_marriage(suitors, suiteds)
for k, v in d.items():
    print(k, v)
