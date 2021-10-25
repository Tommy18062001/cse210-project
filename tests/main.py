"""Initiate test directory"""

import pytest
from pathlib import Path

#root_dir = Path(__file__).parent
#path_to_point = root_dir / "point.py"


pytest.main(["-v", "--tb=line", "-rN", "test_point.py"])
pytest.main(["-v", "--tb=line", "-rN", "test_actor.py"])
pytest.main(["-v", "--tb=line", "-rN", "test_score.py"])
pytest.main(["-v", "--tb=line", "-rN", "test_director.py"])
