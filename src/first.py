def get_unique_names(full_names: list[list[str]]) -> list[str]:
    flat = []
    for full_name in full_names:
        flat.extend(full_name)

    only_names = []
    for person in flat:
        name = person[:person.find(' ')]
        only_names.append(name)
    unique_names = set(only_names)
    all_names_sorted = sorted(list(unique_names))

    return all_names_sorted


def get_top_3_names(full_names: list[list[str]]) -> list[list[str, int]]:
    flat = []
    for full_name in full_names:
        flat.extend(full_name)

    only_names = []
    for person in flat:
        name = person[:person.find(' ')]
        only_names.append(name)
    unique_names = set(only_names)

    popular = []
    for name in unique_names:
        popular.append(
            [name, only_names.count(name)])

    popular.sort(key=lambda x: (-x[1], x[0]))

    top_3 = popular[:3]

    return top_3


def get_max_min_duration_courses(courses: list[str],
                                 durations: list[int]) \
        -> dict[str, list[list, int]]:

    courses_list = []
    for title, duration in zip(courses, durations):
        course_dict = {'title': title, 'duration': duration}
        courses_list.append(course_dict)

    min_ = min(durations)
    max_ = max(durations)

    maxes = []
    minis = []

    for index, value in enumerate(durations):
        if value == max_:
            maxes.append(index)
        elif value == min_:
            minis.append(index)

    courses_min = []
    courses_max = []
    for idx in minis:
        courses_min.append(courses_list[idx]['title'])
    for idx in maxes:
        courses_max.append(courses_list[idx]['title'])

    return {
        'short_courses': [courses_min, min_],
        'long_courses': [courses_max, max_]
    }
