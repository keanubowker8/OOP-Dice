from dice import*
import random
random.seed(9001)
import pytest


die6 =  Die(6,[0,0,0,0,0,6])
die5 =  Die(6,[-1,0,0,0,0,6])
die4 =  Die(6,[0,0,0,0,0,0])


def test_setProbabilities():
	assert die6.setProbabilities() == ['6', '6', '6', '6', '6', '6']
	with pytest.raises(Exception):
		assert die5.setProbabilities() == Exception('negative probabilities not allowed')
		assert die4.setProbabilities() == Exception('probability sum must be greater than 0')


def test_roll():
	die6.roll()
	assert die6.value == '6'
	with pytest.raises(Exception):
		die5.roll()
		assert die6.value == Exception('negative probabilities not allowed')
		die4.roll()
		assert die6.value == Exception('probability sum must be greater than 0')


factory20 = DiceFactory(20)

def test_make_die():
	assert factory20.make_die() == 10

