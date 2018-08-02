class ConstraintViolationError(AttributeError):
    def __init__(self, violatoins=None):
        self._violations = violatoins if violatoins else []

    @property
    def violations(self):
        return self._violations
