def to_camel_case(snake_str):
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


file = open("input.txt", "r")
lines = file.readlines()
for upper_snake in lines:
    upper_snake = upper_snake.rstrip()
    camel = to_camel_case(upper_snake.lower())
    print(f"""
public TestHttpResponse is{camel}() {{ 
    checkState(actual().equals(HttpStatus.{upper_snake}), "\\nexpected: %s\\n but was: %s", HttpStatus.{upper_snake}, actual());
    return back();
}}""")

"""
TestHttpResponse isContinue(HttpStatus status) {
    assertThat(actual()).isEqualTo(HttpStatus.CONTINUE);
    return back();
}
"""
