## Environment Testing
_These instructions are for testing that the environment was correctly installed on the SARP computers_

1. Run/open `jupyter lab`
2. Create a new notebook with `Python [conda env:sarp]` as the kernel
3. Copy and paste the code from `test_env.py` into a cell and run it. If the code runs without error the test was successful.
4. Back in a terminal window run `conda install -n sarp plotly --yes`. This tests that the user can install additional libraries in their environment without problems.
