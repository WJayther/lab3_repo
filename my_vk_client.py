import VK_get_id
import VK_parser


if __name__ == '__main__':
    str_id = input('Type some ID: ')
    test = VK_get_id.GetIDFromUsername(str_id)
    uid = test.execute()
    test = VK_parser.ParseFriends(uid)
    print(test.execute())
