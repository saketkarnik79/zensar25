# class InvalidMarksError(Exception):
#     pass

class InvalidMarksError(Exception):
    def __init__(self, marks):
        self.marks = marks

        super().__init__(
            f"Invalid marks, You entered the marks as: {marks}"
        )