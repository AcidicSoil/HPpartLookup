
def main():
    endList()
    mark_up_list()
    


def mark_up(n):
    if n > 50:
        i = n * 0.3
    elif n < 50:
        i = n * 0.5
    return n + i

#number_of_items = input("Enter total number of items to be marked up: ")

#item_prices = input("Enter item prices to be marked up: " )


not_marked_up_item_list = [294.99, 64.90, 199.99, 119.99, 159.99]
#199.99, 199.99, 769.99
marked_up_list = [mark_up(i) for i in not_marked_up_item_list]
print(sum(marked_up_list) + 120)


end_of_list = False

def endList():
    while len(not_marked_up_item_list) > 0:
        end_of_list = False
        return
        if len(not_marked_up_item_list) == 0:
            end_of_list = True
            return
        else:
            end_of_list = False
            return
def mark_up_list():
    for i in not_marked_up_item_list:
        end_of_list()
        mark_up(i)
        #not_marked_up_item_list.append(item_prices)
        end_of_list()
        print(not_marked_up_item_list)
        break
#main()
