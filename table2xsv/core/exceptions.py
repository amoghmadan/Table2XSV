class Error(Exception):
    """Every custom error should inherit from this class."""

    pass


class CommandError(Error):
    """
    Exception class indicating a problem while executing a management
    command.

    If this exception is raised during the execution of a management
    command, it will be caught and turned into a nicely-printed error
    message to the appropriate output stream (i.e., stderr); as a
    result, raising this exception (with a sensible description of the
    error) is the preferred way to indicate that something has gone
    wrong in the execution of a command.
    """

    def __init__(self, *args, return_code=1, **kwargs):
        self.return_code = return_code
        super().__init__(*args, **kwargs)


class SystemCheckError(Error):
    """
    The system check framework detected unrecoverable errors.
    """

    pass
