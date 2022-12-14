
class MockReporter:
    def __init__(self):
        pass

    def warning(self, description, line):
        pass

    def debug(self, message):
        pass


class MockDocument:
    def __init__(self):
        self.reporter = MockReporter()
