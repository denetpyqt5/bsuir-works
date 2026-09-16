class ValidInput:
    """Utility for reading and validating integer input from the user.

    The validator keeps asking until the user provides a value that
    parses as an integer and falls within the inclusive range
    ``[left, right]``. Invalid entries trigger a message and a retry.
    """
    def _is_valid(self, data, left, right):
        """Check whether a value is an integer within the given range.

        :param data: value to check
        :param left: lower bound (inclusive)
        :param right: upper bound (inclusive)
        :return: ``True`` if ``data`` is an ``int`` and
            ``left <= data <= right``, ``False`` otherwise
        """
        return isinstance(data, int) and left <= data <= right

    def _parse(self, raw, left, right):
        """Parse a raw string into a valid integer within a range.

        Attempts to convert ``raw`` to ``int`` and then validates the
        result against ``[left, right]``.

        :param raw: raw user input (usually from ``input()``)
        :param left: lower bound (inclusive)
        :param right: upper bound (inclusive)
        :return: the parsed integer if it is valid, or ``None`` if
            parsing failed or the value is out of range
        """
        try:
            data = int(raw)
        except (ValueError, TypeError):
            return None
        return data if self._is_valid(data, left, right) else None

    def valid_int_input(self, left, right, text):
        """Prompt the user until a valid integer in range is entered.

        Repeatedly prints ``text`` and reads a line from standard
        input. If the entered value cannot be parsed as an integer,
        or falls outside ``[left, right]``, prints an error message
        and prompts again.

        :param left: lower bound (inclusive)
        :param right: upper bound (inclusive)
        :param text: prompt string shown to the user
        :return: a valid integer within ``[left, right]``
        """
        while True:
            data = self._parse(input(text), left, right)
            if data is not None:
                return data
            print("Wrong data. Try one more time")
