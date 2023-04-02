#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import request


r = request.get("https://httpbin.org/ip")

print(r.status())
