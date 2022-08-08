def display_inventory(inventory):
    print("持ち物リスト:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total += v
    print("アイテム総数:" + str(item_total))

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inv = {'金貨':42, 'ロープ': 1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']
inv = add_to_inventory(inv, dragon_loot)
#  = {'ロープ': 1, 'たいまつ': 6, '金貨': 42, '手裏剣': 1, '矢': 12}
display_inventory(inv)