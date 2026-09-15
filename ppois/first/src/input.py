class ValidInput:
    def _is_valid(self, data, left, right):
        return isinstance(data, int) and left <= data <= right

    def _parse(self, raw, left, right):
        try:
            data = int(raw)
        except (ValueError, TypeError):
            return None
        return data if self._is_valid(data, left, right) else None

    def valid_int_input(self, left, right, text):
        while True:
            data = self._parse(input(text), left, right)
            if data is not None:
                return data
            print("Wrong data. Try one more time")