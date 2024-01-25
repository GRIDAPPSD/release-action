import os
import sys
from typing import List

from actions import io


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    # now you can access the inputs like:
    #    f"Hello {os.environ["INPUT_NAME"]}"

    # you can write to output like:
    #   io.write_to_output({var: val, ...})
    #io.write_to_output()
    print("I am here")
    for p in os.environ:
        print(p)

    print("I am here 2")
    io.write_to_output({"phrase": f"Hello {os.environ.get('INPUT_NAME', 'World')}"})


if __name__ == "__main__":
    main(sys.argv[1:])
