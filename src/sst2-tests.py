import json
import sys
import re
import os
import checklist
from checklist.test_suite import TestSuite

if(len(sys.argv) != 3):
  raise ValueError("Usage")

in_pkl_file = sys.argv[1]
out_dir = sys.argv[2]

suite = TestSuite.from_file(in_pkl_file)

int_to_class = ["negative", "neutral", "positive"]

for i, b in enumerate(suite.tests):
  name = re.sub(r"[^0-9a-zA-Z]", "_", b, count=0)
  name = "%03d" % i + "_" + name

  labels = suite.tests[b].labels
  if(type(labels) == type([]) or type(labels) == type(1)):
    has_neutral = False
    if(labels == 1):
      has_neutral = True
    elif(type(labels) == type([])):
      for k in labels:
        if k == 1:
          has_neutral = True
    if has_neutral:
      continue

    d = suite.tests[b].data
    print(name, str(type(suite.tests[b].labels)), "data", str(type(d[0])))

    type_dir = os.path.join(out_dir, name)
    os.mkdir(type_dir)

    train_fp = open(os.path.join(out_dir, name, "train.jsonl"), "w")
    test_fp = open(os.path.join(out_dir, name, "test.jsonl"), "w")

    for j, text in enumerate(d):
      example = {"index": name + ":%04d" % j, "sentence": text}
      if(type(labels) == type(1)):
        example["label"] = int_to_class[labels]
      else:
        example["label"] = int_to_class[labels[j]]

      if j < 10:
        train_fp.write(json.dumps(example) + "\n")
      else:
        test_fp.write(json.dumps(example) + "\n")

    train_fp.close()
    test_fp.close()

