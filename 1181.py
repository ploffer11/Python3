print(
    *sorted(
        list(
            set(
                [input() for j in range(int(input()))]
            )
        ),key=lambda x :(len(x), x)
    )
)