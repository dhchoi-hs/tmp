# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import os


print(os.uname())
# -

# ##
# ** hello **
# * MD cell 1
#

# '''MD test cell 2'''

# """asdf""" 
# `ss`
# ``ss``

#

# +
a = 1234
b = 'hello'

print(a, b)
# -

# ZZ

C = [1,2,3]
C.append(44)

# +
f = 'fdsa'

dd = 'zzz'
gg = f+dd


# +
def func():
    return 1

print(func())
print("END")
print(321)

