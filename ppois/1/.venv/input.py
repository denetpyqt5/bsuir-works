class ValidInput:
    def valid_int_input(self, left : int, right: int, text: str) -> int:
        while True:
            try:
                data = int(input(text))
                if left <= data <= right:
                    return data
            except Exception:
                print("Wrong data. Try one more time")
