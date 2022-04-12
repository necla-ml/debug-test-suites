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

int_to_class = ["different", "same"]

for i, b in enumerate(suite.tests):
  name = re.sub(r"[^0-9a-zA-Z]", "_", b, count=0)
  name = "%03d" % i + "_" + name

  labels = suite.tests[b].labels
  if(type(labels) == type([]) or type(labels) == type(1)):
    d = suite.tests[b].data
    # print(name, str(type(suite.tests[b].labels)), "data", str(type(d[0])))

    type_dir = os.path.join(out_dir, name)
    os.mkdir(type_dir)

    train_fp = open(os.path.join(out_dir, name, "train.jsonl"), "w")
    test_fp = open(os.path.join(out_dir, name, "test.jsonl"), "w")

    # print(name, type(d[0]), len(d[0]), str(type(())))

    for j, x in enumerate(d):
      if(type(x) == type([])):
        for k, y in enumerate(x):
          example = {"index": name + ":%04d" % j + ":%02d" % k, "question1": y[0], "question2": y[1]}
          if(type(labels) == type([])):
            example["label"] = int_to_class[labels[j][k]]
          elif(type(labels) == type(1)):
            example["label"] = int_to_class[labels]
          else:
            raise ValueError("Weird label type")

          if j < 10:
            train_fp.write(json.dumps(example) + "\n")
          else:
            test_fp.write(json.dumps(example) + "\n")

      else:          
        example = {"index": name + ":%04d" % j, "question1": x[0], "question2": x[1]}
        if(type(labels) == type([])):
          example["label"] = int_to_class[labels[j]]
        elif(type(labels) == type(1)):
          example["label"] = int_to_class[labels]
        else:
          raise ValueError("Weird label type")

        if j < 10:
          train_fp.write(json.dumps(example) + "\n")
        else:
          test_fp.write(json.dumps(example) + "\n")

    train_fp.close()
    test_fp.close()

