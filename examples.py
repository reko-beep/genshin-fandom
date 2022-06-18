import client


def get_character_data(character_name: str):
    '''

    gets character data

    '''

    client_ = client.Client()

    char_obj = client_.filter_item(character_name, client_.characters)
    if char_obj is not None:
        return char_obj.get_data().data


test_char = get_character_data('eula')