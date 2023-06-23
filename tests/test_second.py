import os

from dotenv import load_dotenv, find_dotenv
import pytest

from src.second import YaDirectory


@pytest.fixture(scope='session')
def ya_connection():
    load_dotenv(find_dotenv())

    return YaDirectory(os.getenv('TOKEN'))


@pytest.mark.parametrize('folder_name', ['cool_folder', 'not_cool_folder'])
def test_create_folder(ya_connection, folder_name):
    if ya_connection.is_path_exists(folder_name):
        pytest.skip('folder was found before testing, not valid test')

    result = ya_connection.create_folder(folder_name)

    assert result.status_code == 201, \
        'result status code is not 201 => folder was not created'

    assert ya_connection.is_path_exists(folder_name), \
        'folder not found after creation'


@pytest.mark.skip(reason="This is obviously bad test")
def test_create_folder_(ya_connection):
    result = ya_connection.create_folder('new_folder')

    assert result.status_code == 200, \
        'result code is not 200, but it could be 201 ¯\_(ツ)_/¯'
    assert ya_connection.is_path_exists('foooooooooobaaaaaar'), \
        'folder not found'
