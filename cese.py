#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-03-24 04:08:46
# @Author  : 崔立波 (baiyuexingchen@gmail.com)
# @Link    : http://blog.sina.com.cn/dejavu1
# @Version : 1


import os
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import time
import sys
import requests
import bs4
import csv
import datetime
import json
from envelopes import Envelope
import exifread
from faker import Faker
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#fake = Faker("zh_CN")
###############################################
#以下开始