from uuid import UUID

from bleak.uuids import to_uuid


def test_to_uuid_16():
    uuid = to_uuid("1801")
    assert isinstance(uuid, UUID)
    assert str(uuid) == "00001801-0000-1000-8000-00805f9b34fb"


def test_to_uuid_128():
    uuid = to_uuid("00000000-1111-2222-3333-ABCDEFabcdef")
    assert isinstance(uuid, UUID)
    assert str(uuid) == "00000000-1111-2222-3333-abcdefabcdef"
