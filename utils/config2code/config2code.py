# 将复杂的配置转换成 python 代码
from numbers import Number


def config2code(d):
    global stack
    global code
    for key, value in d.items():

        # 将 key 添加到列表中，注意只添加key，不添加 value
        stack.append(key)

        # 如果 value 还是一个字典，则递归执行 config2code
        if isinstance(value, dict):
            config2code(value)
            # dict1: {"key1": "value1"} 此处这个 key 是 dict1
            stack.pop()

        # 如果 value 不是一个字典，则直接打印表达式，这也是递归的基线条件
        else:

            # 如果是数值型，转换成数值类型，否则为字符串
            if isinstance(value, (int, float, list)) or value is None:
                code.write("_".join(stack) + ' = data.get("%s", %s)\n' % (stack[-1], value))
            else:
                code.write("_".join(stack) + ' = data.get("%s", "%s")\n' % (stack[-1], value))

            # 更改value
            d[stack[-1]] = "$" + "_".join(stack) + "$"

            # dict1: {"key1": "value1"} 此处这个 key 是key1
            stack.pop()


if __name__ == '__main__':
    import json

    with open("./config.json", 'r', encoding="utf-8") as f:
        # \ 需要转义
        config_str = f.read().replace("\\", "\\\\")
        try:
            # 存放 key 的列表
            stack = []
            # 转换后的文件，并清空
            code = open("code.py", 'a', encoding="utf-8")
            code.seek(0)
            code.truncate()

            # json 形式的 config 文件
            config = json.loads(config_str)

            config2code(config)

            # 原始配置在递归中也被改变，存储改变后的配置文件
            with open("config_handle.json", "w", encoding="utf-8") as c:
                json.dump(config, c)

        finally:
            code.close()
