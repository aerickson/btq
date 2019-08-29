import os
import subprocess

import pytest


@pytest.fixture
# script working directory
def root_dir():
    swd = os.path.dirname(os.path.abspath(__file__))
    return os.path.abspath(os.path.join(swd, ".."))


def test_lvl0(root_dir):
    command = "%s/tq . %s/test/simple.toml" % (root_dir, root_dir)
    result = subprocess.run(command, shell=True, capture_output=True)
    expected = "{'title': 'TOML Example 2345'}"
    assert result.stdout.decode().strip() == expected


def test_lvl1(root_dir):
    command = "%s/tq .title %s/test/test.toml" % (root_dir, root_dir)
    result = subprocess.run(command, shell=True, capture_output=True)
    expected = "TOML Example"
    assert result.stdout.decode().strip() == expected


def test_lvl2(root_dir):
    command = "%s/tq .database.ports %s/test/test.toml" % (root_dir, root_dir)
    result = subprocess.run(command, shell=True, capture_output=True)
    expected = "[8001, 8001, 8002]"
    assert result.stdout.decode().strip() == expected