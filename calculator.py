#!/usr/bin/env python3
"""一个简单的命令行 Python 计算器。"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("除数不能为 0")
    return a / b


def main() -> None:
    print("=== Python 计算器 ===")
    print("支持运算: +  -  *  /")

    while True:
        expr = input("请输入表达式（例如 1 + 2，输入 q 退出）: ").strip()
        if expr.lower() in {"q", "quit", "exit"}:
            print("已退出计算器。")
            break

        parts = expr.split()
        if len(parts) != 3:
            print("输入格式错误，请使用：数字 运算符 数字")
            continue

        left, op, right = parts
        try:
            a = float(left)
            b = float(right)
        except ValueError:
            print("数字格式错误，请输入有效数字。")
            continue

        try:
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print("不支持的运算符，请使用 + - * /")
                continue

            if result.is_integer():
                print(f"结果: {int(result)}")
            else:
                print(f"结果: {result}")
        except ZeroDivisionError as exc:
            print(f"错误: {exc}")


if __name__ == "__main__":
    main()
