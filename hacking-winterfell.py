import math


class seven_kingdom_army():
    # Get the seven_kingdom_army strengths and army
    def __init__(self, no_of_dragons):
        self.high_troop = no_of_dragons
        self.low_troop = 5000
        self.low_troop_defence = 2
        self.high_troop_defence = 600

    def high_defence(self):
        return self.high_troop * 600

    def low_defence(self):
        return self.low_troop * 2

    def attack_strength(self):
        return self.high_troop * 600 + self.low_troop * 2

    def low_dead(self, dead):
        if dead == 'all':
            self.low_troop = 0
        else:
            self.low_troop -= dead

    def high_dead(self, dead):
        if dead == 'all':
            self.high_troop = 0
        else:
            self.high_troop -= dead

    def __str__(self):
        return f'''
        Seven Kingdoms:
        Attack: {self.attack_strength()},
        Dragons:{self.high_troop}, Infantry: {self.low_troop},
        '''


class white_walker_army():
    # Get the white_walker_army strengths and army
    def __init__(self, no_of_lords):
        self.high_troop = no_of_lords
        self.low_troop = 10000
        self.low_troop_defence = 3
        self.high_troop_defence = 100

    def high_defence(self):
        return self.high_troop * 100

    def low_defence(self):
        return self.low_troop * 3

    def attack_strength(self):
        return self.high_troop * 50 + self.low_troop * 1

    def low_dead(self, dead):
        if dead == 'all':
            self.low_troop = 0
        else:
            self.low_troop -= dead

    def high_dead(self, dead):
        if dead == 'all':
            self.high_troop = 0
        else:
            self.high_troop -= dead

    def __str__(self):
        return f'''
        White Walkers:
        Attack: {self.attack_strength()},
        Lords:{self.high_troop}, Walkers: {self.low_troop},
        '''


def attack(attack_army, defence_army):
    # check if the attack will kill all the high troops first
    print('before attack')
    print(attack_army)
    print(defence_army)

    if defence_army.high_defence() > 0:

        if attack_army.attack_strength() >= defence_army.high_defence():
            # remove all dead high troops
            defence_army.high_dead('all')
            # calculate dead
            if (attack_army.attack_strength() - defence_army.high_defence()) >= defence_army.low_troop_defence:
                dead = math.floor(
                    (attack_army.attack_strength() - defence_army.high_defence()) / defence_army.low_troop_defence)
                # remove dead from remaining low troops
                defence_army.low_dead(dead)
                print(dead)

        elif defence_army.high_defence() > attack_army.attack_strength():
            # calculate high dead
            high_dead = math.floor(attack_army.attack_strength() /
                                   defence_army.high_troop_defence)
            # remove dead from remaining high troops
            defence_army.high_dead(high_dead)

            print(high_dead)

            diff = attack_army.attack_strength() - (high_dead * defence_army.high_troop_defence)

            if diff >= defence_army.low_troop_defence:
                # calculate low dead
                low_dead = math.floor(diff / defence_army.low_troop_defence)
                # remove dead from remaining low troops
                defence_army.low_dead(low_dead)

                print(low_dead)

    elif defence_army.high_defence() <= 0:

        if attack_army.attack_strength() >= defence_army.low_defence():
            # remove all dead high troops
            defence_army.low_dead('all')

        elif attack_army.attack_strength() >= defence_army.low_troop_defence:
            # calculate dead
            dead = math.floor(attack_army.attack_strength() /
                              defence_army.low_troop_defence)
            # remove dead from remaining high troops
            defence_army.low_dead(dead)
            print(dead)

    print('after attack')
    print(attack_army)
    print(defence_army)


def check_if_army_has_troops(army):
    return army.low_troop > 0 or army.high_troop > 0


def run(first_strike_army_name, no_of_dragons, no_of_lords):
    # Some work here; return type and arguments should be according to the problem's requirements
    start = False
    try:
        dragons = int(no_of_dragons)
        lords = int(no_of_lords)
        if dragons >= 0 and lords >= 0:
            start = True
            print("Valid parameter provided")
        else:
            print('Invalid parameter provided')
    except:
        print('Invalid parameter provided')

    if start:
        kingdom_army = seven_kingdom_army(no_of_dragons)

        walker_army = white_walker_army(no_of_lords)

        turn = 1

        if first_strike_army_name.lower() == 'seven kingdom army':

            attack(kingdom_army, walker_army)

            has_troops = check_if_army_has_troops(walker_army)

            if has_troops:
                retaliate = "White Walker Army"
            else:
                print(f'Seven Kingdom Army | {turn}')

            print(first_strike_army_name, turn)
            while retaliate:
                turn += 1
                print(retaliate, turn)

                if retaliate == "White Walker Army":
                    attack(walker_army, kingdom_army)
                    has_troops = check_if_army_has_troops(kingdom_army)

                    if has_troops:
                        retaliate = 'Seven Kingdom Army'

                    else:
                        print(f'White Walker Army | {turn}')
                        break

                elif retaliate == 'Seven Kingdom Army':
                    attack(kingdom_army, walker_army)
                    has_troops = check_if_army_has_troops(walker_army)
                    if has_troops:
                        retaliate = "White Walker Army"

                    else:
                        print(f'Seven Kingdom Army | {turn}')
                        break

        elif first_strike_army_name == 'White Walker Army':

            attack(walker_army, kingdom_army)

            has_troops = check_if_army_has_troops(kingdom_army)

            if has_troops:
                retaliate = 'Seven Kingdom Army'
            else:
                print(f'Seven Kingdom Army | {turn}')

            while retaliate:
                turn += 1

                if retaliate == "White Walker Army":

                    attack(walker_army, kingdom_army)

                    has_troops = check_if_army_has_troops(kingdom_army)

                    if has_troops:
                        retaliate = 'Seven Kingdom Army'
                    else:
                        print(f'White Walker Army | {turn}')
                        break

                elif retaliate == 'Seven Kingdom Army':

                    attack(kingdom_army, walker_army)

                    has_troops = check_if_army_has_troops(walker_army)

                    if has_troops:
                        retaliate = "White Walker Army"
                    else:
                        print(f'Seven Kingdom Army | {turn}')
                        break


run('Seven Kingdom Army', 5, 4)  # White Walker Army | 6
