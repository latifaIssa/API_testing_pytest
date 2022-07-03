import pytest
import traceback

# use pytest.raises() raised exceptions
def f():
    raise SystemExit(0)

def test_mytest():
    with pytest.raises(SystemExit):
        f()


def test_zero_division():
    print("Latifa")

    with pytest.raises(ZeroDivisionError):
        1 / 0


# excinfo is an ExceptionInfo instance, which is a wrapper around the actual exception raised. The main attributes of interest are .type, .value and .traceback.

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()


        f()
        print(str(excinfo.traceback))
    assert "maximum recursion" in str(excinfo.value)
    assert "RecursionError" in str(excinfo.type)

    # assert "maximum recursion depth exceeded" in str(excinfo.traceback)