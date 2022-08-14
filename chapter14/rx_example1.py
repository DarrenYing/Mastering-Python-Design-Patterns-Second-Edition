from rx import create


def get_quotes():
    import contextlib, io
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this

    quotes = zen.getvalue().split('\n')[1:]
    return quotes


def push_quotes(obs, scheduler):
    quotes = get_quotes()
    for q in quotes:
        if q:  # skip empty
            obs.on_next(q)
    obs.on_completed()


class ZenQuotesObserver:

    def on_next(self, value):
        print(f"Received: {value}")

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print(f"Error Occurred: {error}")


source = create(push_quotes)

source.subscribe(ZenQuotesObserver())  # 订阅之后，push_quotes函数才会执行
