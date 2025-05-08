#!/usr/bin/python3
for i in range(0, 11):
  print("Table for ", i, ":", end=" ")
  for j in range(1, 11):
    print("{}".format(i * j), end=" ")
  print()