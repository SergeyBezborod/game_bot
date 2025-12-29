from inventory import *
from farming import *
from teleportation import *
from game_start_reload import *


def global_run_and_farm(personage, event):
    loop_t_start = time.time()
    event.wait()
    loc_counter = 0
    for s_reg in range(0, len(s_regs)):
        event.wait()
        if s_reg_tp(s_regs[s_reg][0], s_regs[s_reg][1], s_regs[s_reg][2],
                    s_regs[s_reg][3], s_regs[s_reg][4], s_regs[s_reg][5],
                    s_regs[s_reg][6]):
            event.wait()
            reload_game(personage)
            for reg in range(0, len(f_regs)):
                if f_regs[reg][2] == s_regs[s_reg][4]:
                    if f_reg_tp(f_regs[reg][0], f_regs[reg][1], f_regs[reg][2], f_regs[reg][3], f_regs[reg][4]):
                        event.wait()
                        for loc in range(0, len(locs)):
                            if locs[loc][2] == f_regs[reg][3]:
                                if len(locs[loc]) > 8:
                                    move_map(locs[loc][8], locs[loc][9])

                                event.wait()
                                if move_to_loc(locs[loc][0], locs[loc][1], locs[loc][3], locs[loc][4], locs[loc][5]):
                                    event.wait()
                                    if open_loc(locs[loc][0], locs[loc][1], locs[loc][3]):
                                        event.wait()
                                        farm_loc(locs[loc][3], locs[loc][6], locs[loc][7], personage, event)
                                        event.wait()
                                        loc_counter = loc_counter + 1
                                        logging(f"Счётчик локаций: {loc_counter}")
                                    else:
                                        """Если не открылась локация"""
                                        event.wait()
                                        pass
                                else:
                                    """Если не прибежал к следующей локации"""
                                    event.wait()
                                    pass
                    else:
                        """Если не перемещён в регион фарма"""
                        event.wait()
                        pass

            if s_regs[s_reg][4] == "Метаноя" or s_regs[s_reg][4] == "Панфобион" or s_regs[s_reg][4] == "Харангер-Фьёрд":
                if s_reg_tp(0, 0, s_regs[s_reg][2], s_regs[s_reg][3], s_regs[s_reg][4],
                            s_regs[s_reg][5], s_regs[s_reg][6]):
                    event.wait()
                    if bank_enter(s_regs[s_reg][7], s_regs[s_reg][8], s_regs[s_reg][9],
                                  s_regs[s_reg][10], s_regs[s_reg][11], s_regs[s_reg][12]):
                        event.wait()
                        save_items_in_bank()
                        event.wait()
                        if store_enter(s_regs[s_reg][13], s_regs[s_reg][14], s_regs[s_reg][15], s_regs[s_reg][16],
                                       s_regs[s_reg][17],  s_regs[s_reg][18], s_regs[s_reg][19], s_regs[s_reg][20]):
                            event.wait()
                            sale_items_in_store()
                            event.wait()
                            use_glad_kris()
                            event.wait()
                        else:
                            """Если не зашли в магазин"""
                            event.wait()
                            pass
                    else:
                        """Если не зашли в банк"""
                        event.wait()
                        pass
                else:
                    """Если не перемещён в безопасный регион после фарма"""
                    event.wait()
                    pass
        else:
            """Если не перемещён в безопасный регион в начале фарма"""
            event.wait()
            pass

    if k_city_tp():
        event.wait()
        if k_bank_enter():
            event.wait()
            save_items_in_bank()
            event.wait()
            if k_store_enter():
                event.wait()
                sale_items_in_store()
                event.wait()
                use_glad_kris_and_drop_useless_items()
                event.wait()
            else:
                """Если не зашли в магазин"""
                event.wait()
                pass
        else:
            """Если не зашли в банк"""
            event.wait()
            pass
    else:
        """Если не перемещён в безопасный регион после фарма"""
        event.wait()
        pass

    loop_t_finish = time.time()
    loop_t = loop_t_finish - loop_t_start
    logging(f"Время круга: {int(loop_t // 3600)}ч {int((loop_t // 60) % 60)}м {int(loop_t % 60)}c")
