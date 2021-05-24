import numpy as np
import pandas as pd
import pytest
from hfmodule import helper_functions as hf


def test_rand_state_df():
    df = pd.DataFrame(
        data={
            "A": (1, 2, 3),
            "B": (4, 5, 6),
            "C": (7, 8, 9)
        }
    )
    rand_df = hf.RandomDataFrame(df=df, random_state=25)
    r1 = rand_df.randomize()
    r2 = rand_df.randomize()
    assert not (np.array_equal(np.array(df.index), np.array(r2.index)))
    assert (np.array_equal(np.array(r1.index), np.array(r2.index)))
