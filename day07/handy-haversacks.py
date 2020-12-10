import re

def parse_bags(reversed=False):
    bag_map = {}

    for instruction in open("input").readlines():
        bag_id, contents = re.split(r"\sbags\scontain\s", instruction.strip())
        contents = re.split(r"(?:no\sother)?\sbags?[,\.]\s?", contents)

        for content in contents:
            if content:
                parent_bag_id = bag_id
                child_bag_id = content[2:]
                child_amount = int(content[0])
                if reversed:
                    parent_bag_id, child_bag_id = child_bag_id, parent_bag_id
                bags = bag_map.get(parent_bag_id, {})
                bags[child_bag_id] = child_amount
                bag_map[parent_bag_id] = bags

    return bag_map

def part_one():
    bags = parse_bags(reversed=True)
    searched = set()
    to_search = set(bags["shiny gold"].keys())

    while to_search:
        new_bags = set()
        for bag in to_search:
            for child in bags.get(bag, {}).keys():
                if child not in searched:
                    new_bags.add(child)
            searched.add(bag)
        to_search = new_bags

    return len(searched)


def part_two():
    bags = parse_bags()

    def count_inner(bag_id):
        children = bags[bag_id]
        return sum(map(
            lambda child_id: (
                (count_inner(child_id) + 1 if bags.get(child_id) else 1) * 
                children[child_id]),
            children))

    return count_inner("shiny gold")

print(part_one())
print(part_two())
