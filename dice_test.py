from dice import*

die6 =  Die(6,[0,0,0,0,0,6])


def test_setProbabilities():
	assert die6.setProbabilities() == ['6', '6', '6', '6', '6', '6']


def test_roll():
	die6.value = 6

factory20 = DiceFactory(20)

def test_make_die():
	assert factory20.make_die() == 9

