#! /usr/bin/env python3

from dataclasses import dataclass, field


@dataclass()
class BySize(object):
    size: int
    afile_objs: list = field(init=False)
