import re

rules_up = {}
rules_down = {}
rule_pattern = re.compile(r'^(.+) bags contain (.+)')
bag_pattern = re.compile(r'(\d+) (.+?) bags?')

with open('input.txt', 'r') as input:
    for line in input:
        m_rule = rule_pattern.match(line.strip())
        color = m_rule.group(1)
        if color not in rules_down:
            rules_down[color] = {}
        bags = [elm.strip() for elm in m_rule.group(2).split(',')]
        for bag in bags:
            m_bag = bag_pattern.match(bag)
            if m_bag is None:
                continue
            count = m_bag.group(1)
            bag_color = m_bag.group(2)
            if bag_color not in rules_up:
                rules_up[bag_color] = {}
            rules_up[bag_color][color] = int(count)
            rules_down[color][bag_color] = int(count)


    def explore_color(color, explored):
        for k in rules_up[color].keys():
            if k not in explored:
                explored[k] = None
                if k in rules_up:
                    explored = explore_color(k, explored)
        return explored


    def count_down(color):
        count = 0
        for k, v in rules_down[color].items():
            count += v + v * count_down(k)
        return count


    print("Part 1:", len(explore_color('shiny gold', {}).keys()))

    print("Part 2:", count_down('shiny gold'))
