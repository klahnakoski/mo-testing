from mo_logs import logger
from mo_future import Mockable, mockable


def mock(mockable, *, value=None, function=None):
    """
    FUNCTION DECORATOR TO ALLOW REPLACEMENT WITH ANOTHER function (OR value)
    """
    if function is None:
        function = _constant(value)

    return Mocking(mockable, function)


class Mocking:
    """
    REPLACE mockable WITH mock FOR THE DURATION OF THIS CONTEXT
    """

    def __init__(self, mockable, mock):
        if not isinstance(mockable, Mockable):
            logger.error("expecting Mockable, not {mockable}", mockable=mockable, stack_depth=1)
        self.mockable = mockable
        self.mock = mock
        self.func = None

    def __enter__(self):
        self.func, self.mockable.func = self.mockable.func, self.mock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.func, self.mockable.func = None, self.func

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            with self:
                return func(*args, **kwargs)

        return wrapped


def _constant(value):
    def f(*args, **kwargs):
        return value

    return f
