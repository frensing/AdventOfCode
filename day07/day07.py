import re

rules = {}
rule_pattern = re.compile(r'^(.+) bags contain (.+)')
bag_pattern = re.compile(r'(\d+) (.+?) bags?')

with open('input.txt', 'r') as input:
    for line in input:
        m_rule = rule_pattern.match(line.strip())
        color = m_rule.group(1)
        bags = [elm.strip() for elm in m_rule.group(2).split(',')]
        for bag in bags:
            m_bag = bag_pattern.match(bag)
            if m_bag is None:
                continue
            count = m_bag.group(1)
            bag_color = m_bag.group(2)
            if bag_color not in rules:
                rules[bag_color] = {}
            rules[bag_color][color] = count


    def explore_color(color, explored):
        for k in rules[color].keys():
            if k not in explored:
                explored[k] = None
                if k in rules:
                    explored = explore_color(k, explored)
        return explored


    outer_bags = explore_color('shiny gold', {}).keys()

    print("Part 1:", len(outer_bags))
