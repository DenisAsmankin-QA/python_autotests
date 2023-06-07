import requests
import pytest

host = 'https://pokemonbattle.me:9104'

def test_status_code():
    trainer = requests.get(f'{host}/trainers', params = {'trainer_id' : 4673})
    assert trainer.status_code == 200

def test_include():
    trainer_include = requests.get(f'{host}/trainers', params = {'trainer_id' : 4673})
    assert trainer_include.json()['trainer_name'] == 'Finish'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Finish'),
                                        ('city', 'Ekb'),
                                        ('get_history_battle', '0'),
                                        ('id', '4673')])                       #параметризация

def test_include_parts(key, value):
    trainer_include_parts = requests.get(f'{host}/trainers', params = {'trainer_id' : 4673})
    assert trainer_include_parts.json()[key] == value