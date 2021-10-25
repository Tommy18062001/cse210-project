from game.score import Score
import pytest

class TestScore:
    """
        Code template for testing the Score class. 
    """
        
    def test_update_score(self):
        """This will make sure that the function update score is working properly
        """
        score = Score()
        score.update_score(5)
        assert score.score == 5

pytest.main(["-v", "--tb=line", "-rN", "test_score.py"]) 