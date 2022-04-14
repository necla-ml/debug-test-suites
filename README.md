# Fast Few-shot Debugging for NLU Test Suites

This repository contains the test suites used in the paper,
["Fast Few-shot Debugging for NLU Test Suites"](https://arxiv.org/abs/2204.06555).
They are derived from test suites in [HANS](https://github.com/tommccoy1/hans)
by Tom McCoy et al. and [CheckList](https://github.com/marcotcr/checklist)
by Marco Ribeiro et al..

For each test suite, `train.jsonl` contains the ten examples used
for debugging.  The remainder of the test suite is used for testing,
in `test.jsonl`.  The file `train-plus.jsonl` contains the ten debugging
examples together with the up to twenty newly misclassified examples
collected from the original training set (MultiNLI, Quora Question Pairs,
or SST-2).

## Test extraction tool for CheckList

We also include scripts for extracting individual debugging examples
from the Pickle files included in CheckList repositories.
To run it, you should first install CheckList in your Python path
following the instructions in the
[CheckList repository](https://github.com/marcotcr/checklist).
In the CheckList source tree, you have Pickle files
containing the original test suites in the `release_suites` directory.
You may collect the ten debugging examples and remaining test examples for
each suite with
```
mkdir qqp-suites
python src/qqp-tests.py release_suites/qqp_suite.pkl qqp-suites
mkdir sst2-suites
python src/sst2-tests.py release_suites/sentiment_suite.pkl sst2-suites
```
This procedure reproduces the training and testing files included in this
repository, but we only include the suites where accuracy before debugging
is worst.

## Citation

If you use our few-shot test suites, please cite our ACL 2022 workshop paper:

```
@inproceedings{debugging,
  title={Fast Few-shot Debugging for NLU Test Suites}
  author={Malon, Christopher and Li, Kai and and Kruus, Erik},
  booktitle={Proceedings of Deep Learning Inside Out (DeeLIO): The 3rd Workshop on Knowledge Extraction and Integration for Deep Learning Architectures},
  address={Dublin, Ireland},
  year={2022}
}
```

