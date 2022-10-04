import sys

notation = {
    "---": "0",
    "--x": "1",
    "-w-": "2",
    "-wx": "3",
    "r--": "4",
    "r-x": "5",
    "rw-": "6",
    "rwx": "7",
}


def symb_to_num(symbolic):
    """
    Convert symbolic permission notation to numeric notation.
    """

    if len(symbolic) == 9:
        group = (symbolic[:-6], symbolic[3:-3], symbolic[6:])
        try:
            numeric = (
                notation[group[0]] + notation[group[1]] + notation[group[2]]
            )
        except:
            numeric = "Invalid Symbolic Representation!"
    else:
        numeric = "Symbolic input should be of lengh 9!"

    return numeric


def num_to_symb(num):
    """
    Convert number permission notation to symbolic notation.
    """

    num = str(num)
    if len(num) == 3:
        group = (num[0], num[1], num[2])
        symbolic = ""

        for key, value in notation.items():
            for g in group:
                if int(g) > 8 or int(g) < 0:
                    symbolic = "Invalid Numerical Representation!"
                elif g == value:
                    symbolic = symbolic + key
    else:
        symbolic = "Number input should be of length 3!"

    return symbolic


def main():
    representation = sys.argv[1]
    mode = sys.argv[2]
    if mode == "S":
        print(num_to_symb(representation))
    elif mode == "N":
        print(symb_to_num(representation))
    else:
        print(
            "Invalid Mode Selection. Please select 'S' for numerical --> symbolic conversion or 'N' for symbolic --> numerical conversion!"
        )


if __name__ == "__main__":
    main()
