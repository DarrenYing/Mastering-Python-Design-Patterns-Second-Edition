from rx import from_, operators


def get_quotes():
    import contextlib, io
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        pass

    quotes = zen.getvalue().split('\n')[1:]
    return enumerate(quotes)


zen_quotes = get_quotes()

from_(zen_quotes).pipe(
    operators.filter(lambda q: len(q[1]) > 0)
).subscribe(lambda value: print(f"Received: {value[0]} - {value[1]}"))
