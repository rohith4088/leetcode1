def slow_week():
    seconds_per_day = 86400
    return 7 * seconds_per_day

import ast , inspect , pprint

pprint.pprint(
    ast.dump(
        ast.parse(
            inspect.getsource(slow_week)
        )
    )
)


import dis
dis.dis(slow_week)

# print(
# slow_week.__code__,
# slow_week.__code__.co_code,
# slow_week.__code__.co_argcount
# )


# a , b = 1000,1000
# print(a is b)
# c ,d = 4.2 ,4.2
# print(c is d)

tree = ast.parse("print('hello world')")
exec(compile(tree , filename="<ast>" , mode = "exec"))


