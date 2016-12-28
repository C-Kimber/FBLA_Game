def neighborhood(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)


def connectTextures(txt = open("./assets/long_levels/level_0")):
    txt = txt
    text = []
    col = []
    for x in txt: #Rows
        for y in x: #Collums
            if y == "\n":
                continue
            col.append(y)
        text.append(col)
        col = []
        #print text
    m =0
    n = 0
    for y in text:
        for x in y:
            if m - 1 >= 0 and m + 1 <= 37:
                if n-1 >= 0 and n+1 <= 119:#
                    cur = y[n] #current AKA Middle
                    left = y[n - 1]
                    right = y[n + 1]
                    top = text[m - 1][n]
                    bot = text[m + 1][n]
                    f = "."
                    if cur == "-":
                        if left == "-":
                            if right == "-":
                                if bot == "-":
                                    if top == "-":
                                        f = "4" #Surrounded
                                    else:
                                        f = "1"
                                elif top == "-":
                                    f = "7"
                                else:
                                    f = "1"
                            elif top == "-":
                                f = "8"
                            elif bot == "-":
                                f = "2"
                            else:
                                f = "2"
                            #elif:
                        elif right == "-": #NO LEFT
                            if top == '-':
                                if bot == "-":
                                    f = "3"
                                else:
                                    f = "6"
                            elif bot == "-":
                                f = "0"
                            else:
                                f = "0"
                        elif top == "-": #NO LEFT OR RIGHT
                            if bot == "-":
                                f = "4"
                            else:
                                f = "7"
                        elif bot == "-": #NO LEFT, RIGHT, OR UP
                            f = "1"

                        else:
                            f = "1"
                    print y[n + 1], f, y[n-1]
                    print text[m + 1][n - 1], text[m + 1][n], text[m + 1][n + 1]

            n += 1
        m += 1

        n = 0

