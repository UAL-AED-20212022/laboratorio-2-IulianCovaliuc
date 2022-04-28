from models.LinkedList import LinkedList
from models.Node import Node


def main():
    lista = LinkedList()
    while True:
        user_data = input().split()
        if user_data[0] == "RPI":
            lista.insert_at_start(user_data[1])
            lista.traverse_list()
        if user_data[0] == "RPF":
            lista.insert_at_end(user_data[1])
            lista.traverse_list()
        if user_data[0] == "RPDE":
            lista.insert_after_item(user_data[2], user_data[1])
            lista.traverse_list()
        if user_data[0] == "RPAE":
            lista.insert_before_item(user_data[2], user_data[1])
            lista.traverse_list()
        if user_data[0] == "RPII":
            lista.insert_at_index(int(user_data[2]), user_data[1])
            lista.traverse_list()
        if user_data[0] == "VNE":
            print(f"O número de elementos são {lista.get_count()}.")
        if user_data[0] == "VP":
            if lista.search_item(user_data[1]):
                print(f"O país {user_data[1]} encontra-se na lista.")
            else:
                print(f"O país {user_data[1]} não se encontra na lista.")
        if user_data[0] == "EPE":
            print(f"O país {lista.start_node.get_item()} foi eliminado da lista.")
            lista.delete_at_start()
        if user_data[0] == "EUE":
            print(f"O país {lista.get_last_node()} foi eliminado da lista.")
            lista.delete_at_end()
        if user_data[0] == "EP":
            lista.delete_element_by_value(user_data[1])
            print("item found")
            print(f"O país",user_data[1],"foi eliminado da lista.")
