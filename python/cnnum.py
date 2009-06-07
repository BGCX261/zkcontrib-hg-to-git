# -*- encoding: utf-8 -*-

# Translate Chinese digits to Arabic digit and vice versa
# Author: Zeng Ke
# Email:  superisaac.ke@gmail.com

def to_unicode(*args):
    return map(lambda x: unicode(x, 'utf-8'), args)

cn_digits = to_unicode('零', '一', '二', '三', '四', '五', '六', '七', '八', '九'))
cn_quantifier = to_unicode('十', '百', '千', '万', '亿 ')

def get_index(cndigit):
    try:
        return cn_digits.index(cndigit)
    except ValueError:
        return -1

def cn_2_arab(cn_digits):
    """
    >>> cn_2_arab('二千零一')
    2001
    >>> cn_2_arab('二千一')
    2100
    >>> cn_2_arab('一万二千三百四十五')
    12345
    >>> cn_2_arab('十二')
    12
    >>> cn_2_arab('二十二')
    22
    """
    

    

