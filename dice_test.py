from dice import*

die6 =  Die(6,[0,0,0,0,0,6])


def test_setProbabilities():
	assert die6.setProbabilities() == ['6', '6', '6', '6', '6', '6']


def test_roll():
	die6.value = 6s