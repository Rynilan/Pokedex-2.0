from tkinter import Entry


class Entry(Entry):
    def __init__(self: object, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def custom_get(self: object,
                   validation_function=None,
                   formatting_function=None) -> str:
        value = self.get()
        if validation_function:
            if not validation_function(value):
                raise ValueError('Valor {} inválido'.format(value))
        if formatting_function:
            return formatting_function(value)
        return value
