from pendu import pendu


def test_pendu():

    res = pendu.play(word="ENFANT", nb_tries=3, letters=["E", "N", "F","A", "T"])

    assert res, "user whould have won this game, finding word ENFANT"


def test_pendu_fail():
    res = pendu.play(word="ENFANT", nb_tries=1, letters=["T", "P"])

    assert res == False, "user whould have fail this game"

