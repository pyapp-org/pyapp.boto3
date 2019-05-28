from pyapp.app import CliApplication, argument

import sample

app = CliApplication(
    sample, name="PyApp Sample", description="Sample pyApp application."
)


@app.command
def foo(opts):
    print("bar")


if __name__ == "__main__":
    app.dispatch()
