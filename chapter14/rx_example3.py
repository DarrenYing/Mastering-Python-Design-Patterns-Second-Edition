from rx import interval, from_, of
from rx import operators as ops
import rx


def get_quotes():
    import contextlib, io
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this

    quotes = zen.getvalue().split('\n')[1:]
    return enumerate(quotes)


zen_quotes = get_quotes()

interval(1).pipe(
    ops.flat_map(lambda seq: from_(zen_quotes)),
    ops.flat_map(lambda q: from_(q[1].split())),
    ops.filter(lambda s: len(s) > 2),
    ops.map(lambda s: s.replace('.', '').replace(',', '').replace('!', '').replace('-', '')),
    ops.map(lambda s: s.lower()),
).subscribe(lambda value: print(f"Received: {value}"))

input("Starting... Press any key to quit\n")