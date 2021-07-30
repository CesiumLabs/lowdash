import re

class RegExp:

    def __init__(self, pattern: str, _global: bool = False, _ignore: bool = False):
        self._global = _global
        self._ignore = _ignore
        self._pattern = re.compile(pattern, flags = re.I if _ignore else 0)

    def find(self, text: str):
        if self._global:
            return self._pattern.findall(text)
        else:
            result = self._pattern.search(text)
            return [result.group()] if result else []

    def replace(self, text: str, repl):
        return self._pattern.sub(repl, text, count = 0 if self._global else 1)

    def from_re(regex):
        pattern, option = regex[1:].rsplit("/", 1)
        return RegExp(pattern, "g" in option, "i" in option)