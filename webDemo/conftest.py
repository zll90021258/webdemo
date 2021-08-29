
import pytest
from webDemo.common.constants import BASE_DIR
from webDemo.common.delFiles import del_file
@pytest.fixture(scope="session",autouse=True)
def clean_file():
    del_file(path=BASE_DIR)


