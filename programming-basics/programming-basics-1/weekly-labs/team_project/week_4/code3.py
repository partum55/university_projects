"""
Code 3
"""


def analyze_student_scores(input_file: str, output_file: str) -> list[dict]:
    """
    Prorgam that read data, count average scores and output this data
    :param input_file: name of file, from where to read data
    :param output_file: name of file, where to write data
    :return: list of dictionaries with our data
    """
    with open(input_file, 'r', encoding="utf-8") as file:
        results = []
        for line in file:
            name, scores = line.strip().split(':')
            scores = scores.split(',')
            total = 0
            highest = 0
            for score in scores:
                score = int(score)
                total += score
                highest = max(score, highest)
            average = total / len(scores)
            failed = average < 75
            results.append({
                'name' : name,
                'average': average,
                'highest': highest,
                'failed': failed
            })
    with open (output_file, 'w', encoding="utf-8") as file:
        output_file = f"{results[0].values()}".strip("dict_values()[]")
        file.write(output_file + "\n")
        for line in results:
            output_file = f"{line.values()}".strip("dict_values()[]")
            file.write(output_file + "\n")
    return results
