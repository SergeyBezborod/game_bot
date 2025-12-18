from validation import *
from controller import *


def save_items_in_bank():
    sleeper(2, "Подготовка")
    for bank_stash_bag in range(0, len(bank_stash_bags)):
        mouse_click(bank_stash_bags[bank_stash_bag][0], bank_stash_bags[bank_stash_bag][1])
        for value_item in range(0, len(items)):
            entry = locate_item(items[value_item][0],
                                items[value_item][1], bank_stash_bags[bank_stash_bag][2], 1093,
                                275, 320, 220)
            if len(entry) > 0:
                if items[value_item][1] == "VIP сундук":
                    for index in range(0, len(entry)):
                        entry1 = locate_item(items[value_item][0], items[value_item][1],
                                             bank_stash_bags[bank_stash_bag][2], 1093, 275, 320, 220)
                        mouse_click_to_item(entry1[0][0] + 1093, entry1[0][1] + 275)
                        mouse_doubleclick_to_item(entry1[0][0] + 1093, entry1[0][1] + 275)
                        print(f"{time.ctime()}: Предмет '{items[value_item][1]}' перемещен в банк")
                        logging(f"Предмет '{items[value_item][1]}' перемещен в банк")
                else:
                    mouse_click_to_item(entry[0][0] + 1093, entry[0][1] + 275)
                    mouse_doubleclick_to_item(entry[0][0] + 1093, entry[0][1] + 275)
                    print(f"{time.ctime()}: Предмет '{items[value_item][1]}' перемещен в банк")
                    logging(f"Предмет '{items[value_item][1]}' перемещен в банк")
            else:
                pass
    mouse_click(1430, 540)
    sleeper(2, "Выход из банка")


def sale_items_in_store():
    sleeper(2, "Подготовка")
    for bank_stash_bag in range(0, len(bank_stash_bags)):
        mouse_click(bank_stash_bags[bank_stash_bag][0], bank_stash_bags[bank_stash_bag][1])
        time.sleep(0.5)
        empty_bag_marker = validate_image("run_data/empty_slots.png", 1093, 275, 320, 220, 0.95)

        for bank_stash_bag_slot in range(0, len(bank_stash_bags_slots)):
            mouse_click_to_item(bank_stash_bags_slots[bank_stash_bag_slot][0],
                                bank_stash_bags_slots[bank_stash_bag_slot][1])
            mouse_doubleclick_to_item(bank_stash_bags_slots[bank_stash_bag_slot][0],
                                      bank_stash_bags_slots[bank_stash_bag_slot][1])
        if empty_bag_marker:
            print(f"{time.ctime()}: В сумке много пустых слотов. Продажа окончена")
            break

    mouse_click(1430, 540)
    sleeper(2, "Выход из магазина")


def use_glad_kris_and_drop_useless_items():
    sleeper(2, "Подготовка")
    mouse_click(1430, 540)
    mouse_click(1310, 315)
    sleeper(5, "Загрузка в инвентарь")
    for stash_bag in range(0, len(stash_bags)):
        mouse_click(stash_bags[stash_bag][0], stash_bags[stash_bag][1])
        sleeper(1, f"Переход в '{stash_bags[stash_bag][2]}'")
        entry = locate_item("run_data/value_items/item_glad_kris.png", "Гладиаторский темный кристалл",
                            stash_bags[stash_bag][2], 1022, 251, 320, 220)
        sleeper(1, f"Поиск 'Гладиаторский темный кристалл' в '{stash_bags[stash_bag][2]}'")
        if len(entry) > 0:
            for index in range(0, len(entry)):
                entry1 = locate_item("run_data/value_items/item_glad_kris.png", "Гладиаторский темный кристалл",
                                     stash_bags[stash_bag][2], 1022, 251, 320, 220)
                time.sleep(0.5)
                mouse_click_to_item(entry1[0][0] + 1022, entry1[0][1] + 251)
                time.sleep(0.5)
                mouse_doubleclick_to_item(entry1[0][0] + 1022, entry1[0][1] + 251)
                sleeper(1, "Ожидание окна подтверждения")
                mouse_click(895, 565)
                print(f"{time.ctime()}: 'Гладиаторский темный кристалл' использован")
                logging("'Гладиаторский темный кристалл' использован")
        else:
            pass
    for stash_bag in range(0, len(stash_bags) - 1):
        mouse_click(stash_bags[stash_bag][0], stash_bags[stash_bag][1])
        mouse_click(1265, 490)
        for stash_bag_slot in range(0, len(stash_bags_slots)):
            mouse_click_to_item(stash_bags_slots[stash_bag_slot][0],
                                stash_bags_slots[stash_bag_slot][1])
            mouse_click(895, 550)
        mouse_click(1265, 490)
    mouse_click(1430, 540)
    sleeper(2, "Выход из инвентаря")


def drop_useless_items():
    sleeper(2, "Подготовка")
    mouse_click(1430, 540)
    mouse_click(1310, 315)
    sleeper(5, "Загрузка в инвентарь")
    for stash_bag in range(0, len(stash_bags) - 1):
        mouse_click(stash_bags[stash_bag][0], stash_bags[stash_bag][1])
        mouse_click(1265, 490)
        for stash_bag_slot in range(0, len(stash_bags_slots)):
            mouse_click_to_item(stash_bags_slots[stash_bag_slot][0],
                                stash_bags_slots[stash_bag_slot][1])
            mouse_click(895, 550)
        mouse_click(1265, 490)
    mouse_click(1430, 540)
    sleeper(2, "Выход из инвентаря")


def use_glad_kris():
    sleeper(2, "Подготовка")
    mouse_click(1430, 540)
    mouse_click(1310, 315)
    sleeper(5, "Загрузка в инвентарь")
    for stash_bag in range(0, len(stash_bags)):
        mouse_click(stash_bags[stash_bag][0], stash_bags[stash_bag][1])
        sleeper(1, "Переход в " + "'" + stash_bags[stash_bag][2] + "'")
        entry = locate_item("run_data/value_items/item_glad_kris.png", "Гладиаторский темный кристалл",
                            stash_bags[stash_bag][2], 1022, 251, 320, 220)
        sleeper(1, "Поиск 'Гладиаторский темный кристалл' в " + "'" + stash_bags[stash_bag][2] + "'")
        if len(entry) > 0:
            for index in range(0, len(entry)):
                entry1 = locate_item("run_data/value_items/item_glad_kris.png", "Гладиаторский темный кристалл",
                                     stash_bags[stash_bag][2], 1022, 251, 320, 220)
                time.sleep(0.5)
                mouse_click_to_item(entry1[0][0] + 1022, entry1[0][1] + 251)
                time.sleep(0.5)
                mouse_doubleclick_to_item(entry1[0][0] + 1022, entry1[0][1] + 251)
                sleeper(1, "Ожидание окна подтверждения")
                mouse_click(895, 565)
                print(f"{time.ctime()}: 'Гладиаторский темный кристалл' использован")
                logging("'Гладиаторский темный кристалл' использован")
        else:
            pass
    mouse_click(1430, 540)
    sleeper(2, "Выход из инвентаря")
