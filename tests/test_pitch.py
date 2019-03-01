
import unittest
from app.models import Pitch, User


class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


    def test_save_Pitch(self):
       
        self.new_Pitch.save_Pitch() # saving the new Credentials
        self.assertTrue(len(Pitch.query.all()>0)

    def test_get_pitch_by_id(self):

        self.new_Pitch.save_Pitch()
        got_pithcz = Pitch.get_pitche
